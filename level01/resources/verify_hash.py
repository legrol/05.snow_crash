#!/usr/bin/env python3

import crypt

TARGET = "42hDRfypTqqnw"
PASSWORD = "abcdefg"

print(crypt.crypt(PASSWORD, "42") == TARGET)
