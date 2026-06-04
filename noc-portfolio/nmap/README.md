# Nmap

One of the first tools I picked up and still one I reach for constantly. I use it to map what is on a network, confirm what services are running, and verify that hosts are behaving as expected. In a NOC context that means less "let me explore" and more "something fired an alert, let me confirm what is actually up and listening."

## How I use it

```bash
# Sweep a subnet to see what hosts are alive
nmap -sn 192.168.1.0/24

# Full port scan on a specific host
nmap -p- 192.168.1.1

# Service and version detection
nmap -sV 192.168.1.1

# OS detection, versions, scripts, traceroute
nmap -A 192.168.1.1

# Save output for documentation or comparison
nmap -sV 192.168.1.0/24 -oN scan.txt

# Fast scan with timing optimization
nmap -T4 -sV 192.168.1.0/24
```

## How it fits into my workflow

When an alert comes in, the first thing I verify is whether the host is reachable and whether the expected ports are open. Nmap answers both in seconds. I also use it for baselining — running scheduled scans and comparing results to catch unauthorized services or unexpected changes in the network topology.

I have used it across WiFi networks, local subnets, and web-facing hosts, which gave me a solid practical sense of what normal looks like and what stands out.
