#! /usr/bin/python3

from pathlib import Path
from zipfile import ZipFile
import subprocess
import os
import sys
import glob


for dirs, subdirs, files in os.walk("/mnt/c/Users/ashan/Download"):
    for file in files:
        du = subprocess.call(["du", "-h", file])
        print(du.stdou)
        #if du.stdout > 900:
        #    with ZipFile.open("new4.zip", "w") as t:
        #        t.write(file)
        #else:
        #     os.system("ls")










