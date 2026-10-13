# 🎓 Curso CTF · 100% local, de cero a tu primer CTF real

**Para:** Estudiante · **Material:** únicamente lo que vive en esta carpeta (`retos/`, `lab/`) ·
**Dónde se corre:** tu Kali local, o tu propia EC2 (ver [`lab/README.md`](lab/README.md)) ·
**Idioma de trabajo:** español

Este curso ordena **tus 260 retos locales** (no por día, sino por técnica) en 10 módulos con
prerrequisito, concepto, práctica y **examen de salida**: no pasas al siguiente módulo sin
aprobarlo. No depende de ninguna plataforma externa, ninguna cuenta, ningún evento en vivo:
**todo el material para aprender la técnica y todo el material para practicarla vive en este
repo.** Si en algún momento quieres medirte contra algo externo (un CTF real, otra plataforma),
es una decisión tuya, nunca un requisito para avanzar aquí.

> Cómo trabajar con Claude: abre esta carpeta y pídele "retomemos el curso". Seguirá
> [`CLAUDE.md`](CLAUDE.md): te guía con preguntas y pistas, no te da las flags directamente.
> Tu avance se marca en [`CURSO_PROGRESO.md`](CURSO_PROGRESO.md) y en el panel (`panel.html`).

---

## 1. Cómo está armado

- **Días 1–30 (240 retos):** Crypto, Encoding, Stego, Forensics, OSINT, Reversing (con fuente),
  Web (máquina) y Pwn/Privesc (máquina). Progresión N1→N4 dentro de cada técnica.
- **Días 31–42 (12 retos, `Pwn-Bin`):** explotación de binarios **real** — overflow de variable
  local → ret2win (secuestro de flujo) → format string leak → format string write (`%n`). Son
  máquinas Docker nuevas: te descargas el binario exacto para analizarlo offline y levantas el
  contenedor para explotarlo contra un socket TCP real.
- **Días 43–50 (8 retos, Reversing ciego):** binarios compilados **sin el `.c`**, como en un CTF
  real — el programa solo dice "correcto"/"incorrecto", nunca imprime la flag. Tienes que
  decompilar de verdad.

No haces los 260 uno a uno: cada módulo marca un subconjunto **núcleo** (el mínimo para aprender
la técnica completa) y deja el resto como **opcional**, para cuando quieras más repetición de la
misma técnica antes de seguir.

**Si te atascas en un reto de Pwn-Bin o Reversing ciego:** su última pista (🤖, en el panel) es un
prompt listo para copiar y pegar en cualquier LLM, junto con tu propio `objdump`/`gdb`/Ghidra.
Ese prompt le pide al LLM que te haga preguntas y te dé pistas una a la vez — nunca el exploit
completo.

---

## 2. Método de trabajo (aplícalo a cada reto)

1. **Lee el brief y el `concepto`** del reto en el panel (2 min). Di en voz alta qué tipo de
   problema es antes de tocar una herramienta.
2. **Intenta sin ayuda, 15–20 min.** Usa la hoja de triage (§6 de `PLAN_DE_ESTUDIO.md`) según la
   categoría. Anota tu hipótesis.
3. **Escalera de ayuda** (no saltes peldaños): pista 1 → pista 2 → pasos de la guía → (solo en
   Pwn-Bin/Reversing ciego) el prompt 🤖 para un LLM externo.
4. **Valida la flag** en el panel.
5. **Writeup de 5 líneas** en `writeups/` (plantilla incluida). Si no puedes explicar *por qué*
   funcionó, el reto no cuenta como aprendido.
6. **Variante:** cuando termines el núcleo de una técnica, resuelve además **uno de los retos
   opcionales de la misma técnica sin abrir ninguna pista**. Esa es tu prueba real de que
   aprendiste la técnica y no memorizaste el reto.

**Ritmo sugerido (no hay fecha límite — ajústalo a tu semana):** cada módulo trae una estimación
de horas; a ~1–1,5 h/día, los módulos pequeños (M0, M1, M9) te toman 3-5 días y los grandes (M3,
M5, M7) 2-3 semanas. Prioriza profundidad: es mejor llegar al final con 100 retos bien entendidos
que con 260 hechos en automático.

**Reglas**
1. No avanzas de módulo sin aprobar su examen de salida (te lo toma Claude).
2. Cada reto núcleo resuelto = writeup de 5 líneas en `writeups/`.
3. Cada módulo termina con **una variante sin pistas** (regla 6 de arriba) como parte del examen.
4. Solo objetivos de este lab: tu Kali local o tu propia EC2. Nunca sistemas de terceros.

---

## M0 · Terminal, entorno y método

**Meta:** moverte en Linux sin pensar y tener el lab corriendo.
**Prerrequisito:** ninguno. **Estimado:** 3-5 h.

**Concepto (autocontenido, sin lecturas externas):** un CTF se resuelve en la terminal. Necesitas
soltura con: navegación (`cd`, `ls`, rutas relativas/absolutas), permisos (`chmod`, `ls -l`, el
significado de `rwx` y del bit SUID), procesos y pipes (`|`, `ps`, `grep`), y variables de entorno
(`$PATH`, `export`). Si algo de esto no te es automático, practícalo en tu propia Kali antes de
seguir — no hace falta ninguna plataforma externa para esto, basta con usar la terminal a diario.

**Práctica**
- Levanta el taller: `python3 lab/control.py` → abre `http://127.0.0.1:8000/`.
- Levanta y detén `d01-web` (botón "Levantar máquina" / "Detener") desde el panel.
- Instala en tu Kali: `pwntools`, `pwndbg` o `gef`, `ghidra`, `socat`.

**Entregable:** una captura del lab corriendo (`d01-web` levantada y respondiendo a `curl`).
**Examen de salida:** (1) Explicas con tus palabras qué hace `find / -perm -4000 2>/dev/null` y
qué es un pipe. (2) Levantas y detienes una máquina del lab sin ayuda. (3) Explicas qué es
`$PATH` y por qué importa para un *PATH hijack*.

---

## M1 · Codificación y criptografía clásica

**Meta:** reconocer un formato por su alfabeto, romper cifrados clásicos y automatizar con Python.
**Prerrequisito:** M0 aprobado. **Estimado:** 6-8 h.

**Concepto:** antes de usar una herramienta, mira el **alfabeto** del dato (¿solo letras? ¿termina
en `=`? ¿son todo dígitos hex?) — eso ya te dice la familia (sustitución, base-N, hex/binario). La
sección `concepto` de cada reto del panel explica la técnica concreta de ese día; léela antes de
intentar.

**Práctica local — núcleo**

| Enfoque | Técnica | **Núcleo** | Opcional (repetición) |
|---|---|---|---|
| Encoding | Capas de codificación (1→4) | D01, D08, D16, D24 | D02-D07, D09-D15, D17-D23, D25-D30 |
| Crypto | César / Vigenère | D01, D02, D08, D09 | D03-D07, D10-D15 |

**Entregable:** un script `decode.py` que desapile capas Base64/Base32/hex/ROT13 automáticamente.
**Examen de salida:** (1) César y Vigenère sin ayuda (Vigenère con análisis de frecuencias). (2) Un
reto **opcional** (no núcleo) de 4 capas, resuelto sin pistas, en terminal y con tu script.

---

## M2 · Forensics, Stego y OSINT

**Meta:** analizar un archivo desconocido en 5 minutos y saber qué buscar.
**Prerrequisito:** M1 aprobado. **Estimado:** 8-10 h.

**Concepto:** todo archivo miente en su extensión; el *magic number* (`file`) no. Después de eso,
la secuencia es siempre: `strings` (texto legible) → `xxd`/hexdump (cabeceras, firmas
embebidas) → `exiftool` (metadatos) → `binwalk`/`foremost` (archivos dentro del archivo). Para
esteganografía en imágenes: LSB (`zsteg`), canal por canal, y datos tras el EOF del formato.

**Práctica local — núcleo** (primer y último nivel de cada técnica)

| Enfoque | Técnica | **Núcleo** | Opcional |
|---|---|---|---|
| Forensics | Las 5 técnicas (Base64 en log, hex plano, ZIP embebido, gzip, ruido) | D01-D05, D26-D30 | D06-D25 |
| Stego | Las 5 técnicas (LSB RGB, metadatos, EOF, invisibles, canal único) | D01-D05, D26-D30 | D06-D25 |
| OSINT | Correlación (2→4 fuentes) | D01, D08, D16, D24 | el resto |

**Entregable:** tu **hoja de triage** personal (1 página): qué corres primero según el tipo de
archivo (puedes partir de la de `PLAN_DE_ESTUDIO.md` §6 y ajustarla con lo que aprendiste).
**Examen de salida:** (1) Dado un archivo sin extensión (uno opcional que no hayas tocado),
determinas su tipo y extraes lo oculto sin ayuda. (2) Un reto Stego o Forensics de nivel 4 de
los opcionales, sin pistas.

---

## M3 · Web I · inyecciones, autenticación y control de acceso

**Meta:** encontrar y explotar las vulnerabilidades web del lado servidor más comunes.
**Prerrequisito:** M2 aprobado. **Estimado:** 10-14 h.

**Concepto:** toda vulnerabilidad web de este bloque viene de **confiar en una entrada del
usuario** sin validarla: un parámetro que se concatena en una consulta SQL (SQLi), una ruta que
se concatena en una llamada al sistema de archivos (path traversal) o un parámetro que se pasa
tal cual a un comando de shell (command injection). El método es siempre: identificar el punto de
entrada (`gobuster`/`ffuf`, DevTools, `curl`), inyectar un carácter de prueba (`'`, `"`, `;`, `../`)
y observar el cambio de comportamiento (error, delay, contenido distinto).

**Práctica local — núcleo (máquinas Web)**

| Enfoque | Técnica | **Núcleo** | Opcional |
|---|---|---|---|
| Web | Command injection, cookie/auth, IDOR, LFI, SQLi (login), SQLi UNION | D01, D02, D03, D04, D06, D07 (+ D11-D17 para repetir) | D21-D27 |

**Entregable:** un script en Python con `requests` que automatice una SQLi booleana (extraer un
dato carácter a carácter) contra una de las máquinas del lab.
**Examen de salida:** (1) Dos máquinas Web **opcionales** (no núcleo) resueltas sin pistas. (2)
Explicas por qué una consulta parametrizada evita la SQLi y por qué validar la ruta evita el LFI.

---

## M4 · Reconocimiento y escalada de privilegios

**Meta:** el ciclo completo de una máquina: enumerar → acceso inicial → root.
**Prerrequisito:** M3 aprobado. **Estimado:** 6-8 h.

**Concepto:** la escalada de privilegios en Linux sigue siempre el mismo patrón: encuentra algo
que corre **como root o con más permiso que el tuyo** y que **tú puedas influenciar** (un binario
SUID, una entrada de `sudo -l`, un cron que escribe un script tuyo, una capability). GTFOBins
(conceptualmente: una lista de binarios comunes y cómo abusarlos bajo sudo/SUID) es la referencia
mental, no hace falta visitarla para entender el patrón — cada reto del panel te explica la
técnica concreta en su `concepto`.

**Práctica local — núcleo (máquinas Pwn = privesc)**

| Enfoque | Técnica | **Núcleo** | Opcional |
|---|---|---|---|
| Pwn | Las 10 técnicas de privesc (SUID, sudo find/awk/python, `/etc/passwd`, PATH hijack, cron, capabilities ×2, LD_PRELOAD) | D01-D10, D11-D20 | D21-D30 |

**Entregable:** una **checklist de privesc** propia (`sudo -l`, SUID, cron, capabilities, PATH,
archivos escribibles) con el comando de cada punto.
**Examen de salida:** (1) Una máquina Pwn **opcional** resuelta sin pistas. (2) Para 3 técnicas de
la tabla, explicas la causa raíz y cómo se corrige (el defensor, no solo el atacante).

---

## M5 · Criptografía real

**Meta:** atacar RSA y hashes mal usados con matemática y Python, no solo con herramientas.
**Prerrequisito:** M1 y M4 aprobados. **Estimado:** 8-10 h.

**Concepto:** XOR de clave repetida se rompe explotando que `A XOR A = 0` (si conoces o adivinas
parte del texto plano, recuperas la clave); RSA factorizable se rompe cuando el módulo `n` es
producto de primos pequeños o cercanos (Fermat); un hash sin sal se rompe por diccionario/fuerza
bruta (`hashcat`/`john`). El `concepto` de cada reto del panel detalla la variante exacta.

**Práctica local — núcleo**

| Enfoque | Técnica | **Núcleo** | Opcional |
|---|---|---|---|
| Crypto | XOR clave repetida, XOR 1 byte, RSA factorizable, hash MD5 | D16-D19, D24-D27 | D20-D23, D28-D30 |

**Entregable:** un script `rsa_attacks.py` con factorización por Fermat/`sympy` (impleméntalo tú,
no uses solo una librería que ya lo resuelva).
**Examen de salida:** (1) Rompes un RSA débil **opcional** con tu script. (2) Explicas por qué
reusar la clave de un XOR (o un *nonce*) es inseguro, con un ejemplo propio.

---

## M6 · Reversing de binarios (con y sin código fuente)

**Meta:** entender un ejecutable, con y sin tener su código fuente.
**Prerrequisito:** M4 aprobado y saber leer C básico. **Estimado:** 10-14 h.

**Concepto:** ingeniería inversa es reconstruir la lógica de un programa a partir de su
comportamiento y/o su código máquina. Con fuente (`.c`), practicas leer la transformación
directamente. Sin fuente (binario compilado), tienes que decompilar (Ghidra) o leer ensamblador
(`objdump -d`) y reconstruir la misma lógica mirando instrucciones, no texto.

**Práctica local — núcleo**

| Bloque | Técnica | **Núcleo** | Opcional |
|---|---|---|---|
| Reversing (con fuente, días 1-30) | Deshacer transformación N1→N4 | D01, D08, D16, D24 | el resto |
| **Reversing ciego (días 43-50, sin `.c`)** | XOR constante → XOR posicional → add+XOR → retroalimentación | **las 8 (43-50)** | — (son solo 8, haz todas) |

**Entregable:** para cada técnica de Reversing ciego, el script Python que invierte la
transformación (no lo que imprime el binario: el script que TÚ escribiste razonando la lógica).
**Examen de salida:** (1) Las 8 de Reversing ciego resueltas. (2) Dado un ELF nuevo (uno de los
opcionales de los días 1-30, pero resuélvelo **sin abrir el `.c`**, solo con Ghidra/objdump/gdb),
localizas `main`, la comparación con la flag y la transformación aplicada. (3) Explicas la
diferencia entre análisis estático (leer sin ejecutar) y dinámico (ejecutar y observar).

---

## M7 · Explotación de binarios (Pwn-Bin)

**Meta:** escribir un exploit de stack overflow y de format string con `pwntools`, contra un
servicio real (`nc IP puerto`).
**Prerrequisito:** M6 aprobado. **Estimado:** 14-18 h (es el bloque más denso, tómate tu tiempo).

**Concepto:** un stack overflow ocurre cuando un programa escribe más bytes de los que reservó
para una variable local y esos bytes extra invaden memoria vecina (otra variable, o la dirección
de retorno de la función). Una cadena de formato vulnerable (`printf(buf)` en vez de
`printf("%s", buf)`) deja que tú controles qué especificadores interpreta `printf`, lo que te deja
leer (`%p`) o escribir (`%n`) memoria arbitraria. El `concepto` y los `pasos` de cada reto del
panel traen el razonamiento completo, nivel por nivel.

**Práctica local — núcleo (las 12, sin PIE/canary/CET para enfocarte en la técnica base)**

| Técnica | Retos | Nivel |
|---|---|---|
| Overflow de variable local (pisar un flag de autorización vecino) | D31, D32, D33 | N1 |
| **ret2win**: medir el offset y secuestrar la dirección de retorno | D34, D35, D36 | N2 |
| Format string **leak**: filtrar un valor del stack con `%N$p` | D37, D38, D39 | N3 |
| Format string **write**: usar `%n` para activar una variable | D40, D41, D42 | N4 |

**Entregable:** para cada técnica, tu exploit en Python con `pwntools` (reutilizable: debe
funcionar igual contra `127.0.0.1` que contra la IP de una EC2 donde levantes el mismo lab).
**Examen de salida:** (1) Las 12 máquinas de Pwn-Bin resueltas de extremo a extremo (binario
descargado analizado offline + exploit contra el socket real). (2) Explicas, para el ret2win, por
qué el offset incluye el "saved RBP" además del buffer. (3) Explicas, para el format string write,
qué significa literalmente que `%n` "escribe cuántos caracteres se han impreso".

> Heap, ROP avanzado, ASLR/PIE con leak y canary bypass quedan fuera de este curso a propósito
> (ver §Nivel 2): primero domina la base sin esos obstáculos.

---

## M8 · Web II · cliente y servidor avanzado

**Meta:** SSRF, JWT, SSTI y XXE.
**Prerrequisito:** M3 aprobado. **Estimado:** 6-8 h.

**Concepto:** estas cuatro son variaciones del mismo patrón de M3 (confiar en una entrada) pero
contra superficies distintas: SSRF (el servidor hace una petición HTTP que tú controlas), JWT
`alg:none` (el servidor confía en un token sin validar su firma), SSTI (tu entrada se evalúa como
plantilla, no como texto), XXE (el parser XML resuelve entidades externas que tú defines).

**Práctica local — núcleo (máquinas Web N3-N4)**

| Enfoque | Técnica | **Núcleo** | Opcional |
|---|---|---|---|
| Web | SSRF, JWT alg:none, SSTI (Jinja2), XXE | D05, D08, D09, D10 | D15, D18, D19, D20, D25, D28, D29, D30 |

**Examen de salida:** (1) Dos máquinas **opcionales** de la tabla, sin pistas. (2) Explicas cómo
se previene cada una de las 4 (allowlist de destinos para SSRF, verificar la firma del JWT,
sandboxing/autoescape para SSTI, deshabilitar entidades externas para XXE).

---

## M9 · Capstone

**Meta:** demostrar que puedes resolver bajo presión de tiempo, con el repertorio completo.
**Prerrequisito:** M0-M8 aprobados. **Estimado:** 6-8 h.

1. **Simulacro de 4-6 h, con reloj:** elige 10-12 retos **opcionales** (no núcleo) que no hayas
   tocado, repartidos entre varios enfoques, y resuélvelos como si fuera un CTF real: 10 min
   leyéndolos todos, tope de ~30-40 min por reto, notas de lo intentado en cada uno aunque no lo
   resuelvas.
2. **Informe final:** por cada reto del simulacro, un writeup (lo resolvieras o no) con causa raíz
   y cómo te habrías defendido.
3. **Portafolio:** ≥ 20 writeups acumulados en `writeups/` a lo largo del curso.

> Si en este punto quieres probarte contra algo externo — un CTF Jeopardy real, otra plataforma —
> es el mejor momento para hacerlo: ya tienes el repertorio completo. Pero es una decisión tuya,
> no un requisito de este curso: con M0-M9 aprobados, **ya estás listo para enfrentar un CTF.**

---

## Examen final · "Listo para CTF"

Marca todo con honestidad (Claude lo revisa contigo):

- [ ] Analizo un archivo desconocido y decido en 5 min qué categoría es.
- [ ] Decodifico 4 capas de codificación y rompo César, Vigenère y XOR sin ayuda.
- [ ] Rompo un RSA débil con mi propio script.
- [ ] Hago SQLi (UNION y booleana), LFI, IDOR y command injection a mano.
- [ ] Explotación web avanzada: SSRF, SSTI, JWT y XXE en máquinas del lab.
- [ ] Hago escalada de privilegios en Linux con mi propia checklist.
- [ ] Leo un ELF en Ghidra/objdump y reconstruyo su lógica, **con o sin** el código fuente.
- [ ] Escribo un ret2win y un format string (leak y write) con `pwntools` contra un socket real.
- [ ] Tengo ≥ 20 writeups que explican causa raíz y defensa, no solo "cómo saqué la flag".

---

## Nivel 2 (después del curso, fuera del alcance de este repo)

Si quieres seguir profundizando por tu cuenta, el orden natural que sigue de aquí es: ROP y heap
exploitation, bypass de canary/ASLR con un leak, kernel exploitation, criptografía de curva
elíptica, Active Directory, y metodología de pentest más amplia. Nada de esto es necesario para
"estar listo para un CTF" — son especializaciones que se construyen encima de lo que ya aprendiste
aquí, cuando te topes con un reto real que las necesite.

---

## Mapa rápido: tus 260 retos por módulo

| Módulo | Bloque | Núcleo | Opcionales |
|---|---|---|---|
| M1 | Encoding, Crypto (César, Vigenère) | 8 | 37 |
| M2 | Forensics, Stego, OSINT | 14 | 76 |
| M3 | Web (cmd injection, cookie, IDOR, LFI, SQLi ×2) | 6 | 24 |
| M4 | Pwn/Privesc (las 10 técnicas) | 20 | 10 |
| M5 | Crypto (XOR ×2, RSA, MD5) | 8 | 7 |
| M6 | Reversing con fuente + Reversing ciego | 12 | 26 |
| M7 | **Pwn-Bin (las 12, núcleo = todas)** | 12 | 0 |
| M8 | Web (SSRF, JWT, SSTI, XXE) | 4 | 8 |
| **Total** | | **84** | **176** |

Un reto se identifica como `D<día> <enfoque>` (archivo o máquina) igual que siempre; los de
Pwn-Bin y Reversing ciego llevan además su `maquina_id`/carpeta (`pwnbin-NN`, `revbin-NN`). Los
hashes validan la flag igual que antes.
