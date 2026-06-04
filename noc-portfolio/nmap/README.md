# Nmap

I started using Nmap when I first got into cybersecurity, and it stuck with me even after I shifted focus entirely to networking. It was one of the first tools that made networks feel tangible — you run a scan and suddenly you can see what's alive, what's listening, what's exposed.

I use it mostly for three things: figuring out what devices are on a network, checking which ports are open on a specific host, and verifying whether a service is actually running where it should be. In a NOC context that last one matters a lot — if a monitoring alert fires, Nmap is often the first thing I reach for to confirm whether a port is genuinely down or just misbehaving.

## How I use it

\`\`\`bash
# Quick sweep to see what's alive on a subnet
nmap -sn 192.168.1.0/24

# Check what ports are open on a host
nmap -p- 192.168.1.1

# Find out what services and versions are running
nmap -sV 192.168.1.1

# Full picture: OS, versions, scripts
nmap -A 192.168.1.1

# Save results for documentation
nmap -sV 192.168.1.0/24 -oN scan.txt
\`\`\`

## Where it fits in NOC work

When something breaks on a network, the first question is usually "is the host reachable and is the service up?" Nmap answers both fast. It also helps with baselining — knowing what *should* be open so you notice when something unexpected shows up.

I've also used it on WiFi networks and against web-facing hosts to understand their exposure, which gave me a practical sense of what attackers see before a NOC team does.
