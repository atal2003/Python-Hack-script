#! /usr/bin/python3

import collections


hist = {}

for line in open("/mnt/c/Users/ashan/PycharmProjects/linux/test.log"):
    url = line.split()[0].split("-")[1]
    hist[url] = 1
    print(hist)





