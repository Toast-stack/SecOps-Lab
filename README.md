# SecOps-Lab

A lightweight, modular project designed to simulate cloud security events, perform threat intelligence correlation, and display alerts on a simple Flask dashboard. This project helps demonstrate skills in cloud security monitoring, threat intelligence integration, automated incident response, and basic dashboard development.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Components](#project-components)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Introduction

This project serves as a cost-effective and resource-efficient example of modern security operations. It simulates cloud log generation, applies a threat intelligence module to flag suspicious activity, and displays incidents through a Flask-based web dashboard. The modular design allows you to extend its capabilities with real data sources or additional analysis modules over time.

---

## Features

- **Fake Log Generator:** Simulates cloud security events (e.g., logins, access, modifications) with randomly assigned attributes.
- **Threat Intelligence Module:** Checks log entries against a predefined list of malicious IP addresses.
- **Correlation Engine:** Processes logs to detect and flag suspicious events.
- **Flask Dashboard:** A simple, web-based interface showing identified security alerts and offering a JSON endpoint for all logs.
- **Automation Ready:** Easy to integrate with scheduled tasks (via cron or GitHub Actions) for periodic log generation and analysis.

---

## Project Components

1. **FakeLogsGen.py**  
   - Generates fake logs with various attributes like timestamp, resource, action, status, and IP address.
   - Outputs logs in JSON Lines format to `logs.jsonl`.

2. **ThreatIntel.py**  
   - Contains a static list of known malicious IP addresses.
   - Provides a helper function `is_malicious()` to verify if an IP is suspicious.

3. **CorrelationStation.py**  
   - Reads `logs.jsonl` and uses the threat intelligence module to flag any logs with malicious IPs.
   - Produces an alert list for further investigation.

4. **app.py (Flask Dashboard)**  
   - Serves a web interface displaying flagged alerts.
   - Provides a `/logs` endpoint for accessing all generated logs in JSON format.

5. **templates/index.html**  
   - The HTML template for the dashboard that displays the alert details.

---

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python 3 installed on your machine.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Toast-stack/SecOps-Lab
   cd SecOps Lab
   ```

2. ** Install Dependencies:**
   ```bash
   pip install flask
   ```

## Usage
### Generating Fake Logs
Run the fake log generator to simulate a new event:
```bash
python FakeLogsGen.py
```
Each time you run this script, a new log entry is appended to `logs.jsonl`.

### Processing Logs
To run the correlation station and see the alerts in the terminal:
```bash
python CorrelationStation.py
```

### Running the Flask Dashboard
Start the Flask application to view the dashboard:
```bash
python app.py
```
Open your browser and navigate to HTTP://127.0.0.1:5000/ to see the alerts dashboard.
You can also view all raw logs by visiting HTTP://127.0.0.1:5000/logs.

## Directory Structure
```
secops-lab/
├── app.py                  # Flask dashboard application
├── FakeLogsGen.py          # Generates fake log entries
├── CorrelationStation.py   # Correlates logs with threat intel
├── ThreatIntel.py          # Contains threat IP list and lookup logic
├── logs.jsonl              # Log file in JSON Lines format
├── templates/
    └── index.html          # HTML template for the dashboard
```

## Future Enhancements
- **Automation**: Integrate a scheduler (cron job or GitHub Actions) to generate logs periodically.
- **Extended Threat Intelligence**: Connect to free threat intelligence feeds (e.g., AlienVault OTX) for real-time data.
- **Enhanced Forensics**: Add modules for deeper forensic analysis on flagged incidents.
- **Improved UI**: Enhance the dashboard using modern front-end frameworks for a better user experience.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or additional features. When contributing, please adhere to the project’s coding standards and document new functionalities.

## License
This project is open source and available under the MIT License.

## Contact
- Zachary Nicholas
- GitHub: Toast-stack
- Discord: toast_stack

