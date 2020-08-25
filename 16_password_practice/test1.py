#! /usr/bin/env python

import scapy.all as scapy


def atal(ip):
    a = scapy.ARP(ip)
    scapy.ls(scapy.ARP)


atal("192.168.84.2")