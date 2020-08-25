#! /usr/bin/python3

# do't runt it the it will be hard to stop it. 

from time import sleep

from signal import *


def isprime(n):
    sleep(1)
    x = 2
    while (x * x) <=n:
        if not n %x: 
            return False
        x += 1
    return True

signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)
siganl(SIGTERM, SIG_IGN)

n = 1 
primes_list = []

while True:
    if isprime(n):
        print(" %d is prime" % n)
        primes_list.append(n)
    n += 1



