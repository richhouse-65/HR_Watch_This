
# Wireshark

Wireshark is where I go when I need to understand what is actually happening on the wire. Alerts and logs tell you something is wrong — Wireshark shows you exactly what. I use it to capture traffic on my own network, analyze protocol behavior, and build a clear picture of what normal traffic looks like so anomalies stand out immediately.

## Protocols I work with

- **ARP** — device discovery at Layer 2; I use it to map MAC addresses to IPs and spot anything unexpected on a subnet

- **DNS** — I watch DNS traffic to verify resolution is working correctly and catch unusual query patterns

- **HTTP/HTTPS** — useful for understanding application behavior and confirming traffic is reaching its destination

- **ICMP** — my first check for connectivity and latency issues; ping and traceroute both live here

- **TCP** — I watch handshakes and connection states to identify dropped connections, retransmissions, and port issues

## How I use it

```bash

# Capture on a specific interface

wireshark -i wlan0

# Headless capture, save for later analysis

dumpcap -i wlan0 -w capture.pcap

# Open a saved capture

wireshark capture.pcap

```

## Filters I use regularly. Isolate a specific host

ip.addr == 192.168.1.1

DNS only

dns

HTTP only

http

Filter by port

tcp.port == 443

ARP traffic

arp

Show retransmissions — useful for spotting connectivity issues

tcp.analysis.retransmission ## How it fits into my workflow

I use Wireshark in combination with tcpdump — capture remotely with tcpdump, pull the .pcap file, analyze in Wireshark. That workflow covers both headless servers and local network analysis. The goal is always the same: confirm whether traffic is flowing correctly and isolate exactly where it breaks when it is not.

