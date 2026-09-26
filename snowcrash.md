# SnowCrash

<img width="1536" height="1024" alt="snowcrash42" src="https://github.com/user-attachments/assets/b37a6ea2-af3a-4c33-80c3-55ff9507dd42" />

<br><br>

## Descripción

SnowCrash es un proyecto de tipo CTF (Capture The Flag) centrado en la seguridad informática. Se proporciona una OVA de Linux (x64, Ubuntu) y el objetivo es encontrar las distintas banderas.

El proyecto tiene 15 niveles, del `level00` al `level14`:

- Los niveles `level00` a `level09` son obligatorios.
- Los niveles `level10` a `level14` son bonificaciones.

El proyecto permite estudiar problemas de seguridad de diferentes tipos, como:

- Código mal escrito o sin protección.
- Comunicaciones de red sin protección.
- Trabajos automatizados mal gestionados en las máquinas.

## Encontrar y validar las banderas

En el sistema hay dos tipos principales de cuentas de usuario:

- `levelXX`: cuenta correspondiente al nivel actual. `XX` representa el número del nivel, por ejemplo `level00`, `level01` o `level11`.
- `flagXX`: cuenta asociada a cada nivel, por ejemplo `flag00`, `flag01` o `flag11`.

Normalmente hay que encontrar la contraseña de la cuenta `flagXX` correspondiente al nivel actual. Por ejemplo, en `level03` hay que encontrar la contraseña que permite iniciar sesión como `flag03`.

Después de acceder como `flagXX`, se ejecuta el programa `getflag`, que muestra la bandera del nivel. Esa bandera es también la contraseña del siguiente nivel. Por ejemplo, la bandera obtenida desde `flag03` permite iniciar sesión como `level04`.

El flujo habitual es el siguiente:

```bash
# Encontrar la contraseña de la cuenta flag03
level03@SnowCrash:~$ su flag03
Password:

flag03@SnowCrash:~$ getflag
Check flag. Here is your token: XXXXXXXXXXXXXXXXXXXXXXXXX

flag03@SnowCrash:~$ su level04
Password:  # La contraseña es la bandera obtenida en flag03
```

No siempre es necesario iniciar sesión como `flagXX` para obtener la bandera. En algunos niveles la bandera se encuentra directamente desde la cuenta `levelXX`, y en otros no es necesario ejecutar `getflag`.

El binario `getflag` se encuentra normalmente en:

```text
/bin/getflag
```

## Recursos

Los recursos del proyecto incluyen:

- El tema en inglés y en francés.
- La imagen OVA de Linux.
- El vídeo del proyecto disponible en Intra y en formato RAW, sin necesidad de iniciar sesión.

## Comenzar el proyecto

Para iniciar el proyecto, hay que abrir la OVA en una máquina virtual, como VMware o VirtualBox.

Si se utiliza VirtualBox, no es necesario configurar la red en modo puente, con el modo NAT por defecto es suficiente.

Tras haber importado la OVA, la abrimos para comporbar la IP de la misma. 

Nos pedirá un login y un password. En nuestro primer nivel level00 será:

```text
login: level00
password: level00
```

En nuestro caso, observamos que la IP está configurada:

```text
enp0s3: 10.0.2.15
```
<br><br>

<img width="864" height="620" alt="image0" src="https://github.com/user-attachments/assets/35958d45-bae7-4822-9f2a-810313ff377f" />

<br><br>

Ahora accedemos en la configuración de la OVA en la zona Red / Adaptador 1

<br><br>

<img width="1766" height="1326" alt="image1" src="https://github.com/user-attachments/assets/c34457e4-1019-4972-98e1-6a5e665d7dd3" />

<br><br>

hacemos click en Reenvío de puertos y dejamos esta configuración:

<br><br>

<img width="1596" height="1076" alt="image2" src="https://github.com/user-attachments/assets/67ec0fa3-3506-4bc2-a43d-83d523bd1d1f" />

<br><br>

Notar que hemos configurado en el Hot Anfitrión el puerto 2424, ya que el 4242 (recomendado) en 42 Málaga se haya ocupado por otros servicios.

Según el tema de 42, se debe acceder a la máquina mediante SSH usando el puerto `4242` (nosotros gestionaremos el 2424). 

Ahora nos conectaremos vía ssh desde una terminal con:

```bash
ssh level00@127.0.0.1 -p 2424

o

ssh level00@localhost -p 2424

```

<img width="1030" height="710" alt="image3" src="https://github.com/user-attachments/assets/7b918ef7-3999-4c6e-88c0-ad96945002fd" />






REVISAR LO SIGUIENTE



## Estructura del proyecto

El repositorio debe contener un directorio para cada nivel, con el formato `levelXX`. Por ejemplo, los cuatro primeros niveles serían:

```text
$> ls -al
drwxr-xr-x 2 root root 4096 Dec 3 XX:XX level00
drwxr-xr-x 2 root root 4096 Dec 3 XX:XX level01
drwxr-xr-x 2 root root 4096 Dec 3 XX:XX level02
drwxr-xr-x 2 root root 4096 Dec 3 XX:XX level03
```

Dentro de cada directorio debe existir un archivo llamado `flag` con la explicación del proceso utilizado para obtener la bandera.

También puede existir un directorio `resources` que contenga los archivos necesarios para demostrar o reproducir el proceso. Todo lo incluido en ese directorio debe explicarse durante la corrección.

Un ejemplo de estructura para `level00` es:

```text
$> ls -alR level00
level00:
total 16
drwxr-xr-x 3 root root 4096 Dec 3 15:22 .
drwxr-xr-x 6 root root 4096 Dec 3 15:20 ..
-rw-r--r-- 1 root root    5 Dec 3 15:22 flag
drwxr-xr-x 2 root root 4096 Dec 3 15:22 resources
```
