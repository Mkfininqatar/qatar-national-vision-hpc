from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime

app = FastAPI(
    title="TrustFlow QNV Server",
    description="High-Performance Computing & Digital Twin Telemetry",
    version="1.0.0"
)

class GrievanceRecord(BaseModel):
    worker_id: str
    company_name: str
    issue_type: str
    description: str

grievance_db = []

@app.get("/")
def read_root():
    return {
        "platform": "TrustFlow QNV HPC Cluster",
        "status": "Operational"
    }

@app.post("/api/v1/grievance")
def submit_grievance(record: GrievanceRecord):
    data = record.dict()
    data["timestamp"] = datetime.datetime.utcnow().isoformat()
    grievance_db.append(data)
    return {"success": True, "record": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("trustflow_server:app", host="0.0.0.0", port=8000, reload=True)
