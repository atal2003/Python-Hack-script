import subprocess
import optparse
import re


def change_mac(interface, mac_change):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_change])
    subprocess.call(["ifconfig", interface, "up"])


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="please put an valid interface")
    parser.add_option("-m", "--mac_address", dest="mac_change", help="please put an valid interface")
    (option, argument) = parser.parse_args()
    if not option.interface:
        parser.error("ATAL \n\n  please provied something otthin provided go to -help")
    elif not option.mac_change:
        parser.error("notthin provided go to -help")
    return option


def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w\:\w\w\:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("couldn't read mac address")


option = get_argument()
current_mac = get_mac_address(option.interface)
print("CURRENT MAC ADDRESS:  " + current_mac)
change_mac(option.interface, option.mac_change)
current_mac = get_mac_address(option.interface)
if current_mac == option.mac_change:
    print("Mac address sucessfully changed")
else:
    print("Mac addrress didn't changed")


