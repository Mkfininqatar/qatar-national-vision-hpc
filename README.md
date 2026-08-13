# qatar-national-vision-hpc
High-Performance Computing (HPC) cluster diagnostics and spatial-temporal logging, aligned with Qatar National Vision 2030 for smart infrastructure.
# hpc_telemetry.py
# Core Telemetry Engine for QNV HPC
# Author: Abdul Majeed (MIT/ISACA)

import os
import time
import json
import logging
# Import apnar core logger library theke
from python_logger2 import SpatialTemporalLogger

# Configuration
HPC_NODE_ID = os.getenv('HOSTNAME', 'HPC_NODE_01')
LOG_FILE = '/var/log/qnv_hpc_telemetry.log'
TWIN_API_URL = 'https://api.digitaltwin.qatar/v1/update'

# Initialize Logger
# Apnar 0% failure rate logger-er ekta instance
telemetry_logger = SpatialTemporalLogger(
    project='QNV_HPC_Monitor',
    node=HPC_NODE_ID,
    log_path=LOG_FILE,
    golden_sync_enabled=True
)

def get_hpc_metrics():
    """Simulates gathering HPC node metrics (CPU, RAM, Temp, Voltage)."""
    # Real implementation would use 'psutil' or specific HPC APIs
    # Ekhane just example data
    metrics = {
        'cpu_load_percent': 85.5,
        'mem_used_gb': 6.4, # Connected to your 8GB Ram note
        'temp_celsius': 72.1,
        'pmic_voltage_v': 1.19,
        'timestamp': time.time()
    }
    return metrics

def main_loop():
    while True:
        metrics = get_hpc_metrics()
        
        # Use apnar logger-er robust method
        telemetry_logger.log_state(
            state='HPC_OPERATIONAL',
            metrics=metrics,
            correlation_id='QNV_HPC_RUN_001'
        )
        
        # Simulate pushing data to Digital Twin API (future implementation)
        # print(f"Sending to Twin: {TWIN_API_URL} - {json.dumps(metrics)}")
        
        telemetry_logger.info("HPC Metrics logged successfully.")
        
        # Sleep for configured interval (e.g., 30 seconds, same as Actions run time)
        time.sleep(30)

if __name__ == '__main__':
    telemetry_logger.info("Starting QNV HPC Telemetry Service...")
    try:
        main_loop()
    except KeyboardInterrupt:
        telemetry_logger.info("Shutting down QNV HPC Telemetry Service.")
    except Exception as e:
        telemetry_logger.error(f"Critical failure: {e}")
        exit(1)
