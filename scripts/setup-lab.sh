#!/usr/bin/env bash
# Prepara el host (EC2) y arranca el orquestador del lab como servicio systemd.
# Idempotente: se puede ejecutar en cada deploy sin romper nada.
#
# Se espera que la carpeta del lab ya este sincronizada en $LAB_HOME/roadmap
# (lo hace el workflow con rsync). El panel queda escuchando SOLO en 127.0.0.1
# a proposito (control.py puede ejecutar Docker en el host): se accede por tunel
# SSH, no se publica a Internet.
set -euo pipefail

LAB_USER="$(id -un)"
LAB_HOME="$(eval echo "~${LAB_USER}")"
LAB_DIR="${LAB_HOME}/roadmap"

echo "[setup] usuario=${LAB_USER} dir=${LAB_DIR}"

# --- dependencias (solo si faltan) ---------------------------------------
need_apt=0
command -v docker  >/dev/null 2>&1 || need_apt=1
command -v python3 >/dev/null 2>&1 || need_apt=1
python3 -c 'import flask' >/dev/null 2>&1 || need_apt=1
docker compose version >/dev/null 2>&1 || need_apt=1

if [ "$need_apt" = "1" ]; then
  echo "[setup] instalando dependencias..."
  export DEBIAN_FRONTEND=noninteractive
  sudo apt-get update -y
  sudo apt-get install -y docker.io docker-compose-v2 python3-flask rsync
fi

# docker activo y el usuario en el grupo docker (para 'docker compose' sin sudo)
sudo systemctl enable --now docker
if ! id -nG "$LAB_USER" | tr ' ' '\n' | grep -qx docker; then
  sudo usermod -aG docker "$LAB_USER"
fi

# --- servicio systemd del orquestador ------------------------------------
echo "[setup] escribiendo servicio ctf-lab..."
sudo tee /etc/systemd/system/ctf-lab.service >/dev/null <<EOF
[Unit]
Description=CTF Lab orchestrator (panel + docker compose por maquina)
After=docker.service
Requires=docker.service

[Service]
User=${LAB_USER}
WorkingDirectory=${LAB_DIR}
Environment=LAB_BIND=127.0.0.1
Environment=LAB_PORT=8000
ExecStart=/usr/bin/python3 ${LAB_DIR}/lab/control.py
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable ctf-lab
sudo systemctl restart ctf-lab

sleep 2
systemctl is-active --quiet ctf-lab \
  && echo "[setup] OK: ctf-lab activo en 127.0.0.1:8000" \
  || { echo "[setup] ERROR: ctf-lab no arranco"; sudo systemctl status ctf-lab --no-pager -l || true; exit 1; }
