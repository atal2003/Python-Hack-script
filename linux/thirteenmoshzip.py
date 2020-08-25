#! /usr/bin/python3

from pathlib import Path
from zipfile import ZipFile


with ZipFile("new3.zip", "w") as zip:
    for path in Path("/home/atal").rglob("*.*"):
        zip.write(path)




