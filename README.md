##CMPE 273 – Week 1 Lab 1  
## Tiny Distributed System (HTTP)

### Overview
This project implements a tiny locally distributed system consisting of two independent services that communicate over HTTP. The goal is to demonstrate inter-service communication, basic logging, timeouts, and independent failure handling.


## Architecture

### Service A (Provider – Echo API)
- Runs on: `localhost:8080`
- Endpoints:
  - `GET /health` → returns `{"status":"ok"}`
  - `GET /echo?msg=hello` → returns `{"echo":"hello"}`

### Service B (Consumer)
- Runs on: `localhost:8081`
- Endpoints:
  - `GET /health` → returns `{"status":"ok"}`
  - `GET /call-echo?msg=hello`
    - Calls Service A `/echo`
    - Returns a combined JSON response

Both services run as **separate processes in separate terminals**.


## Technology Used
- Language: Python 3.10+
- Protocol: HTTP (REST)
- Framework: Flask
- HTTP Client: requests


## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/cmpe273-week1-lab1.git
cd cmpe273-week1-lab1
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.\.venv\Scripts\Activate.ps1 # Windows

3. Install dependencies
pip install -r requirements.txt

Running the Services
Terminal 1 – Start Service A
python python-http/service_a.py


Service A runs on http://127.0.0.1:8080

Terminal 2 – Start Service B
python python-http/service_b.py


Service B runs on http://127.0.0.1:8081

Logging

Each service logs every request with:

Service name

Endpoint

HTTP status code

Request latency (milliseconds)

Service B logs an error when Service A is unreachable or times out.

python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OR
.\.venv\Scripts\Activate.ps1 # Windows
pip install -r requirements.txt


