#! /usr/bin/python3
from optparse import OptionParser

import subprocess


parser = OptionParser()
parser.add_option('-a', dest="commandtest", type="str")

(options, args) = parser.parse_args()

atal = options.commandtest

subprocess.Popen(["ls", "-l", atal])
