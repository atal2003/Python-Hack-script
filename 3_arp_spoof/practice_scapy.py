#! /usr/bin/env python3

import scapy.all as scapy
import time
import sys

packet = scapy.ARP(op=2, pdst="192.168.81.142", hwdst="00-0c-29-4F-7A-8E", psrc="192.168.81.2")
packet1 = scapy.ARP(op=2, pdst="192.168.81.2", hwdst="00:50:56:f2:9a:fc", psrc="192.168.81.150")
# sent_packets_count = 0
# print(packet)


scapy.ls(scapy.ARP())
print(packet.show())
print(packet.summary())