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
import streamlit as st
import numpy as np
import time

# --- ১. ফ্রিকোয়েন্সি ও ভাইব্রেশন ক্যালকুলেশন ফাংশনসমূহ ---
def calculate_wave_frequency(base_freq=7.83, harmonic_multiplier=1.601):
    current_time = time.time()
    omega = 2 * np.pi * base_freq * harmonic_multiplier
    wave_amplitude = np.sin(current_time * omega * 0.01)
    return {
        "effective_frequency": round(base_freq * harmonic_multiplier, 4),
        "instantaneous_amplitude": round(float(wave_amplitude), 4)
    }

def calculate_magnetic_frequency(geomagnetic_base=7.83, index_k=1.601):
    current_time = time.time()
    omega_m = 2 * np.pi * geomagnetic_base * index_k
    magnetic_fluctuation = np.cos(current_time * omega_m * 0.005)
    return {
        "effective_magnetic_frequency": round(geomagnetic_base * index_k, 4),
        "instantaneous_flux": round(float(magnetic_fluctuation), 4)
    }

def get_vibration_reading(base_acceleration=9.81, prime_factor=1.601):
    noise = np.random.normal(0, 0.05)
    vibration_amplitude = np.sin(time.time() * prime_factor) * 1.5 + noise
    frequency_hz = round(base_acceleration * prime_factor * 0.5, 2)
    return {
        "acceleration_ms2": round(float(vibration_amplitude), 4),
        "frequency_hz": frequency_hz,
        "status": "স্বাভাবিক (NORMAL)" if abs(vibration_amplitude) < 2.0 else "সতর্কবার্তা (WARNING)"
    }

# --- ২. Streamlit UI ড্যাশবোর্ড সেকশন (বাংলায়) ---
st.title("কাতার ন্যাশনাল ভিশন এইচপিসি - টেলিমেট্রি ও ডিজিটাল টুইন")

st.subheader("📡 রিয়েল-টাইম ওয়েভ, ম্যাগনেটিক এবং ভাইব্রেশন মেট্রিক্স")

# ডাটা ফেচ করা
wave_data = calculate_wave_frequency()
mag_data = calculate_magnetic_frequency()
vib_data = get_vibration_reading()

# ড্যাশবোর্ডে কলাম আকারে শো করা
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="ওয়েভ ফ্রিকোয়েন্সি (Wave Frequency)", value=f"{wave_data['effective_frequency']} Hz", delta=wave_data['instantaneous_amplitude'])

with col2:
    st.metric(label="ম্যাগনেটিক ফ্রিকোয়েন্সি (Magnetic Frequency)", value=f"{mag_data['effective_magnetic_frequency']} Hz", delta=mag_data['instantaneous_flux'])

with col3:
    st.metric(label="ভাইব্রেশন এক্সিলারেশন (Vibration)", value=f"{vib_data['acceleration_ms2']} m/s²", delta=vib_data['status'])
