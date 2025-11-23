from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter("request_count_total", "Total number of requests to /")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello — sample monitored app!"

@app.route("/metrics")
def metrics():
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
