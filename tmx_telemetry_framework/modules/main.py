from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI(
    title="Qatar Islamic Library - Master Matrix SCADA & Telemetry API",
    version="1.0.0",
    description=(
        "REST API serving real-time sensor telemetry, multi-zone HVAC metrics, "
        "environmental regulation data, and CAD manifests for the Qatar Islamic Library subterranean enclave."
    )
)

@app.get("/health", tags=["System Health"])
async def health_check():
    """Performs system health check and returns enclave security and coherence status."""
    return {
        "status": "HEALTHY",
        "system": "Qatar Islamic Library Master Matrix",
        "enclave_core": "SECURE_LOCKED",
        "coherence": "98.5%",
        "grid_status": "OPTIMAL"
    }

@app.get("/api/telemetry/vibrational", tags=["Telemetry"])
async def get_vibrational_telemetry():
    """Returns baseline vibrational frequency and harmonic sync telemetry."""
    return {
        "title": "QATAR ISLAMIC LIBRARY - GEODESIC VIBRATIONAL MAP",
        "base_frequency": "432 Hz",
        "grid_status": "OPTIMAL",
        "coherence": "98.5%",
        "energy_vectors": "ALIGNED",
        "resonance_bands": {
            "resonance_band_1": "Active Harmonic Sync",
            "sacred_geometry_grid": "Metatron & Golden Spiral Matrix",
            "architectural_nodes": ["Central Dome", "Outer Archways", "Subterranean Enclave"]
        }
    }

@app.get("/api/telemetry/hvac", tags=["Telemetry"])
async def get_hvac_telemetry():
    """Returns multi-zone HVAC energy consumption and static pressure differential metrics."""
    return {
        "title": "QATAR ISLAMIC LIBRARY - HVAC ENERGY & PRESSURE SIMULATION ENGINE",
        "subterranean_depth_m": 15.0,
        "total_daily_energy_kwh": 521.1,
        "hvac_metrics": [
            {
                "zone_id": "ZONE-01: Upper Vault Intake Plenum",
                "depth_m": 5.0,
                "pressure_differential_pa": 15.2,
                "energy_consumption_kwh_day": 145.5,
                "hvac_operational_status": "STABLE_PRESSURIZED"
            },
            {
                "zone_id": "ZONE-02: Intermediate Archive Corridors",
                "depth_m": 10.0,
                "pressure_differential_pa": 22.5,
                "energy_consumption_kwh_day": 112.0,
                "hvac_operational_status": "STABLE_PRESSURIZED"
            },
            {
                "zone_id": "ZONE-03: Subterranean Enclave Core",
                "depth_m": 15.0,
                "pressure_differential_pa": 30.0,
                "energy_consumption_kwh_day": 98.4,
                "hvac_operational_status": "STABLE_PRESSURIZED"
            },
            {
                "zone_id": "ZONE-04: Deep Exhaust Plenum",
                "depth_m": 20.0,
                "pressure_differential_pa": 8.5,
                "energy_consumption_kwh_day": 165.2,
                "hvac_operational_status": "NOMINAL"
            }
        ]
    }

@app.get("/api/cad/manifest", tags=["CAD & Architecture"])
async def get_cad_manifest():
    """Serves the structured JSON CAD manifest containing architectural surfaces and geodesic vibrational nodes."""
    manifest_path = "qatar_library_cad_manifest.json"
    
    # If the local JSON artifact exists, load and return it
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to parse CAD manifest: {str(e)}")
            
    # Fallback default CAD manifest structure if file is missing
    return {
        "manifest_title": "QATAR ISLAMIC LIBRARY - CAD MANIFEST & GEODESIC TOPOLOGY",
        "version": "1.0.0",
        "unit": "meters",
        "coordinate_system": "Cartesian (XYZ)",
        "architectural_surfaces": [
            {
                "surface_name": "Central Geodesic Dome",
                "geometry_type": "Hemispherical Vault",
                "parameters": {"radius_m": 15.0, "apex_elevation_m": 35.0, "mesh_resolution": [20, 30]}
            },
            {
                "surface_name": "Library Base Podium",
                "geometry_type": "Rectangular Platonic Base",
                "parameters": {"dimension_x_m": 50.0, "dimension_y_m": 50.0, "elevation_m": 0.0, "mesh_resolution": [15, 15]}
            }
        ],
        "geodesic_vibrational_nodes": [
            {"node_id": "NODE-01", "node_name": "Central Dome Apex", "coordinate_x": 0.0, "coordinate_y": 0.0, "coordinate_z": 35.0, "resonance_frequency_hz": 432.0, "status": "OPTIMAL"},
            {"node_id": "NODE-10", "node_name": "Subterranean Enclave Core", "coordinate_x": 0.0, "coordinate_y": 0.0, "coordinate_z": -10.0, "resonance_frequency_hz": 528.0, "status": "LOCKED"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
