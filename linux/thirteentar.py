#! /usr/bin/python3

import tarfile
import os
import sys

def add_to_archive(f, t):
    try:
        t.add(f)
    except PermissionError as e:
        print("sorry atal %s " %e, file=sys.stderrr)

if len(sys.argv) < 2:
    list = ["."]
else:
    list = sys.argv[1:]

with tarfile.open("/home/atal/new.tar", "w") as t:
    for file in list:
        if os.path.isdir(file):
            for root, dirs, files in os.walk(file):
                for name in files:
                    add_to_archive(root + "/" + name, t)
        else:
            add_to_archive(file, t)

