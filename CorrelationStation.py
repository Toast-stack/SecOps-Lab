import json
from ThreatIntel import is_malicious

def process_logs(log_file="logs.jsonl"):
    # Read logs from the file
    alerts = []
    with open(log_file, "r") as f:
        for line in f:
            try:
                log = json.loads(line)
                if is_malicious(log["ip_address"]):
                    alerts.append(log)
            except json.JSONDecodeError:
                continue
    return alerts

if __name__ == "__main__":
    alerts = process_logs()
    if alerts:
        print("Suspicious activity detected:")
        for alert in alerts:
            print(alert)
    else:
        print("No suspicious activity detected.")