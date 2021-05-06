#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_macAddress", help="New MAc Address")
    (options, arguments) =  parser.parse_args()
    if not(options.interface):
        parser.error("[-] Please Specify thr interface, use --hrlp for more info")

    elif not options.new_macAddress:
        parser.error("[-] Please Specify the new mac, use --hrlp for more info")

    return options

def change_mac(interface, new_macAddress):
    print("changing mac address for " + interface + "to" + new_macAddress)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_macAddress])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return (mac_address_search_result.group(0))

    else:
        print("[-] Could not read the mac address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current mac = " + str(current_mac))
change_mac(options.interface, options.new_macAddress)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_macAddress:
    print("mac address was changed to " + current_mac)
else:
    print("MAC address did not get changed")



