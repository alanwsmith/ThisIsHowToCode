#!/usr/bin/env python3

import base64


with open('chime_v3.mp3', 'rb') as _file:
    #print(_file.read().decode("utf-8"))
    encoded = base64.b64encode(_file.read())

with open('base64_audio.txt', 'w') as _file:
    _file.write(encoded.decode("utf-8"))


# print(encoded.decode("utf-8"))

