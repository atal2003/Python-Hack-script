#! /usr/bin/python3

import os
import tarfile
import time


os.chdir("/home/atal/extract_here")

mintime = time.time() - (7200)


with tarfile.open("/home/atal/new.tar", "r") as t:
    for info in t:
        if info.mtime > mintime and info.isfile():
            print("extractig %s" % info.name)
            t.extract(info)
        



