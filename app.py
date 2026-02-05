from flask import Flask, request, jsonify
import time
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
app = Flask(__name__)

SERVICE_NAME = "B"
SERVICE_A = "http://127.0.0.1:8080"
TIMEOUT_SECONDS = 1.0

@app.before_request
def start_timer():
    request._start_time = time.perf_counter()

@app.after_request
def log_request(response):
    latency_ms = int((time.perf_counter() - request._start_time) * 1000)
    logging.info(
        f"service={SERVICE_NAME} endpoint={request.path} status={response.status_code} latency_ms={latency_ms}"
    )
    return response

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/call-echo")
def call_echo():
    msg = request.args.get("msg", "")
    try:
        r = requests.get(
            f"{SERVICE_A}/echo",
            params={"msg": msg},
            timeout=TIMEOUT_SECONDS
        )
        r.raise_for_status()
        return jsonify(serviceB="ok", serviceA=r.json())
    except requests.exceptions.Timeout as e:
        logging.error(f"service={SERVICE_NAME} error=timeout calling_service=A details={e}")
        return jsonify(error="service A timeout", serviceA="unavailable"), 503
    except requests.exceptions.RequestException as e:
        logging.error(f"service={SERVICE_NAME} error=failed calling_service=A details={e}")
        return jsonify(error="service A unavailable", serviceA="unavailable"), 503

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)
