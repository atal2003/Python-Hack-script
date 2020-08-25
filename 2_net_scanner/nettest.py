#! /usr/bin/env python

import scapy.all as scapy


def scan(ip):
    a = scapy.ARP(pdst=ip)
    b = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    a_b = b/a
    z = scapy.srp(a_b, timeout=1, verbose=False)[0]
    #print(z.summary())

    print("IP\t\t\t\t\t\t\tMAC")
    client_list = []
    for element in z:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}

        client_list.append(client_dict)



    for client in client_list:
        print(client["IP"] + "\t\t\t\t\t" + client["MAC"])
        #print(client)
       # print(client.values())


scan("192.168.81.2/24")
