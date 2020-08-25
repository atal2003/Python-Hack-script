#! /usr/bin/python3

import os
import subprocess
import hashlib


file = input("please enter a file name:  ")
if os.path.exists(file):                                                                                                     hasher = hashlib.md5()
with open(file, "rb") as f:
    buf = f.read()
    hasher.update(buf)
    hexg = hasher.hexdigest()
    print(hexg)
