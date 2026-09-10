import time
import requests
import datetime

API_URL = "http://localhost:8000"

def monitor_system():
    print("=" * 60)
    print("🇶🇦 TrustFlow QNV - Real-Time Telemetry & Health Monitor")
    print("=" * 60)
    
    while True:
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                data = response.json()
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Status: {data['telemetry']['status']} | Sync: {data['telemetry']['zero_drift_clock_sync']}")
            else:
                print(f"[{datetime.datetime.now()}] Warning: Server responded with status code {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"[{datetime.datetime.now()}] Alert: Cannot connect to TrustFlow backend server. Make sure trustflow_server.py is running.")
        
        time.sleep(5) # প্রতি ৫ সেকেন্ড পর পর টেলিমেট্রি স্ট্যাটাস চেক করবে

if __name__ == "__main__":
    monitor_system()
