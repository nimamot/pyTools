#!/usr/bin/env python3

import subprocess

interface = "wlan0"
    # input("what interface would you like to change the macAddress for(eth0/wlan0)?")
new_macAddress = "00:11:22:33:44:77"
    # input("What's the new macAddress(aa:bb:cc:dd:ff:gg)?")
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_macAddress, shell=True)
subprocess.call("ifconfig " + interface  + " up", shell=True)

