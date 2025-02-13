import time
import requests

CONTROL_CENTER_URL = "http://control-center-service:5000/data"

while True:
    data = {"explorer_id": "Explorer-1", "coordinates": [42.0, 57.8], "status": "OK"}
    
    try:
        response = requests.post(CONTROL_CENTER_URL, json=data)
        print(f"🔭 Sent data: {data}, Response: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error sending data: {e}")

    time.sleep(5)