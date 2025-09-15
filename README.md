# 🛡️ Log Sentinel

A Python-powered log monitoring & automation tool for modern systems engineer

## 🌟 Overview

Log Sentinel is a lightweight system utility designed to help engineers:

- Parse logs for errors & warnings
- Summarize patterns (top errors, HTTP status codes)
- Automate log rotation & maintenance
- Monitor disk space with alerts

This project simulates real-world tasks a Systems Engineer or DevOps Engineer would perform daily — and demonstrates scripting, troubleshooting, and automation skills.

⚡ Features
✅ Extract ERROR & WARNING logs from server files
✅ Summarize top error types and HTTP status codes
✅ Automatic log rotation (alerts.log → alerts.log.1)
✅ Disk space monitoring with low-space alerts

```
log-sentinel/
│
├── logs/
│ └── server.log # Sample log file for testing
│
├── log_sentinel.py # Main script
├── utils.py # Helper functions
├── README.md # Documentation
└── requirements.txt # Dependencies
```

## 📊 Example Output

Console:

```
Error Summary:
DiskFull: 5
NetworkDown: 2

HTTP Status Codes:
200: 1342
404: 56
500: 12

Disk Free: 72%
```

## Why This Project?

This project simulates real-world tasks a Systems/ Devops Engineer performs:

- Log parsing
- Data analysis
- Automation of maintenance tasks

👤 Mukhadis Yaru – Aspiring Cloud/ DevOps Engineer

LinkedIn: https://www.linkedin.com/in/mukhadis-yaru/
