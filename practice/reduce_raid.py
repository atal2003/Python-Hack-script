#! /local/bin/env python


import os
import subprocess
import time
from datetime import datetime


df = subprocess.call(["df", "-h"], stdout=subprocess.PIPE)

print(df.stdout())
# for i in df.stdout:

	# y = i.split()
	# if y == "RAID" and y >= 80:
	# 	n = os.chdir("/root/PyacharmProject")
	# 	for e in n:
	#             print(e)
