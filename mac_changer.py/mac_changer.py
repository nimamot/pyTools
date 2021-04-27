#!/usr/bin/env python3

import subprocess
import optparse


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_macAddress", help="New MAc Address")

(options, arguments) = parser.parse_args()


interface = options.interface
new_macAddress = options.new_macAddress


print("changing mac address for " + interface + "to" + new_macAddress)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_macAddress])
subprocess.call(["ifconfig", interface, "up"])
