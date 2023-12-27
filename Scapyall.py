#!/usr/bin/env python
from scapy.all import IP, TCP, sr, Ether

# Create IP and TCP layers
i = IP(dst='192.168.56.100')
t = TCP(dport=22)

# Create Ethernet layer with source MAC address
src_mac = '00:11:22:33:44:55'  # Replace with the actual source MAC address
eth = Ether(src=src_mac)

# Construct the packet
packet = eth / i / t

# Send the packet and receive answers with verbose set to False
answered, unanswered = sr(packet, verbose=False)

# Print summary of answered packets
answered.nsummary()
