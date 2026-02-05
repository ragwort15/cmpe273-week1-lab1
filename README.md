# CMPE 273 – Week 1 Lab 1  
## Tiny Distributed System (HTTP)

---

## Overview
This lab implements a tiny locally distributed system with two independent services that communicate over HTTP. The system demonstrates inter-service communication, basic logging, request timeouts, and independent failure handling.

---

## Architecture

### Service A (Provider – Echo API)
- Runs on `localhost:8080`

### Service B (Consumer)
- Runs on `localhost:8081`

Both services run as **separate processes in separate terminals**.

---

## **Step 1 – Clone the Repository**
```bash
git clone https://github.com/<your-username>/cmpe273-week1-lab1.git
cd cmpe273-week1-lab1

Step 2 – Set Up the Python Environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.\.venv\Scripts\Activate.ps1 # Windows
Step 3 – Start Service A (Provider)

Open Terminal 1 and run:
  python3 python-http/appA.py
Service A runs on:
http://127.0.0.1:8080


