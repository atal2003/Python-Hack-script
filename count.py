#! /usr/bin/env python

from pathlib import Path

d = Path("/root/Desktop1/")

files = d.walkfiles("*.py")

for file in files:
    file.remove()
    print("Removed{} file".format(file))
