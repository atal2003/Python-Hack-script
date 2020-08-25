#! /usr/bin/python3

from subprocess import Popen, PIPE
from datetime import datetime
import os
import sys
root_dir = "/"
df = Popen(["df", "-h"], stdout = PIPE)

for i in df.stdout:
    split_line = i.decode().split()
    if split_line[5] == root_dir:
        if int(split_line[4][:-1]) > 55:
             print("you need to reduce the size of the directory")


file_time = os.stat(root_dir)
file_created = file_time.st_ctime
now = datetime.now()
print("%s created %d ago" % (root_dir, file_created))
