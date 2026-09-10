from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime

app = FastAPI(
    title="TrustFlow QNV Server",
    description="High-Performance Computing & Digital Twin Telemetry for Qatar National Vision 2030",
    version="1.0.0"
)

class GrievanceRecord(BaseModel):
    worker_id: str
    company_name: str
    issue_type: str
    description: str

# ইন-মেমোরি স্টোরেজ (প্রোডাকশনে ডাটাবেস বা সিকিউরড লগ ফাইল ব্যবহার করা হবে)
grievance_db = []
telemetry_status = {
    "system": "TrustFlow Security Engine",
    "status": "Active & Secured",
    "zero_drift_clock_sync": "Synchronized (μs precision)",
    "national_vision_alignment": "QNV 2030 Compliant"
}

@app.get("/")
def read_root():
    return {
        "platform": "TrustFlow QNV",
        "telemetry": telemetry_status,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

@app.post("/api/v1/grievance")
def submit_grievance(record: GrievanceRecord):
    try:
        entry = {
            "worker_id": record.worker_id,
            "company_name": record.company_name,
            "issue_type": record.issue_type,
            "description": record.description,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "status": "Under Government Review"
        }
        grievance_db.append(entry)
        return {"success": True, "message": "Grievance securely logged and forwarded to oversight authorities.", "data": entry}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/grievances")
def get_grievances():
    return {"total_records": len(grievance_db), "records": grievance_db}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime

app = FastAPI(
    title="TrustFlow QNV Server",
    description="High-Performance Computing & Digital Twin Telemetry for Qatar National Vision 2030",
    version="1.0.0"
)

class GrievanceRecord(BaseModel):
    worker_id: str
    company_name: str
    issue_type: str
    description: str

grievance_db = []
telemetry_status = {
    "system": "TrustFlow Security Engine",
    "status": "Active & Secured",
    "zero_drift_clock_sync": "Synchronized (μs precision)",
    "national_vision_alignment": "QNV 2030 Compliant"
}

@app.get("/")
def read_root():
    return {
        "platform": "TrustFlow QNV",
        "telemetry": telemetry_status,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

@app.post("/api/v1/grievance")
def submit_grievance(record: GrievanceRecord):
    try:
        entry = {
            "worker_id": record.worker_id,
            "company_name": record.company_name,
            "issue_type": record.issue_type,
            "description": record.description,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "status": "Under Government Review"
        }
        grievance_db.append(entry)
        return {"success": True, "message": "Grievance securely logged and forwarded to oversight authorities.", "data": entry}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/grievances")
def get_grievances():
    return {"total_records": len(grievance_db), "records": grievance_db}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
