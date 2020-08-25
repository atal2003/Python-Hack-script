#! /usr/bin/python3

from pathlib import Path
from zipfile import ZipFile


with ZipFile("new3.zip") as zip:
    print(zip.namelist())
    




