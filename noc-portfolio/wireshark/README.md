# Wireshark

My main use for Wireshark has been capturing and observing traffic on my own WiFi network — seeing what devices are communicating, what protocols are running, and what a normal network actually looks like at the packet level. That baseline understanding of "normal" is exactly what matters in NOC work, where you need to recognize when something is off.

## Protocols I work with

- **ARP** — maps IP addresses to MAC addresses; useful for identifying devices on a subnet and spotting ARP spoofing attempts
- **DNS** — every domain lookup passes through here; anomalies in DNS traffic often indicate malware or misconfiguration
- **HTTP/HTTPS** — web traffic; in plain HTTP you can see requests and responses clearly, which is useful for understanding application behavior
- **ICMP** — ping and traceroute live here; helps diagnose connectivity and routing issues
- **TCP/UDP** — the foundation of most traffic; watching handshakes and connection states helps identify dropped connections or port issues

## How I use it

\`\`\`bash
# Capture on a specific interface
wireshark -i wlan0

# Capture without GUI, save to file
dumpcap -i wlan0 -w capture.pcap

# Open a saved capture
wireshark capture.pcap
\`\`\`

## Filters I use

\`\`\`
ip.addr == 192.168.1.1
dns
http
tcp.port == 80
arp
\`\`\`

## Where it fits in NOC work

Wireshark is how you go from "something is wrong" to "here is exactly what is wrong." Alerts tell you there is a problem — packet captures show you what the problem actually is at the network level. I use it to verify traffic is flowing correctly, identify unexpected hosts, and understand what applications are doing on the wire.
