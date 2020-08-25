#! /usr/bin/env python

import scapy.all as scapy


def scan(ip):
    a = scapy.ARP(pdst=ip)
    b = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    a_b = b/a
    answered_list = scapy.srp(a_b, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        print(element)
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        print(client_dict)
        client_list.append(client_dict)
    return client_list


def print_result(result_list):
    print("IP\t\t\t\t\tMAC Address\n....................................\n")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


scan_list = scan("192.168.81.0/24")
print_result(scan_list)




