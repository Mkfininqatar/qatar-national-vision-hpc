import streamlit as st
import time
import random
import pandas as pd
from datetime import datetime
import numpy as np

# --- ১. পেজ কনফিগারেশন ---
st.set_page_config(
    page_title="QNV HPC Digital Twin Telemetry",
    page_icon="⚡",
    layout="wide"
)

# --- ২. হেডার ও স্টাইলিং ---
st.title("🇶🇦 Qatar National Vision HPC - Cardio-Neural Digital Twin")
st.markdown("### Real-Time Infrastructure Diagnostics & Spatial-Temporal Telemetry Dashboard")
st.markdown("---")

# --- ৩. সাইডবার কন্ট্রোলস ---
st.sidebar.header("Telemetry Controls")
node_id = st.sidebar.selectbox("Select HPC Node", ["HPC_NODE_GRC_QATAR_01", "HPC_NODE_002", "HPC_NODE_003"])
refresh_rate = st.sidebar.slider("Refresh Interval (seconds)", 1, 10, 2)
sim_mode = st.sidebar.checkbox("Live Simulation Mode", value=True)

# --- ৪. কোর সিস্টেম ইনফ্রাস্ট্রাকচার লেআউট ---
st.subheader("🖥️ Core System Infrastructure")
col1, col2, col3, col4 = st.columns(4)
metric_cpu = col1.empty()
metric_mem = col2.empty()
metric_temp = col3.empty()
metric_drift = col4.empty()

st.markdown("---")

# --- ৫. গিটহাব কমিট ফিচার: ওয়েভ, ম্যাগনেটিক, গ্র্যাভিটি ও প্রক্সিমিটি মেট্রিক্স ---
st.subheader("📡 রিয়েল-টাইম ওয়েভ, ম্যাগনেটিক এবং ভাইব্রেশন মেট্রিক্স")
col5, col6, col7, col8 = st.columns(4)
metric_wave = col5.empty()
metric_mag = col6.empty()
metric_vib = col7.empty()
metric_prox = col8.empty()  # Proximity Sensor

st.markdown("---")

# --- ৬. রিয়েল-টাইม গ্রাফ সেকশন ---
st.subheader("📈 Live Wave Modulation & Resource Tracking")
chart_placeholder = st.empty()

# চার্টের ডাটা বাফার
chart_data = pd.DataFrame(columns=["Time", "CPU Load (%)", "Memory (GB)", "Temperature (°C)", "Gravity Wave (mG)"])

# --- ৭. সিমুলেশন ফাংশনসমূহ (কমিট হিস্ট্রি অনুযায়ী) ---
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

# Commit: Implement gravity wave reading simulation function
def get_gravity_wave_reading():
    base_gravity = 9.80665  # Doha baseline
    fluctuation = np.sin(time.time() * 0.5) * 0.002
    return round(base_gravity + fluctuation, 5)

# Commit: Implement proximity sensor simulation
def get_proximity_reading():
    distance = random.uniform(10.0, 150.0)  # cm distance to node rack
    status = "Secure" if distance > 30.0 else "Clearance Alert!"
    return {"distance_cm": round(distance, 1), "status": status}


# --- ৮. ইউনিফাইড রিয়েল-টাইম লাইভ লুপ ---
if sim_mode:
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Core Infrastructure Data
        cpu = round(random.uniform(78.0, 82.5), 2)
        mem = 8.37  
        temp = round(65.5 + (cpu / 10), 2)
        drift = "0.00 µs"
        
        # Advanced Telemetry Data
        wave_data = calculate_wave_frequency()
        mag_data = calculate_magnetic_frequency()
        vib_data = get_vibration_reading()
        g_wave = get_gravity_wave_reading()
        prox_data = get_proximity_reading()
        
        # UI কার্ড আপডেট (English Infrastructure)
        metric_cpu.metric(label="CPU Load", value=f"{cpu}%", delta="+0.4%")
        metric_mem.metric(label="Memory Used", value=f"{mem} GB", delta="Optimal")
        metric_temp.metric(label="Temperature", value=f"{temp} °C", delta="+0.1°C")
        metric_drift.metric(label="Cumulative Drift", value=drift, delta="Synchronized")
        
        # UI কার্ড আপডেট (Bangla Metrics + Proximity/Gravity)
        metric_wave.metric(
            label="ওয়েভ ফ্রিকোয়েন্সি (Wave Frequency)", 
            value=f"{wave_data['effective_frequency']} Hz", 
            delta=f"{wave_data['instantaneous_amplitude']:.4f}"
        )
        metric_mag.metric(
            label="ম্যাগনেটিক ফ্রিকোয়েন্সি (Magnetic Frequency)", 
            value=f"{mag_data['effective_magnetic_frequency']} Hz", 
            delta=f"{mag_data['instantaneous_flux']:.4f}"
        )
        metric_vib.metric(
            label="ভাইব্রেশন এক্সিলারেশন (Vibration)", 
            value=f"{vib_data['acceleration_ms2']} m/s²", 
            delta=vib_data['status']
        )
        metric_prox.metric(
            label="প্রক্সিমিটি সেন্সর (Proximity Sensor)",
            value=f"{prox_data['distance_cm']} cm",
            delta=prox_data['status']
        )
        
        # ডাটাফ্রেমে চার্ট ডাটা পুশ করা (Gravity Wave সহ)
        new_row = pd.DataFrame({
            "Time": [current_time], 
            "CPU Load (%)": [cpu], 
            "Memory (GB)": [mem], 
            "Temperature (°C)": [temp],
            "Gravity Wave (mG)": [g_wave]
        })
        chart_data = pd.concat([chart_data, new_row], ignore_index=True)
        
        if len(chart_data) > 20:
            chart_data = chart_data.tail(20)
            
        chart_placeholder.line_chart(chart_data.set_index("Time"))
        
        time.sleep(refresh_rate)
else:
    st.info("Simulation paused. Enable 'Live Simulation Mode' from the sidebar to start streaming telemetry.")
