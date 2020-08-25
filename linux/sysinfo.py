#! /usr/bin/python3
import os
import subprocess

subprocess.call("ls", shell=True)

a = subprocess.call(["df", "-h"], stdout=subprocess.PIPE)

for dire, subdir, files in os.walk("/home/atal"):
    for file in files:
        if "py" not in file:
            print(file)


