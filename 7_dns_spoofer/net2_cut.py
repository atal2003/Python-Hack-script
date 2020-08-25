#! /usr/bin/env python3

import netfilterqueue
import scapy.all as scapy


def process_pocket(atal):
    print(atal)
    atal.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_pocket)
queue.run()


























