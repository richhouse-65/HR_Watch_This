# tcpdump

When there is no GUI available — which is most of the time on production servers — tcpdump is how you capture and inspect traffic. It does the same job as Wireshark but entirely from the command line, which makes it essential for remote NOC work over SSH.

## How I use it

```bash
# See available interfaces
tcpdump -D

# Capture traffic on a specific interface
tcpdump -i eth0

# Capture and save to file for later analysis in Wireshark
tcpdump -i eth0 -w capture.pcap

# Read a saved capture
tcpdump -r capture.pcap

# Limit capture to 100 packets
tcpdump -i eth0 -c 100
```

## Filters

```bash
# Filter by host
tcpdump -i eth0 host 192.168.1.1

# Filter by port
tcpdump -i eth0 port 80

# Capture only DNS traffic
tcpdump -i eth0 port 53

# Capture ICMP (ping)
tcpdump -i eth0 icmp

# Combine filters
tcpdump -i eth0 host 192.168.1.1 and port 443
```

## Where it fits in NOC work

Most of the infrastructure a NOC monitors runs headless — no desktop, no Wireshark. tcpdump lets you capture traffic directly on a remote server via SSH, save it as a .pcap file, and pull it back to your machine for deeper analysis in Wireshark. That handoff between tcpdump and Wireshark is a standard part of diagnosing network issues in production environments.
