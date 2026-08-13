# hpc_telemetry.py
# Core Telemetry Engine for QNV HPC Diagnostics
# Author: Abdul Majeed (MIT Professional Education | ISACA Certified)
# Description: Gathers HPC node metrics (CPU, RAM, Temp, Voltage) and logs them 
#              using the spatial-temporal logging engine with golden synchronization.
#              Designed for high-availability, failure-free infrastructure monitoring.

import os
import time
import json
import logging
from datetime import datetime

# Import the core spatial-temporal logging engine
# Ensure python_logger2 is installed in the environment
try:
    from python_logger2 import SpatialTemporalLogger
except ImportError:
    print("Critical Error: 'python_logger2' module not found. Please install dependencies.")
    exit(1)

# --- Configuration ---
# Unique identifier for this HPC node, defaults to hostname
HPC_NODE_ID = os.getenv('HOSTNAME', 'HPC_NODE_001') 

# Path to the persistent log file
LOG_FILE_PATH = os.getenv('LOG_PATH', '/var/log/qnv_hpc_telemetry.log')

# Simulated API endpoint for Digital Twin synchronization (placeholder)
DIGITAL_TWIN_API_URL = os.getenv('TWIN_API_URL', 'https://api.digitaltwin.qatar/v1/sync')

# Logging interval in seconds (e.g., 30s)
LOG_INTERVAL = int(os.getenv('LOG_INTERVAL', 30))

# --- Initialization ---
# Initialize the logger with zero cumulative drift capability
telemetry_logger = SpatialTemporalLogger(
    project='QNV_HPC_Infrastructure',
    node=HPC_NODE_ID,
    log_path=LOG_FILE_PATH,
    golden_sync_enabled=True,
    # Set to logging.DEBUG for verbose output, INFO for production
    level=logging.INFO 
)

# Function to simulate gathering HPC metrics
def get_hpc_metrics():
    """
    Gathers real-time metrics from the HPC node.
    In a production environment, this would interface with system APIs,
    such as 'psutil' or vendor-specific hardware drivers.
    """
    try:
        # SIMULATION: Replace with actual hardware/OS calls
        import psutil 
        
        # Get basic system metrics
        cpu_load = psutil.cpu_percent(interval=None) # Non-blocking
        memory = psutil.virtual_memory()
        
        # Simulate temperature and voltage (requires hardware sensors like 'lm-sensors')
        # Using placeholder values for demonstration
        temp_celsius = 65.5 + (cpu_load / 10) # Temperature correlates with load
        pmic_voltage = 1.20 # Nominal voltage rail

        metrics = {
            'timestamp_utc': datetime.utcnow().isoformat(),
            'node_id': HPC_NODE_ID,
            'cpu_load_percent': cpu_load,
            'mem_total_gb': round(memory.total / (1024**3), 2),
            'mem_used_gb': round(memory.used / (1024**3), 2),
            'mem_percent': memory.percent,
            'temp_celsius': round(temp_celsius, 2),
            'pmic_voltage_v': pmic_voltage,
            'system_status': 'OPERATIONAL'
        }
        
        return metrics
    except ImportError:
        # Fallback simulation if psutil is not installed
        print("Warning: 'psutil' not found. Using static simulation data.")
        return {
            'timestamp_utc': datetime.utcnow().isoformat(),
            'node_id': HPC_NODE_ID,
            'cpu_load_percent': 85.5,
            'mem_total_gb': 8.0,
            'mem_used_gb': 6.4,
            'mem_percent': 80.0,
            'temp_celsius': 72.1,
            'pmic_voltage_v': 1.19,
            'system_status': 'SIMULATED'
        }
    except Exception as e:
        telemetry_logger.error(f"Error gathering metrics: {e}")
        return None

# Main execution loop
def run_telemetry_service():
    """
    Starts the continuous HPC telemetry monitoring service.
    """
    telemetry_logger.info(f"Starting QNV HPC Telemetry Service on node: {HPC_NODE_ID}")
    telemetry_logger.info(f"Logging interval: {LOG_INTERVAL}s | Log path: {LOG_FILE_PATH}")

    # Ensure the log directory exists
    log_dir = os.path.dirname(LOG_FILE_PATH)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    run_id = 0
    while True:
        run_id += 1
        telemetry_logger.info(f"Beginning telemetry cycle #{run_id}")

        # 1. Gather metrics
        metrics_data = get_hpc_metrics()

        if metrics_data:
            # 2. Log the state using the robust logger
            telemetry_logger.log_state(
                state='HPC_METRICS_GATHERED',
                metrics=metrics_data,
                correlation_id=f'QNV_HPC_RUN_{run_id:06d}'
            )
            telemetry_logger.info(f"HPC metrics logged successfully for cycle #{run_id}.")

            # 3. Simulate synchronization with Digital Twin API (Future implementation)
            # telemetry_logger.debug(f"Syncing with Digital Twin API: {DIGITAL_TWIN_API_URL}")
            # (Add API call logic here when ready)
        else:
            telemetry_logger.error(f"Failed to gather metrics for cycle #{run_id}. System might be unstable.")

        # 4. Sleep for the configured interval
        # The logger's golden sync helps ensure this sleep is not subject to cumulative drift
        time.sleep(LOG_INTERVAL)

if __name__ == '__main__':
    # Run the service with graceful error handling
    try:
        run_telemetry_service()
    except KeyboardInterrupt:
        telemetry_logger.info("Service interrupted by user. Shutting down QNV HPC Telemetry Service gracefully.")
    except Exception as e:
        telemetry_logger.critical(f"Unhandled exception caused service termination: {e}")
        # In a production setup, a systemd service would restart the script here
        exit(1)
