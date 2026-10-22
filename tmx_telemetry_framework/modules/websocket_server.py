import asyncio
import json
import random
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Qatar Islamic Library - Real-Time SCADA WebSocket Server",
    version="1.0.0",
    description="Streams live sensor telemetry and simulation updates via WebSockets."
)

class ConnectionManager:
    """Manages active WebSocket connections for live telemetry broadcasting."""
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

def generate_live_telemetry_packet() -> dict:
    """Generates simulated real-time sensor updates for the library matrix."""
    return {
        "station_id": "QIL-SUB-CORE-01",
        "timestamp": asyncio.get_event_loop().time(),
        "metrics": {
            "vibrational_coherence_pct": round(98.0 + random.uniform(0.0, 1.8), 2),
            "base_frequency_hz": 432.0,
            "subterranean_core": {
                "temperature_celsius": round(22.5 + random.uniform(-0.2, 0.2), 2),
                "relative_humidity_pct": round(50.0 + random.uniform(-0.5, 0.5), 2),
                "pressure_differential_pa": round(30.0 + random.uniform(-1.0, 1.0), 2)
            },
            "hvac_power_consumption_kwh": round(521.1 + random.uniform(-5.0, 5.0), 2),
            "status": "OPTIMAL_LOCKED"
        }
    }

@app.websocket("/ws/telemetry")
async def websocket_telemetry_endpoint(websocket: WebSocket):
    """WebSocket endpoint that streams live simulation telemetry every 1 second."""
    await manager.connect(websocket)
    try:
        while True:
            packet = generate_live_telemetry_packet()
            await websocket.send_json(packet)
            await asyncio.sleep(1.0)  # Stream frequency: 1 update per second
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/", response_class=HTMLResponse)
async def get_dashboard_client():
    """Serves a lightweight HTML client to test and view live WebSocket telemetry streams."""
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Qatar Islamic Library - Live Telemetry Stream</title>
            <style>
                body { background-color: #080c14; color: #00ffff; font-family: monospace; padding: 20px; }
                h2 { color: #ff00ff; }
                pre { background-color: #05080f; border: 1px solid #112233; padding: 15px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h2>QATAR ISLAMIC LIBRARY - LIVE SCADA TELEMETRY STREAM</h2>
            <p>Connection Status: <span id="status" style="color: yellow;">Connecting...</span></p>
            <pre id="output">Waiting for telemetry packets...</pre>
            <script>
                const ws = new WebSocket("ws://" + window.location.host + "/ws/telemetry");
                ws.onopen = function() {
                    document.getElementById("status").innerText = "CONNECTED (SECURE)";
                    document.getElementById("status").style.color = "#00ff00";
                };
                ws.onmessage = function(event) {
                    const data = JSON.parse(event.data);
                    document.getElementById("output").innerText = JSON.stringify(data, null, 2);
                };
                ws.onclose = function() {
                    document.getElementById("status").innerText = "DISCONNECTED";
                    document.getElementById("status").style.color = "red";
                };
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("websocket_server:app", host="0.0.0.0", port=8000, reload=True)
