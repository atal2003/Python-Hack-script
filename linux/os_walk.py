#! /usr/bin/python3

import os
import subprocess



mydir = "/root/PycharmProjects/"

for dir, subdir, files in os.walk(mydir):
    for file in files:
        if "py" in file:
            print(file)



