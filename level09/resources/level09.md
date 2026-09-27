# Level09 - Snow Crash v2

## Tipo de ejercicio

Análisis de un binario `setuid` que valida un token mediante una política
interna y expone una cadena válida en sus datos legibles.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level10`.

La versión clásica utiliza un token codificado y un programa que transforma
cada carácter según su posición. Esta OVA v2 utiliza el validador `da5id`, que
comprueba una cadena de 12 caracteres antes de leer el flag de `flag09`.

## 1. Identificar el componente del nivel

Desde la sesión SSH de `level09`:

```bash
whoami
hostname
pwd
ls -la
cat README
```

El README contiene la pista:

```text
Da5id saw something he shouldn't have.
```

El ejecutable del nivel se localiza con:

```bash
find /opt/snowcrash/level09 -maxdepth 2 -ls 2>/dev/null
```

Resultado relevante:

```text
/opt/snowcrash/level09/da5id
```

## 2. Analizar permisos y cadenas

```bash
ls -l /opt/snowcrash/level09/da5id
file /opt/snowcrash/level09/da5id
strings -a /opt/snowcrash/level09/da5id
```

El binario es `setuid` y pertenece a `flag09`:

```text
-r-sr-x--- 1 flag09 da5id ... /opt/snowcrash/level09/da5id
```

Entre las cadenas visibles aparecen los mensajes del validador:

```text
Usage: %s <token>
Rate limit exceeded.
Token format error.
checking byte %d...
accepted fp=%08x
rejected at byte %u fp=%08x
Invalid token.
/home/flag09/.flag
TOKEN ACCEPTED.
Flag: %s
Iheartpwnage
```

La cadena `Iheartpwnage` destaca como posible token válido: aparece junto a
los mensajes del programa, antes de la información de compilación, y tiene 12
caracteres.

## 3. Validar el token

Se ejecuta el binario con la cadena encontrada:

```bash
/opt/snowcrash/level09/da5id Iheartpwnage
```

El programa aceptó los 12 bytes y leyó el flag con los privilegios de
`flag09`:

```text
checking byte 0...
checking byte 1...
checking byte 2...
checking byte 3...
checking byte 4...
checking byte 5...
checking byte 6...
checking byte 7...
checking byte 8...
checking byte 9...
checking byte 10...
checking byte 11...
TOKEN ACCEPTED.
Flag: s19q3m3u4toaequegh8ahpicel
```

Las pruebas de control confirman la validación:

```bash
/opt/snowcrash/level09/da5id
/opt/snowcrash/level09/da5id test
/opt/snowcrash/level09/da5id IheartpwnageIheartpwnage
```

El primer comando muestra el uso, el segundo rechaza el formato y el tercero
rechaza la longitud o el contenido del token.

## 4. Conectarse a level10

Desde el equipo anfitrión:

```bash
exit
ssh level10@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
s19q3m3u4toaequegh8ahpicel
```

## Conclusión

La OVA v2 no utiliza el token codificado del ejercicio clásico. El binario
`da5id` funciona como un validador `setuid`, contiene la cadena válida
`Iheartpwnage` y, al aceptarla, lee `/home/flag09/.flag` como `flag09`.

No fue necesario modificar archivos de la OVA ni crear scripts auxiliares.
