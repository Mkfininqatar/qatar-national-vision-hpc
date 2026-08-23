import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="QNV HPC Telemetry", layout="wide")

st.title("🇶🇦 Qatar National Vision HPC - Cardio-Neural Digital Twin")
st.markdown("### Real-Time Infrastructure Diagnostics Dashboard")

node_id = st.sidebar.selectbox("Select Node", ["HPC_NODE_GRC_QATAR_01"])
refresh_rate = st.sidebar.slider("Refresh Interval (s)", 1, 10, 2)
sim_mode = st.sidebar.checkbox("Live Simulation Mode", value=True)

c1, c2, c3, c4 = st.columns(4)
p_cpu = c1.empty()
p_mem = c2.empty()
p_temp = c3.empty()
p_drift = c4.empty()

st.markdown("---")
chart_ph = st.empty()
data = pd.DataFrame(columns=["Time", "CPU Load (%)", "Memory (GB)", "Temperature (°C)"])

if sim_mode:
    for _ in range(100):
        t_str = datetime.now().strftime("%H:%M:%S")
        cpu = round(random.uniform(78.0, 82.5), 2)
        mem = 8.37
        temp = round(65.5 + (cpu / 10), 2)
        
        p_cpu.metric("CPU Load", f"{cpu}%", "+0.4%")
        p_mem.metric("Memory Used", f"{mem} GB", "Optimal")
        p_temp.metric("Temperature", f"{temp} °C", "+0.1°C")
        p_drift.metric("Cumulative Drift", "0.00 µs", "Synchronized")
        
        new_r = pd.DataFrame({"Time": [t_str], "CPU Load (%)": [cpu], "Memory (GB)": [mem], "Temperature (°C)": [temp]})
        data = pd.concat([data, new_r], ignore_index=True).tail(20)
        
        chart_ph.line_chart(data.set_index("Time"))
        time.sleep(refresh_rate)
else:
    st.info("Simulation paused.")
