#! /usr/bin/python3

from subprocess import Popen, PIPE


from optparse import OptionParser
atal = OptionParser()
atal.add_option("-i", "--interface", dest="interface", help="interface name")
atal.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

(values, keys) = atal.parse_args()

interface = values.interface
new_mac = values.new_mac

print("changing the MAC address of interface " + interface + "to" + new_mac)


Popen(["ifconfig", interface, "down"])

Popen(["ifconfig", interface, "hw", "ether", new_mac])

Popen(["ifconfig", interface, "up"])
