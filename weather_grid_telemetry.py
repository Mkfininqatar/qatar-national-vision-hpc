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
import json
import logging

# Configure advanced environmental logger
logging.basicConfig(
    filename='advanced_eco_weather_telemetry.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def evaluate_tree_growth_resonance(grid_id, moisture, magnetic_freq, weather_wave_freq, earth_rhythm):
    """
    Analyzes the synergy between eco-sensors, magnetic frequency, 
    weather wave frequency, and earth rhythm for optimal fruit tree growth.
    """
    # Calculating wave harmonization & rhythm score
    # Weather frequency and earth rhythm alignment logic
    resonance_index = (weather_wave_freq * earth_rhythm) / (abs(magnetic_freq - 150.0) + 1.0)
    
    # Growth viability threshold based on environmental harmony
    is_growth_optimal = (40.0 <= moisture <= 75.0) and (resonance_index >= 5.0)
    
    status = "HARMONIZED_OPTIMAL" if is_growth_optimal else "DISSUN_ADJUSTMENT_NEEDED"
    
    telemetry_payload = {
        "grid_id": grid_id,
        "soil_moisture": moisture,
        "magnetic_frequency": magnetic_freq,
        "weather_wave_frequency": weather_wave_freq,
        "earth_rhythm_factor": earth_rhythm,
        "resonance_index": round(resonance_index, 2),
        "growth_status": status
    }
    
    if is_growth_optimal:
        logging.info(f"OPTIMAL GROWTH ZONE: Grid {grid_id}. Data: {json.dumps(telemetry_payload)}")
    else:
        logging.warning(f"ADJUSTMENT REQUIRED: Grid {grid_id}. Data: {json.dumps(telemetry_payload)}")
        
    return telemetry_payload

if __name__ == "__main__":
    # Test simulation for Doha / regional grid nodes incorporating weather waves
    test_nodes = [
        {"grid_id": "DOHA-ECO-01", "moisture": 58.0, "mag_freq": 142.5, "weather_freq": 24.5, "rhythm": 3.2},
        {"grid_id": "LUSAIL-ECO-02", "moisture": 32.0, "mag_freq": 110.0, "weather_freq": 12.0, "rhythm": 1.5}
    ]
    
    for node in test_nodes:
        result = evaluate_tree_growth_resonance(
            node["grid_id"], 
            node["moisture"], 
            node["mag_freq"], 
            node["weather_freq"], 
            node["rhythm"]
        )
        print(result)
