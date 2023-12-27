from scapy.all import rdpcap

# Replace 'dns.cap' with the actual path to your pcap file
file = rdpcap('dns.cap')

# Now you can work with the 'file' variable, which contains the captured packets
