#! /usr/bin/python3
import subprocess 
import optparse

parser = optparse.OptionParser()
parser.add_option("-l", dest="hello")
#parser.add_option('--air', action='store_const', const='air', dest='element')

(options, args) = parser.parse_args()

hi = options.hello

subprocess.call(["mkdir", hi]) 


