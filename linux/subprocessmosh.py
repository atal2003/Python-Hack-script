#! /usr/bin/python3

import subprocess


completed = subprocess.run(["pythons3", "firstwalk.py"], stdout=subprocess.PIPE)

print(completed.returncode)
print(completed.stdout)
print(compelted.stderr)
print(completed.args)
if completed.returncode != 0:
    print(completed.sterr)




