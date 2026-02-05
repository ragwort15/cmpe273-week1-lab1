from flask import Flask, request, jsonify
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
app = Flask(__name__)

SERVICE_NAME = "A"

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

@app.get("/echo")
def echo():
    msg = request.args.get("msg", "")
    return jsonify(echo=msg)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
