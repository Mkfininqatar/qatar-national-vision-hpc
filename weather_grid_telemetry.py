import time
import json
import logging

# Configure logger for Eco-Sensor & Weather Grid Telemetry
logging.basicConfig(
    filename='weather_grid_telemetry.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def analyze_eco_sensor_data(grid_id, moisture_level, magnetic_freq):
    """
    Analyzes soil moisture and magnetic frequency to determine 
    optimal planting zones for fruit trees.
    """
    # Threshold logic for optimal fruit tree growth
    is_moisture_optimal = 40.0 <= moisture_level <= 75.0
    is_freq_optimal = 100.0 <= magnetic_freq <= 250.0
    
    status = "OPTIMAL" if (is_moisture_optimal and is_freq_optimal) else "SUB-OPTIMAL"
    
    telemetry_data = {
        "grid_id": grid_id,
        "moisture_level": moisture_level,
        "magnetic_frequency": magnetic_freq,
        zone_status: status
    }
    
    if status == "OPTIMAL":
        logging.info(f"SUCCESS: Grid {grid_id} is optimal for planting. Data: {json.dumps(telemetry_data)}")
    else:
        logging.warning(f"WARNING: Grid {grid_id} requires soil conditioning. Data: {json.dumps(telemetry_data)}")
        
    return telemetry_data

if __name__ == "__main__":
    # Example test run for grid nodes
    sample_grids = [
        {"grid_id": "DOHA-GRID-01", "moisture": 62.5, "frequency": 145.2},
        {"grid_id": "LUSAIL-GRID-02", "moisture": 30.1, "frequency": 90.5}
    ]
    
    for grid in sample_grids:
        result = analyze_eco_sensor_data(grid["grid_id"], grid["moisture"], grid["frequency"])
        print(result)
