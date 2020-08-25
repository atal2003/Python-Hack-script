#! /usr/bin/python3

import os
from subprocess import Popen, PIPE
import random

sorter = Popen(["sort", "-nr"], stdin=PIPE, stdout=PIPE)

#write 10 random integers to the sorter's input. 

for i in range(10):
    sorter.stdin.write(("%d\n" % random.randrange(100)).encode())

  
sorter.stdin.close()

for line in sorter.stdout:
    print(line.decode(), end='')
