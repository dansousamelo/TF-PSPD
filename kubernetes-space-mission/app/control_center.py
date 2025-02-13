from flask import Flask, request, jsonify
import logging
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

DATA_RECEIVED = Counter("data_received_total", "Total de requisições recebidas")

@app.route("/")
def index():
    return "🚀 Control Center está rodando!", 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200 

@app.route("/status")
def status():
    logging.info("📡 Status da missão solicitado!")
    return jsonify({"message": "Control Center online"}), 200

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json

    logging.info(f"📡 Dados recebidos: {data}")

    DATA_RECEIVED.inc()
    
    return jsonify({"message": "Dados recebidos"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
