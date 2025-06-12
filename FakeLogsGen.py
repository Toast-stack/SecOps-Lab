from ipaddress import ip_address
import json, random
from datetime import datetime

def generate_fake_log():
    # Define possible values for each field
    actions = ["login", "access", "modify", "delete", "upload", "download"]
    resources = ["server1", "server2", "database1", "api_gateway", "cloud_function"]
    status = ["sucess", "failure"]

    # Generate a list of random IP addresses
    ip_addresss = [f"192.168.1.{random.randint(2,254)}" for _ in range(3)] + \
                    [f"10.0.0.{random.randint(2,254)}" for _ in range(3)]

    # Defines fake malicious IP addresses
    malicous_ips = ["203.0.113.5", "198.51.100.7"]

    # Use a malicious IP address with a 10% chance, otherwise use a normal IP address
    if random.random() < 0.1:
        ip = random.choice(malicous_ips)
    else:
        ip = random.choice(ip_addresss)

    # Creates a Log Entry
    log = {
        "timestamp": datetime.now().isoformat(),
        "resource": random.choice(resources),
        "action": random.choice(actions),
        "status": random.choice(status),
        "ip_address": ip
        }
    return log

if __name__ == "__main__":
 # Append a new log entry to the file
 with open("logs.jsonl", "a") as f:
     log = generate_fake_log()
     f.write(json.dumps(log) + "\n")
     print(f"Generated log: {log}")