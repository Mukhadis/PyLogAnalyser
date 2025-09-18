# 🛡️ Log Sentinel

A Python-powered log monitoring & automation tool for modern systems engineer

## 🌟 Overview

Log Sentinel is a lightweight system utility designed to help engineers:

- Parse logs for errors & warnings
- Summarize patterns (top errors, HTTP status codes)
- Automate log rotation & maintenance
- Monitor disk space with alerts

This project simulates real-world tasks a Systems Engineer or DevOps Engineer would perform daily — and demonstrates scripting, troubleshooting, and automation skills.

## ⚡ Features

**Interactive Menu System with 7 Options:**

1. ✅ **Parse error messages** - Extract ERROR logs from server files and store in alerts.log
2. ✅ **Error summary** - Display count of different error types from parsed logs
3. ✅ **HTTP status codes** - Analyze and display HTTP status code frequencies
4. ✅ **Disk space monitoring** - Check disk usage with low-space alerts
5. ✅ **Log rotation** - Rotate alerts.log to alerts.log.1 and create new alerts.log
6. ✅ **Delete aged files** - Remove files older than 1 minute from logs directory
7. ✅ **Quit** - Exit the program

```
log-sentinel/
│
├── logs/
│ ├── serverlogs/
│ │   └── server.log    # Main server log file for parsing
│ ├── alerts.log        # Generated from error parsing
│ └── alerts.log.1      # Rotated log backup
│
├── log_sentinel.py     # Main interactive script
├── utils.py           # Helper functions
├── README.md          # Documentation
└── requirements.txt   # Dependencies
```

## 📊 Example Usage

**Interactive Menu:**
```
Welcome to Log Sentinel:
      
Please read the below options to direct your requests:

1. Parse error messages and store seperately.
2. Print an error summary
3. Print HTTP status codes
4. Print disk space
5. Rotate Logs
6. Delete aged files
7. Quit
```

**Sample Output:**
```
1
Log parsing complete. Check alerts.log for ERROR messages.

2
Error Summary:
DiskFull: 2
NetworkDown: 1
AuthFailure: 1

4
Disk Free: 72%
```

## 🚀 Installation & Usage

1. **Clone or download** this repository
2. **Navigate** to the project directory
3. **Run the program:**
   ```bash
   python3 log_sentinel.py
   ```
4. **Select options** from the interactive menu (1-7)

## 💡 Prerequisites

- Python 3.x
- Sample log files in `logs/serverlogs/` directory
- Write permissions for log rotation and file deletion

## Why This Project?

This project simulates real-world tasks a Systems/DevOps Engineer performs:

- Log parsing and analysis
- Error pattern recognition
- Automated maintenance tasks
- System monitoring and alerts

👤 Mukhadis Yaru – Aspiring Cloud/ DevOps Engineer

LinkedIn: https://www.linkedin.com/in/mukhadis-yaru/
