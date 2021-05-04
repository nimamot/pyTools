#!/usr/bin/env python3

import subprocess
import optparse

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
options = get_arguments()
# change_mac(options.interface, options.new_macAddress)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

