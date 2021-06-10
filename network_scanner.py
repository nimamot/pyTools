import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("10.11.12.1")
