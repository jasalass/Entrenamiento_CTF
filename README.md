# 🗺️ CTF · Curso progresivo de 50 días (100% local, para Kali Linux)

> 👉 **Ruta recomendada:** sigue [`CURSO.md`](CURSO.md) (curso por módulos, 100% local). Este
> README describe el material (los 260 retos y el lab); el curso decide en qué orden hacerlos.

Entrenamiento autocontenido y **100% local**: nada depende de plataformas externas ni de eventos
en vivo. Todo se resuelve contra **tu propio material y tus propias máquinas Docker** — en tu
Kali local o, si prefieres, desplegando el lab en **tu propia EC2** y atacándola desde Kali
(ver [`lab/README.md`](lab/README.md)).

**Días 1–30:** 8 retos por día (uno de cada enfoque clásico) = **240 retos**, dificultad
creciente (N1 fácil → N4 avanzado).
**Días 31–42:** **12 retos de explotación de binarios real** (Pwn-Bin: stack overflow, ret2win,
format string leak/write) — máquinas Docker nuevas, progresivas, distintas de la privesc de abajo.
**Días 43–50:** **8 retos de ingeniería inversa a ciegas** (binarios compilados **sin** el `.c`,
como en un CTF real: el binario solo dice "correcto"/"incorrecto", nunca imprime la flag).

**Total: 260 retos.**

Enfoques: **Crypto, Encoding, Stego, Forensics, OSINT, Reversing, Web, Pwn, Pwn-Bin**.

## Tipos de reto (todos dentro de los 260)

- **Archivos (análisis) — 188:** Crypto, Encoding, Stego, Forensics, OSINT y Reversing (incluye
  los 8 binarios de reversing ciego, días 43-50). Se **descargan** desde el panel y se resuelven
  con herramientas locales en Kali.
- **Máquinas (infraestructura) — 60:** los retos de **Web** y **Pwn** (días 1-30) son contenedores
  vulnerables que **levantas bajo demanda** desde la propia tarjeta del reto y atacas por red
  (nmap/gobuster/sqlmap/curl → shell → privesc). Ver [`lab/README.md`](lab/README.md).
- **Pwn-Bin (híbrido, binario + máquina) — 12:** días 31-42. Te **descargas el binario exacto**
  que corre en el contenedor (mismo archivo, byte a byte) para analizarlo offline con
  Ghidra/objdump/gdb, y **levantas la máquina** para explotarlo de verdad contra un socket TCP
  (`nc IP puerto`) — igual que un servicio pwn en un CTF real.

## Si te trabas: pide ayuda a cualquier LLM sin arruinarte el reto

Los retos de **Pwn-Bin** y **Reversing ciego** terminan su lista de pistas con un
🤖 **prompt listo para copiar y pegar** en cualquier LLM (ChatGPT, Claude, Gemini, lo que tengas
a mano). El prompt le pide a ese LLM que te haga **preguntas y te dé pistas una a la vez**, nunca
el exploit o la solución completa — pégale también la salida de tu `objdump`/`gdb`/Ghidra para que
pueda orientarte sobre TU binario concreto. Es un asistente socrático de bolsillo para cuando el
material y las pistas del panel no alcanzaron.

## Cómo empezar

**Modo simple (solo archivos):** abre **`panel.html`** en el navegador (funciona sin internet):
guía + descargas + validador + progreso. Pega la flag `FLAG{...}` y **Validar** (por SHA-256;
las flags nunca están en claro en la web).

**Modo completo (archivos + máquinas):** sirve el panel con el orquestador para tener los botones
de **Levantar máquina** y las descargas por HTTP:
```bash
cd roadmap
python3 lab/control.py        # por defecto solo en http://127.0.0.1:8000/
```
Desde la VM de Kali atacas al objetivo `IP:puerto` que indica cada máquina (`http://`, `ssh` o
`nc` según el reto). El panel por defecto **solo escucha en localhost** aunque los contenedores
vulnerables sí quedan accesibles en red — así puedes manejarlo por SSH tunnel incluso si el lab
vive en una EC2 (ver [`lab/README.md`](lab/README.md) para el detalle de exposición remota).

## Plan de estudio y tutor
- [`CURSO.md`](CURSO.md): **el curso progresivo** (10 módulos, 100% local, exámenes de salida). Empieza aquí.
- [`CURSO_PROGRESO.md`](CURSO_PROGRESO.md): tu checklist de avance por módulo y examen de salida.
- [`PLAN_DE_ESTUDIO.md`](PLAN_DE_ESTUDIO.md): diagnóstico del material, método de trabajo, hoja de triage, MCP recomendados y ética.
- [`CLAUDE.md`](CLAUDE.md): instrucciones para que Claude te guíe como mentor (sin darte las flags).
- [`writeups/`](writeups/): plantilla y tus writeups.

## Estructura

```
roadmap/
├── panel.html     ← LA WEB: guía + validador + descargas + botón "Levantar máquina"
├── manifest.js    ← datos de los 260 retos (archivo, máquina o pwnbin-híbrido)
├── SOLUCIONES.md  ← ⚠️ spoilers: todas las flags (solo para comprobar; NO se sirve por HTTP)
├── README.md
├── retos/         ← archivos descargables
│   ├── dia-01/{crypto,encoding,stego,forensics,osint,reversing}/ … dia-30/
│   ├── pwnbin/pwnbin-31/chal … pwnbin-42/chal   (binario exacto del contenedor, sin flag)
│   └── revbin/revbin-43/chal … revbin-50/chal   (reversing ciego, sin .c)
└── lab/           ← infraestructura (días 1-30 Web/Pwn + días 31-42 Pwn-Bin)
    ├── control.py           ← orquestador (sirve panel + Levantar/Detener; lista blanca estricta)
    ├── README.md
    └── machines/
        ├── d01-web/ … d30-web/       (puerto 8000+día, http)
        ├── d01-pwn/ … d30-pwn/       (puerto 8100+día, ssh ctf:ctf)
        └── pwnbin-31/ … pwnbin-42/   (puerto 8200+N, tcp/nc — explotación de binarios real)
```

## Progresión por enfoque (N1→N4 a lo largo de los 50 días)

| Enfoque | Técnicas que recorres |
|---|---|
| **Crypto** | César → Vigenère → XOR (1 byte y clave repetida) → RSA factorizable / crackeo de hash MD5 |
| **Encoding** | 1 capa → hasta 4 capas encadenadas (Base64/32/85, hex, binario, ROT13, invertido) |
| **Stego** | LSB 1 canal → LSB RGB → metadatos (exiftool) → datos tras EOF → caracteres invisibles |
| **Forensics** | strings → Base64 embebido → hex plano → ZIP embebido (carving) → gzip |
| **OSINT** | correlación de 2 fuentes → hasta 4 fuentes con fragmentos codificados |
| **Reversing** | XOR constante → XOR posicional → add+XOR → cifrado por retroalimentación |
| **Web** (máquina) | command injection → cookie/autorización → IDOR → path traversal (LFI) → SSRF → SQLi (login) → SQLi UNION → JWT `alg:none` → SSTI (Jinja2) → XXE |
| **Pwn/Privesc** (máquina) | SUID → sudo (find/awk/python, GTFOBins) → `/etc/passwd` escribible → PATH hijack → cron writable → capabilities (`cap_dac_read_search`, `cap_setuid`) → sudo + `LD_PRELOAD` |
| **Pwn-Bin** (pwnbin-híbrido, días 31-42) | overflow de variable local → ret2win (secuestro de flujo) → format string leak → format string write (`%n`) |
| **Reversing ciego** (archivo, días 43-50) | mismas 4 técnicas que Reversing (XOR const/posicional, add+XOR, retroalimentación) pero **sin el `.c`**: solo tienes el binario compilado y debes decompilarlo tú mismo |

> ℹ️ **"Pwn" (días 1-30) = escalada de privilegios en Linux**; **"Pwn-Bin" (días 31-42) = explotación
> de binarios real** (overflow, ret2win, format string) — ver módulos M4 y M7 de [`CURSO.md`](CURSO.md).
>
> **Reversing (días 1-30)** es de análisis (fuente C) y trae `Makefile` (`make && ./check`).
> **Reversing ciego (días 43-50)** no trae fuente: el binario solo responde "correcto"/"incorrecto",
> así que tienes que decompilar con Ghidra/objdump de verdad, como en un CTF real.
> **Web** y **Pwn** son **máquinas** que levantas y atacas por red (ver [`lab/README.md`](lab/README.md)).
> **Pwn-Bin** es ambas cosas a la vez: descargas el binario para analizarlo offline y levantas la
> máquina para explotarlo contra un socket TCP real (`nc IP puerto`).

## Arsenal Kali por enfoque
- **Crypto:** `tr` (César/ROT), `xortool`, `hashid`, `hashcat`, `john`, `RsaCtfTool`, `openssl`, `python3`+`sympy`
- **Encoding:** `base64`, `basenc`, `xxd`, `tr`, `rev` — decodificación manual capa a capa (encadena los comandos en pipeline; `file`/`strings` te dicen qué capa es cada una)
- **Stego:** `zsteg`, `stegsolve`, `steghide`, `binwalk`, `foremost`, `exiftool`, `strings`, `pngcheck`
- **Forensics:** `file`, `binwalk`, `foremost`, `strings`, `xxd`, `exiftool`, `zcat`, `unzip`
- **OSINT:** `exiftool`, `strings`, `grep`
- **Reversing (con y sin fuente):** `file`, `strings`, `objdump -d`, `radare2`/`r2`, `gdb`, `ghidra`
- **Web:** `curl`, `burpsuite`, `gobuster`/`ffuf`, `nikto`, `whatweb`, `jwt_tool`, DevTools
- **Pwn:** `linpeas`, `pspy`, `find / -perm -4000`, `sudo -l`, GTFOBins, `gdb`, `pwntools`
- **Pwn-Bin:** `checksec` (pwntools), `objdump -d -M intel`, `nm`, `gdb`/`pwndbg`, `python3`+`pwntools`
  (`cyclic`/`cyclic_find`), `nc`/`socat`

## Regenerar
Los 260 artefactos se crearon con scripts (flags con token aleatorio incrustado, verificadas
resolviéndolas una a una de extremo a extremo contra el binario real). Si quieres regenerarlas
con flags nuevas, pídemelo.

> Practica solo contra este material y contra tu propia máquina/VM. Nunca contra sistemas de terceros.
