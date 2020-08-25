#! /usr/bin/python3

from subprocess import Popen
import os
import time
import datetime


def file_measure(filename, directory):
    b = Popen(["wc", "-l", filename])
    print(b)
    c = os.stat(filename)
    z =  c.st_ctime
    m = time.ctime(z)
    print(f"({filename}, 'was created on', {m})")


file_measure("firstwalk.py", "hello")



print("YOU DID IT ATAL")
