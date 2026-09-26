# Level01 - Snow Crash v2

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level02`.

Esta OVA es diferente de la version clasica del reto. No incluye `getflag`,
`john` ni `hashcat`, y la cuenta `flag01` esta configurada con
`/usr/sbin/nologin`.

## 1. Identificar el entorno

Desde la sesion SSH de `level01`:

```bash
whoami
hostname
pwd
grep '^flag01:' /etc/passwd
```

Resultado relevante:

```text
level01
snowcrash
/home/level01
flag01:x:2001:2001::/home/flag01:/usr/sbin/nologin
```

El campo `x` indica que la contrasena no esta en `/etc/passwd`. Ademas,
`flag01` no puede iniciar una sesion normal porque su shell es `nologin`.

## 2. Descartar la ruta clasica

El directorio personal contiene estos archivos:

```bash
ls -la
cat README
cat hash.txt
```

Contenido observado:

```text
Gargoyles never stop collecting.
42hDRfypTqqnw --show
```

`42hDRfypTqqnw` tiene el formato de un hash DES antiguo. La opcion
`--show` no forma parte del hash; es una opcion de John the Ripper.

La OVA no trae esas herramientas:

```bash
command -v john
command -v hashcat
```

Python si incluye el modulo `crypt`, por lo que se puede verificar el hash:

```bash
python3 -c 'import crypt; print(crypt.crypt("abcdefg", "42") == "42hDRfypTqqnw")'
```

El resultado es `True`, pero `abcdefg` no es la contrasena activa de
`flag01`. Esto se confirma al intentar:

```bash
su -s /bin/bash flag01
```

El resultado es `su: Authentication failure`. El hash pertenece a la pista
del reto clasico, no al mecanismo de autenticacion de esta OVA.

## 3. Localizar el componente propio de la OVA

Buscar archivos propiedad de `flag01` y binarios SUID muestra el programa
especifico del nivel:

```bash
find / -xdev -user flag01 -ls 2>/dev/null
find / -xdev -type f -perm -4000 -ls 2>/dev/null
find / -xdev -type f -readable 2>/dev/null | grep -E 'level01|flag01|snowcrash'
```

El archivo relevante es:

```text
/opt/snowcrash/level01/gargoyle
```

El `README` daba la pista `Gargoyles never stop collecting`, asi que se
inspecciono el servicio que lo ejecuta:

```bash
cat /etc/systemd/system/gargoyle.service
```

Su contenido relevante es:

```ini
[Service]
Type=forking
User=flag01
ExecStart=/opt/snowcrash/level01/gargoyle kooda7puivaav1idi4f57q8iq0
Restart=always
RestartSec=5
```

## 4. Obtener la credencial del siguiente nivel

El proceso confirma que el servicio sigue ejecutandose con ese argumento:

```bash
ps aux | grep '[g]argoyle'
```

Resultado:

```text
flag01 ... /opt/snowcrash/level01/gargoyle kooda7puivaav1idi4f57q8iq0
```

El valor encontrado es:

```text
kooda7puivaav1idi4f57q8iq0
```

No es la contrasena de `flag01`; intentar usarlo con `su flag01` falla porque
esa cuenta esta bloqueada o tiene otra contrasena. Es la credencial de acceso
al siguiente nivel.

## 5. Conectarse a level02

Desde el equipo anfitrion:

```bash
ssh level02@localhost -p 2424
```

Cuando SSH solicite la contrasena, introducir:

```text
kooda7puivaav1idi4f57q8iq0
```

La conexion correcta muestra:

```text
level02@snowcrash:~$
```

## Conclusion

La ruta clasica basada en `/etc/passwd`, DES y `getflag` no es valida para
esta imagen. La solucion de esta OVA v2 consiste en leer la configuracion del
servicio `gargoyle`, observar el argumento del proceso que se ejecuta como
`flag01` y reutilizar ese valor como credencial de `level02`.
