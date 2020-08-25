#! /usr/bin/python3

import subprocess
import os
path = "/"

def enumeratepaths(path=path):
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)
            return path_collection

enumeratepaths(path=path)



def enumeratedir(path=path):

    dir_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            dir_collection.append(dir)
            return dir_collection

#subprocess.call(["mkdir", "newtest"])


