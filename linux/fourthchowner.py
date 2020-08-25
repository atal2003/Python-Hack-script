#! /usr/bin/python3

import os
import subprocess



uidset = set()


for i in open("/etc/passwd"):
    splitline = i.split(":")
    uidset.add(int(splitline[2]))


testdir = "/home/atal"
for folder, dirs, files in os.walk(testdir):
    for file in files:  
        path = folder + "/" + file
        attribute = os.stat(path)
        if attribute.st_uid not in uidset:
            print(path + (" ") + "has no owner")
        if os.path.islink(path):
            print( path + " is softlink ... skipping")
            continue

print("THIS WAS A VERY SEUCCEFUL SCRIPT, GOOD JOB ATAL")
