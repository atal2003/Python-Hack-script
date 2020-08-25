#! /usr/bin/python3

import sys


if (len(sys.argv)) == 1:
    print("USAGE python3 sysargv.py <password> ")
else:
    password = sys.argv[1]
    print("you loged in sucessfully", password)
