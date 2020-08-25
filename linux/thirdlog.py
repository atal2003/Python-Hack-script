#! /usr/bin/python3

import os
import subprocess
import time
from timeit import timeit


subprocess.call(["tail", "-n10", "/var/log/dpkg.log"])

print("done")
