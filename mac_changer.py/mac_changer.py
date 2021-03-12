#!/usr/bin/env python3

import subprocess

interface = input("what interface would you like to change the macAddress for(eth0/wlan0)?")
new_macAddress = input("What's the new macAddress(aa:bb:cc:dd:ff:gg)?")
subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether 00:11:22:33:44:66", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)

