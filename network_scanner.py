import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # Ether() creates an Ether object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered_list.summary())


scan("10.11.12.1/24")
