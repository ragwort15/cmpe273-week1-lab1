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

 – **Step 1-Clone the Repository**

git clone <your-github-repo-url>
cd <your-repo-directory>
 for example:
 git clone https://github.com/ragwort15/cmpe273-week1-lab1-starter.git
cd cmpe273-week1-lab1-starter

**Step 2 – Set Up the Python Environment**
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.\.venv\Scripts\Activate.ps1 # Windows
**Step 3 – Start Service A (Provider)**

Open Terminal 1 and run:
  python3 python-http/appA.py
Service A runs on:
http://127.0.0.1:8080

Test Service A:
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/echo?msg=hello

**Step 4 – Start Service B (Consumer)**

Open Terminal 2 and run:

python3 python-http/appB.py

Service B runs on:

http://127.0.0.1:8081
**Test success case**:

curl http://127.0.0.1:8081/call-echo?msg=hello

**Expected**:

HTTP 200

JSON response containing the echoed message from Service A

**Step 5 – Demonstrate Failure**

Stop Service A by pressing Ctrl + C in Terminal 1

Call Service B again:

curl -i http://127.0.0.1:8081/call-echo?msg=hello


Expected:

HTTP 503 Service Unavailable

Error message in the response

Error log printed by Service B

This demonstrates independent failure: Service B remains running even when Service A is down.

---

## Logging
Each service logs every request with:
- Service name
- Endpoint
- HTTP status code
- Request latency (milliseconds)

Service B logs an error when Service A is unreachable or times out.

---

## What Makes This Distributed?
This system is distributed because it consists of two independently running processes (Service A and Service B) that communicate over the network using HTTP. Service B depends on Service A by making an HTTP request, but each service can fail independently. When Service A is stopped, Service B remains operational and returns a 503 error while logging the failure.

**Screenshots of terminal**
<img width="1375" height="826" alt="image" src="https://github.com/user-attachments/assets/f9c07731-d5b3-42fd-a8be-c4b640b2811a" />

<img width="1435" height="786" alt="image" src="https://github.com/user-attachments/assets/fbcd7c1e-7813-4332-83f5-a05306d5d50c" />
Service A :
<img width="1154" height="869" alt="image" src="https://github.com/user-attachments/assets/80c13f92-66ec-44ee-a215-6aa7a122e7d1" />

Service B:
<img width="1404" height="657" alt="image" src="https://github.com/user-attachments/assets/e703b45e-58fc-47c2-8be9-91f807291820" />





