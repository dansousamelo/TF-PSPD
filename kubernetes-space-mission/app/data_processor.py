import requests
import time

CONTROL_CENTER_URL = "http://control-center-service:5000/status"

while True:
    try:
        response = requests.get(CONTROL_CENTER_URL)
        print(f"📊 Status da missão: {response.json()}")
    except Exception as e:
        print(f"🚨 Falha na comunicação com a missão: {e}")
    
    time.sleep(10)
