#!/usr/bin/env bash
# Prepara el host (EC2) y arranca el orquestador del lab como servicio systemd.
# Idempotente: se puede ejecutar en cada deploy sin romper nada.
# Soporta Amazon Linux (dnf/yum) y Debian/Ubuntu (apt-get).
#
# Se espera que la carpeta del lab ya este sincronizada en $LAB_HOME/roadmap
# (lo hace el workflow con rsync). El panel queda escuchando SOLO en 127.0.0.1
# a proposito (control.py puede ejecutar Docker en el host): se accede por tunel
# SSH, no se publica a Internet.
set -euo pipefail

LAB_USER="$(id -un)"
LAB_HOME="$(eval echo "~${LAB_USER}")"
LAB_DIR="${LAB_HOME}/roadmap"
# Interfaz donde escucha el panel. 0.0.0.0 = accesible por red (lab personal:
# restringe el puerto 8000 a tu IP en el Security Group). 127.0.0.1 = solo por
# tunel SSH. Override: LAB_BIND=127.0.0.1 bash setup-lab.sh
LAB_BIND="${LAB_BIND:-0.0.0.0}"

echo "[setup] usuario=${LAB_USER} dir=${LAB_DIR} bind=${LAB_BIND}"

# --- detectar gestor de paquetes -----------------------------------------
if   command -v dnf     >/dev/null 2>&1; then PKG=dnf
elif command -v yum     >/dev/null 2>&1; then PKG=yum
elif command -v apt-get >/dev/null 2>&1; then PKG=apt
else echo "[setup] ERROR: no encuentro dnf/yum/apt-get"; exit 1; fi
echo "[setup] gestor de paquetes: ${PKG}"

pkg_install() {   # pkg_install paquete...
  case "$PKG" in
    dnf) sudo dnf install -y "$@" ;;
    yum) sudo yum install -y "$@" ;;
    apt) sudo DEBIAN_FRONTEND=noninteractive apt-get install -y "$@" ;;
  esac
}

# --- dependencias ---------------------------------------------------------
echo "[setup] instalando dependencias..."
if [ "$PKG" = "apt" ]; then
  sudo apt-get update -y
  pkg_install docker.io docker-compose-v2 python3-flask rsync
else
  # Amazon Linux: docker + python en los repos; compose y flask aparte
  pkg_install docker python3 python3-pip rsync
fi

# docker activo y usuario en el grupo docker (para 'docker compose' sin sudo)
sudo systemctl enable --now docker
if ! id -nG "$LAB_USER" | tr ' ' '\n' | grep -qx docker; then
  sudo usermod -aG docker "$LAB_USER"
fi

# compose v2: en Amazon Linux no viene; instalar el plugin si falta
if ! docker compose version >/dev/null 2>&1; then
  echo "[setup] instalando plugin docker compose v2..."
  COMPOSE_VER="v2.29.7"
  ARCH="$(uname -m)"   # x86_64 / aarch64
  sudo mkdir -p /usr/libexec/docker/cli-plugins
  sudo curl -fsSL \
    "https://github.com/docker/compose/releases/download/${COMPOSE_VER}/docker-compose-linux-${ARCH}" \
    -o /usr/libexec/docker/cli-plugins/docker-compose
  sudo chmod +x /usr/libexec/docker/cli-plugins/docker-compose
fi

# flask: si el import falla (Amazon Linux), instalar con pip
if ! python3 -c 'import flask' >/dev/null 2>&1; then
  echo "[setup] instalando Flask con pip..."
  sudo python3 -m pip install --upgrade flask \
    || sudo python3 -m pip install --break-system-packages --upgrade flask
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
Environment=LAB_BIND=${LAB_BIND}
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
