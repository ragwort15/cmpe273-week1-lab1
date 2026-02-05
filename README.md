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

