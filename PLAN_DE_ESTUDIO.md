# 🧭 Plan de estudio · CTF y ciberseguridad (100% local)

Este plan ordena el material de `roadmap/` y documenta el diagnóstico, el método de trabajo y la
hoja de triage. La progresión completa por módulos (con examen de salida) vive en
[`CURSO.md`](CURSO.md); sigue ese documento con Claude como mentor (ver [`CLAUDE.md`](CLAUDE.md)).

---

## 1. Diagnóstico del material

**Lo que ya está muy bien**
- 260 retos con progresión N1→N4, validación por hash, guía paso a paso por reto (`concepto`,
  `pistas`, `pasos` en `manifest.js`).
- Un lab Docker reproducible (72 máquinas: 60 de Web/Pwn-privesc + 12 de Pwn-Bin) con orquestador
  y progreso persistente — corre igual en tu Kali local o en tu propia EC2.
- Un método pedagógico sano: entender la técnica antes de teclear.

**Brechas que tenía este taller respecto a un CTF real, y cómo se cerraron**

| Brecha | Antes | Ahora |
|---|---|---|
| "Pwn" no era pwn | Las 30 máquinas Pwn son *privesc* Linux (SUID, sudo, cron, capabilities) — útil, pero no es "pwn" en el sentido de un CTF | Se agregaron **12 máquinas `Pwn-Bin` (días 31-42)**: overflow de variable local, ret2win, format string leak/write — explotación de binarios real, contra un socket TCP, con el mismo binario que te descargas para analizar offline |
| Reversing sin binarios reales | Los 30 retos de Reversing traen `check.c`: se pueden resolver leyendo el código fuente | Se agregaron **8 binarios de Reversing ciego (días 43-50)**: compilados sin fuente, el programa solo dice "correcto"/"incorrecto", hay que decompilar de verdad (Ghidra/objdump) |
| Stego y Forensics repiten 5 técnicas | Cada uno rota las mismas 5 variantes por nivel | Sigue siendo así — es una limitación conocida; si quieres más variedad en estas dos categorías, pídemelo y genero variantes nuevas (pcap, chunks PNG, espectrograma de audio) |
| Crypto acotada | César → Vigenère → XOR → RSA factorizable / MD5 | Sigue siendo así para el curso base; ataques más avanzados (Wiener, padding oracle, AES-CBC) quedan para el "Nivel 2" de `CURSO.md` |

**Incoherencias detectadas y corregidas**
- `lab/control.py` documentaba escuchar en `127.0.0.1` pero el código usaba `0.0.0.0`: con Docker
  en el host, cualquiera en tu red podía levantar contenedores. El valor por defecto ahora es
  `127.0.0.1`.
- El servidor entregaba **cualquier archivo** del árbol: `SOLUCIONES.md` (todas las flags) y el
  código/flags de `lab/machines/` eran descargables desde el navegador. Ahora solo sirve
  `panel.html`, `manifest.js` y `retos/` — con una lista blanca que se evalúa sobre la ruta ya
  resuelta (no sobre el texto crudo, para que `retos/../SOLUCIONES.md` tampoco funcione) y que
  nunca sirve un archivo llamado `flag.txt`, caiga donde caiga.
- Pendiente (no se tocó): cada flag lleva solo 4 caracteres aleatorios, así que el hash SHA-256
  del manifest se podría fuerza-brutear (~1,7 millones de combinaciones). No afecta si eres tú
  quien estudia, pero no lo uses como barrera si compartes el taller.

---

## 2. Método de trabajo (aplícalo a cada reto)

1. **Leer el brief y el `concepto`** (2 min). Decir en voz alta qué tipo de problema es.
2. **Triage sin ayuda: 15–20 min.** Los comandos de la sección 4 según categoría. Anota hipótesis.
3. **Escalera de ayuda** (no saltes peldaños): pista 1 → pista 2 → resto de la guía → (solo en
   Pwn-Bin/Reversing ciego) el prompt 🤖 para un LLM externo. Anota cuántas usaste.
4. **Validar la flag** en el panel.
5. **Writeup de 5 líneas** en `writeups/` (plantilla incluida). Si no puedes explicar *por qué*
   funcionó, el reto no cuenta como aprendido.
6. **Variante**: cuando termines el núcleo de una técnica, resuelve un reto opcional de la misma
   técnica sin pistas. Esa es tu prueba real de que la aprendiste.

**Ritmo sugerido (≈ 1–1,5 h/día, ajústalo a tu semana — no hay fecha límite)**
- La progresión completa, con estimación de horas por módulo, está en `CURSO.md`.
- Prioriza profundidad: es mejor terminar con 100 retos bien entendidos que con 260 hechos en
  automático.

---

## 3. El curso progresivo

Toda la progresión por módulos (M0–M9), con prerrequisitos, exámenes de salida y el mapa completo
de tus 260 retos por técnica, vive en [`CURSO.md`](CURSO.md). Es 100% local: no depende de ninguna
plataforma externa ni de ningún evento en vivo — cada módulo trae su propio "concepto" explicado
en el documento y su práctica contra el material de este repo.

---

## 4. Hoja de triage por categoría (primeros 5 minutos)

| Categoría | Primeros comandos |
|---|---|
| **Cualquier archivo** | `file X` · `strings -n 8 X \| head` · `xxd X \| head` · `exiftool X` · `binwalk X` |
| **Crypto** | ¿Texto alfanumérico con `=`? → base. ¿Solo letras? → César/Vigenère. ¿Números grandes `n,e,c`? → RSA: factorización (Fermat/`sympy`) |
| **Stego (imagen)** | `exiftool` · `zsteg -a img.png` · `steghide info img.jpg` · `binwalk -e` |
| **Reversing (con fuente)** | `cat check.c`, identifica la transformación y su inversa |
| **Reversing (sin fuente / ciego)** | `file` · `strings` · Ghidra (decompilar `main`) · `objdump -d -M intel` |
| **Pwn-Bin** | `checksec ./chal` · `objdump -d -M intel` · `nm` · `gdb`/`pwndbg` + patrón cíclico (`pwn cyclic`) |
| **Pwn (privesc)** | `find / -perm -4000 2>/dev/null` · `sudo -l` · revisa `/etc/crontab` y capabilities (`getcap -r / 2>/dev/null`) |
| **Web** | Ver código fuente y `robots.txt` · `gobuster`/`ffuf` · probar `'`, `"`, `{{7*7}}`, `;id` |
| **Máquinas** | `nmap -sCV -p- IP` → servicio por servicio → foothold → `sudo -l`, SUID, cron, capabilities |

---

## 5. MCP y herramientas que te conviene sumar

**Principio:** un MCP solo vale si **te enseña**, no si resuelve por ti. Úsalos en modo mentor:
Claude propone la hipótesis o explica la salida, y **tú** ejecutas y decides. Esto está fijado en
`CLAUDE.md`.

| Prioridad | MCP | Para qué | Cuándo |
|---|---|---|---|
| 1 | **GhidraMCP** (LaurieWired) | Claude lee el decompilado de Ghidra, lista funciones/imports y ayuda a renombrar | Módulo M6 (reversing), sobre todo para la Reversing ciego |
| 2 | **mcp-security-hub** (FuzzingLabs) | Colección de servidores en Docker: `nmap`, `ffuf`, `sqlmap`, `nikto`, `hashcat`, `binwalk`, `radare2`, `ghidra`, wrapper de Burp | Desde M3 en adelante, si quieres un copiloto de herramientas |
| 3 | **MCP Kali Server** | Puente para que Claude ejecute comandos en tu Kali | Opcional, siempre con confirmación manual de cada comando |

**Recomendación concreta (ejecución, no exploración):**
1. **Módulos M0–M5: no instales ninguno.** Los retos se resuelven con terminal + tu propio
   razonamiento; un MCP que ejecute herramientas por ti te quita el aprendizaje.
2. **Al llegar a M6 (reversing): instala GhidraMCP.** Es donde más ayuda — leer decompilado es
   lento y Claude explica bien el flujo mientras tú decides qué mirar.
3. **Desde M7 si lo quieres:** `mcp-security-hub` o Kali MCP, siempre contra este lab (local o tu
   propia EC2), con las confirmaciones de comandos activadas.

**Herramientas no-MCP que debes dominar** (están en Kali): `pwntools`, `pwndbg`, `Ghidra`, `gdb`,
`objdump`, `nm`, `socat`/`nc`.

---

## 6. Ética y límites
- Practica **solo** contra este lab: tu Kali local o tu propia EC2.
- El acceso no autorizado a sistemas de terceros es delito. En Chile aplica la Ley 21.459 sobre
  delitos informáticos (verifica el texto vigente en bcn.cl).
- Mantén el lab en `127.0.0.1` salvo que necesites atacarlo desde otra máquina. Si lo subes a EC2,
  restringe el *security group* a tu IP — el panel (`lab/control.py`) en particular no debería
  quedar expuesto a Internet abierto porque puede ejecutar Docker en el host (ver
  [`lab/README.md`](lab/README.md) para manejarlo por túnel SSH).

---

## 7. Checklist para dejar todo listo (hazlo una vez)
- [ ] Docker + plugin `compose` funcionando (`docker compose version`).
- [ ] `python3 lab/control.py` abre el panel en `http://127.0.0.1:8000/`.
- [ ] Kali con: `pwntools`, `pwndbg` o `gef`, `ghidra`, `socat`.
- [ ] Carpeta `writeups/` abierta y primer writeup del día 1 hecho.
- [ ] (Opcional, si vas a usar EC2) instancia creada, *security group* restringido a tu IP, Docker
  instalado en ella — ver [`lab/README.md`](lab/README.md).
