import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="QNV HPC Digital Twin Telemetry",
    page_icon="⚡",
    layout="wide"
)

# --- Header & Styling ---
st.title("🇶🇦 Qatar National Vision HPC - Cardio-Neural Digital Twin")
st.markdown("### Real-Time Infrastructure Diagnostics & Spatial-Temporal Telemetry Dashboard")
st.markdown("---")

# --- Sidebar Controls ---
st.sidebar.header("Telemetry Controls")
node_id = st.sidebar.selectbox("Select HPC Node", ["HPC_NODE_GRC_QATAR_01", "HPC_NODE_002", "HPC_NODE_003"])
refresh_rate = st.sidebar.slider("Refresh Interval (seconds)", 1, 10, 2)
sim_mode = st.sidebar.checkbox("Live Simulation Mode", value=True)

# --- Main Dashboard Metrics Layout ---
col1, col2, col3, col4 = st.columns(4)

metric_placeholder_cpu = col1.empty()
metric_placeholder_mem = col2.empty()
metric_placeholder_temp = col3.empty()
metric_placeholder_drift = col4.empty()

st.markdown("---")

# --- Real-Time Graph Section ---
st.subheader("📈 Live Wave Modulation & Resource Tracking")
chart_placeholder = st.empty()

# Historical data buffer for chart
chart_data = pd.DataFrame(columns=["Time", "CPU Load (%)", "Memory (GB)", "Temperature (°C)"])

# --- Simulation Loop ---
if sim_mode:
    for _ in range(100):
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Simulated metrics aligned with your HPC peak footprint
        cpu = round(random.uniform(78.0, 82.5), 2)
        mem = 8.37  # Peak optimization footprint
        temp = round(65.5 + (cpu / 10), 2)
        drift = "0.00 µs"
        
        # Update metrics cards
        metric_placeholder_cpu.metric(label="CPU Load", value=f"{cpu}%", delta="+0.4%")
        metric_placeholder_mem.metric(label="Memory Used", value=f"{mem} GB", delta="Optimal")
        metric_placeholder_temp.metric(label="Temperature", value=f"{temp} °C", delta="+0.1°C")
        metric_placeholder_drift.metric(label="Cumulative Drift", value=drift, delta="Synchronized")
        
        # Update dataframe for charts
        new_row = pd.DataFrame({"Time": [current_time], "CPU Load (%)": [cpu], "Memory (GB)": [mem], "Temperature (°C)": [temp]})
        chart_data = pd.concat([chart_data, new_row], ignore_index=True)
        
        # Keep last 20 entries for clean view
        if len(chart_data) > 20:
            chart_data = chart_data.tail(20)
            
        chart_placeholder.line_chart(chart_data.set_index("Time"))
        
        time.sleep(refresh_rate)
else:
    st.info("Simulation paused. Enable 'Live Simulation Mode' from the sidebar to start streaming telemetry.")
