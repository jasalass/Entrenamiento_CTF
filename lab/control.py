#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Orquestador del laboratorio: sirve el panel, descargas y levanta/para maquinas.
Autodescubre lab/machines/*/meta.json. Usa 'docker compose' por maquina.

Ejecutar:
    python3 lab/control.py
Variables de entorno:
    LAB_BIND  (por defecto 127.0.0.1; usa 0.0.0.0 para acceder desde otra maquina)
    LAB_PORT  (por defecto 8000)

Seguridad: este servicio puede ejecutar Docker en el host. No lo expongas a redes
no confiables. Para atacar desde Kali a EC2, corre esto en el host de Docker.
"""
import os, json, subprocess, re
from flask import Flask, request, jsonify, send_from_directory, abort

LAB_DIR  = os.path.dirname(os.path.abspath(__file__))
ROOT     = os.path.dirname(LAB_DIR)                 # carpeta roadmap/
MACHINES = os.path.join(LAB_DIR, "machines")
ID_RE    = re.compile(r"^[a-zA-Z0-9_-]+$")

app = Flask(__name__)

def discover():
    out = {}
    if not os.path.isdir(MACHINES):
        return out
    for name in sorted(os.listdir(MACHINES)):
        d = os.path.join(MACHINES, name)
        mj = os.path.join(d, "meta.json")
        cj = os.path.join(d, "docker-compose.yml")
        if os.path.isfile(mj) and os.path.isfile(cj):
            try:
                meta = json.load(open(mj, encoding="utf-8"))
            except Exception:
                meta = {}
            meta["id"] = name
            meta["dir"] = d
            out[name] = meta
    return out

def project(mid):
    return "lab_" + re.sub(r"[^a-z0-9]+", "_", mid.lower())

def compose(mid, *args, timeout=900):
    m = discover().get(mid)
    if not m:
        return 1, "", "maquina desconocida"
    cmd = ["docker", "compose", "-p", project(mid),
           "-f", os.path.join(m["dir"], "docker-compose.yml")] + list(args)
    try:
        p = subprocess.run(cmd, cwd=m["dir"], capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except FileNotFoundError:
        return 127, "", "no se encontro 'docker'. Instala Docker + plugin compose."
    except subprocess.TimeoutExpired:
        return 124, "", "timeout ejecutando docker compose"

def running(mid):
    rc, out, _ = compose(mid, "ps", "-q", timeout=30)
    return rc == 0 and bool(out.strip())

# ---------- API ----------
@app.get("/api/machines")
def api_machines():
    res = []
    for mid, m in discover().items():
        res.append({"id": mid, "nombre": m.get("nombre", mid),
                    "enfoque": m.get("enfoque", ""), "dificultad": m.get("dificultad", 1),
                    "puerto": m.get("puerto"), "proto": m.get("proto", "http"),
                    "running": running(mid)})
    return jsonify(res)

@app.post("/api/machines/<mid>/start")
def api_start(mid):
    if not ID_RE.match(mid):
        abort(400)
    rc, out, err = compose(mid, "up", "-d", "--build")
    m = discover().get(mid, {})
    return jsonify({"ok": rc == 0, "running": running(mid),
                    "puerto": m.get("puerto"), "proto": m.get("proto", "http"),
                    "log": (out + err)[-4000:]})

@app.post("/api/machines/<mid>/stop")
def api_stop(mid):
    if not ID_RE.match(mid):
        abort(400)
    rc, out, err = compose(mid, "down")
    return jsonify({"ok": rc == 0, "running": running(mid), "log": (out + err)[-4000:]})

# ---------- progreso (persistente en progress.json) ----------
PROGRESS = os.path.join(ROOT, "progress.json")

@app.get("/api/progress")
def api_progress_get():
    try:
        with open(PROGRESS, encoding="utf-8") as f:
            return jsonify(json.load(f))
    except Exception:
        return jsonify({"solved": {}})

@app.post("/api/progress")
def api_progress_set():
    data = request.get_json(silent=True) or {}
    solved = data.get("solved", {})
    if not isinstance(solved, dict):
        abort(400)
    try:
        with open(PROGRESS, "w", encoding="utf-8") as f:
            json.dump({"solved": solved}, f, ensure_ascii=False, indent=1)
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
    return jsonify({"ok": True, "count": len(solved)})

# ---------- estaticos (panel, manifest, lab.js, descargas de retos) ----------
@app.get("/")
def index():
    return send_from_directory(ROOT, "panel.html")

# Solo se sirve lo que el panel necesita. Antes se servia TODO el arbol: eso exponia
# SOLUCIONES.md (flags en claro) y el codigo/flags de lab/machines/ por HTTP.
PUBLIC_FILES = {"panel.html", "manifest.js"}
PUBLIC_DIRS  = ("retos/",)

@app.get("/<path:p>")
def static_files(p):
    root = os.path.realpath(ROOT)
    full = os.path.realpath(os.path.join(root, p))
    if os.path.commonpath([full, root]) != root:
        abort(403)                      # anti path traversal (por ruta, no por prefijo de texto)
    rel = os.path.relpath(full, root).replace(os.sep, "/")   # ya resuelto: sin '..'
    if os.path.basename(rel) == "flag.txt":
        abort(404)                      # nunca servir flags por HTTP, caiga donde caiga
    if rel not in PUBLIC_FILES and not rel.startswith(PUBLIC_DIRS):
        abort(404)
    if not os.path.isfile(full):
        abort(404)
    return send_from_directory(root, rel)

if __name__ == "__main__":
    bind = os.environ.get("LAB_BIND", "127.0.0.1")   # como documenta el docstring/README
    port = int(os.environ.get("LAB_PORT", "8000"))
    print(f"[lab] panel en http://{bind}:{port}/  (maquinas: {', '.join(discover()) or 'ninguna'})")
    app.run(host=bind, port=port)
