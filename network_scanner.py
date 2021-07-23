import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # Ether() creates an Ether object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\t\tMAC Address")

    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("-------------------------------------------------")





scan("192.168.0.251/24")
