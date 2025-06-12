# Define known suspicious IP addresses

threat_ips = ["203.0.113.5", "198.51.100.7"]

def is_malicious(ip_address):
	# Check if the IP address is in the list of known malicious IPs
	return ip_address in threat_ips