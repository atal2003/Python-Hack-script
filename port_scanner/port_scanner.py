#! /local/bin/env python


import socket
#from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host  = raw_input("please enter an ip address")


def scanner_post(port):
    if sock.connect_ex((host, port)):
        print(" Port %d is  closed" % (port))
    else:
        print(" Port %d is  open" % (port))


for port in range(1,100):
    scanner_post(port)