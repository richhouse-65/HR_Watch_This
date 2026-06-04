# Netcat

Netcat is the simplest way to test whether a connection between two points actually works. Before blaming an application or a firewall rule, you use Netcat to verify the basic question: can this machine reach that port? If Netcat can connect and the application cannot, the problem is the application. If Netcat cannot connect either, the problem is the network.

## How I use it

```bash
# Test if a port is open on a host
nc -zv 192.168.1.1 80

# Test a range of ports
nc -zv 192.168.1.1 20-100

# Connect to a specific port (useful for banner grabbing)
nc 192.168.1.1 22

# Listen on a port (useful for testing connectivity from another machine)
nc -lvp 4444

# Send a file
nc -lvp 4444 > received.txt        # receiver
nc 192.168.1.1 4444 < file.txt     # sender
```

## Where it fits in NOC work

When a service alert fires, the first question is whether the issue is the application or the network path. Netcat isolates that immediately. It is also useful for quick banner grabs — connecting to a port and reading what the service returns — which helps confirm what is actually running on a host versus what should be running.
