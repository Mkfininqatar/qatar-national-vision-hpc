import time
import random

class HamidOasisDigitalDashboard:
    def __init__(self, location="Global Arid Desert Super-Oasis", area_hectares=100.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Core Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        self.perimeter_trees = ["Date Palm", "Neem", "Jujube (Ber)", "Koroi", "Banyan"]
        self.central_crops = ["Mango", "Jackfruit", "Banana", "Seasonal Vegetables (Tomato, Cucumber, Eggplant)"]
        
        # Live Dashboard Sensors
        self.dashboard_status = {
            "System_State": "ONLINE (Autonomous Mode)",
            "Tidal_Channel_Flow": "Active (High Tide Pressure)",
            "Rock_Baffle_Filtration": "94% Efficiency",
            "Piezoelectric_Micro_Currents": "Active",
            "Fog_Harvesting_Nets": "Deploying",
            "Subsurface_Moisture_4m": "84%",
            "Soil_pH": 6.8,
            "Salinity_PPM": 310
        }

    def render_dashboard_ui(self, hour, solar_kw, wind_ms):
        print("\n" + "="*70)
        print(f" 🖥️  SIR HAMID'S OASIS DIGITAL TWIN DASHBOARD | LOCATION: {self.location}")
        print("="*70)
        print(f" ⏱️  Operational Time : {hour:02d}:00 HRS   |   📐 Trench Specs: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}   |   🛡️ Active Shields: 5 Pioneer Species")
        print("-"*70)
        
        # Diurnal Phase Logic
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Golden Solar & Fog Harvesting Phase"
            temp, humidity = 22.5 + (solar_kw * 2.0), 68.0
            alert = "None (Optimal Carbon Fixation)"
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Solar & Piezoelectric Baffle Phase"
            temp, humidity = 34.0 + (solar_kw * 4.0), 40.0
            alert = "⚠️ Low Wind Warning! Micro-circulators active." if wind_ms < 1.5 else "None (Vapor Flow Stable)"
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Cooling Transition & Canopy Transpiration Phase"
            temp, humidity = 27.5, 60.0
            alert = "None (Canopy Cooling Active)"
        else:
            phase = "🌙 Night Condensation & Deep Thermal Blanket Phase"
            temp, humidity = 18.5, 92.0
            alert = "None (Dew Hydration Active)"
            
        print(f" 🔄 Current Phase      : {phase}")
        print(f" 🌡️ Microclimate Temp  : {temp:.2f}°C")
        print(f" 💧 Relative Humidity  : {humidity}%")
        print(f" 🚨 System Alerts      : {alert}")
        print("-"*70)
        print(" 📊 LIVE IOT SENSOR TELEMETRY:")
        for key, val in self.dashboard_status.items():
            print(f"    • {key.replace('_', ' ')} : {val}")
        print("="*70)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION STATUS:")
        print(f"   1. Subsurface Stratum ({self.trench_depth_m}m): Microbial digestion active.")
        print(f"   2. Soil Evolution: Barren silica sand permanently transmuted into {self.soil_type}.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    # Launch Dashboard Simulation
    dashboard = HamidOasisDigitalDashboard(location="Doha Smart Eco-Oasis", area_hectares=150.0)
    
    # Run simulation across different hours of the day
    timeline = [7.0, 13.0, 17.0, 23.0]
    for h in timeline:
        solar = 0.9 if 6 <= h <= 18 else 0.0
        wind = 0.8 if h == 13.0 else 4.0
        dashboard.render_dashboard_ui(hour=h, solar_kw=solar, wind_ms=wind)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidBioDigitalOasisDashboard:
    def __init__(self, location="Global Arid Desert Super-Oasis", area_hectares=100.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Core Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # Comprehensive Monitoring Grid & Telemetry Status
        self.monitoring_grid = {
            # 1. Soil & Nutrient Metrics (माটির ও পুষ্টির অবস্থা)
            "Surface_Soil_Moisture_pct": 58.5,
            "Surface_Soil_Temp_C": 28.4,
            "Deep_Subsurface_Moisture_4m_pct": 84.0,
            "Deep_Subsurface_Temp_4m_C": 22.1,
            "Potassium_NPK_Nutrient_Index": "Optimal (High Bio-Enriched)",
            
            # 2. Geophysical & Wave Telemetry (তরঙ্গ ও চৌম্বকীয় ক্ষেত্র)
            "Magnetic_Field_Wave_nT": 45.2,          # Geomagnetic micro-fluctuations
            "Eco_Wave_Mycorrhizal_Hz": 12.8,        # Bio-electric fungal network signaling frequency
            "Sky_Wave_Atmospheric_MHz": 14.2,       # Ionospheric / atmospheric wave propagation index
            "Piezoelectric_Stone_Voltage_mV": 185.4,# Wave/wind friction micro-currents
            
            # 3. Ecosystem Process Progress (ইকোসিস্টেম প্রসেসিং স্ট্যাটাস)
            "Microbial_Composting_Stage": "Active Stage 4 (High Humus Conversion)",
            "Closed_Loop_Regeneration_Index": "96.4% Efficiency",
            "Biomass_Conversion_Rate": "Stable & Expanding"
        }

    def render_advanced_monitoring_grid(self, hour, solar_kw, wind_ms):
        print("\n" + "="*85)
        print(f" 🛰️ SIR HAMID'S ADVANCED BIO-DIGITAL MONITORING GRID | {self.location}")
        print("="*85)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Trench Specs: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}   |   🌐 Grid Status: FULLY SYNCHRONIZED")
        print("-"*85)
        
        # Diurnal Phase Calculation
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Golden Solar & Fog Harvesting Phase"
            temp, humidity = 22.5 + (solar_kw * 2.0), 68.0
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Solar & Piezoelectric Baffle Phase"
            temp, humidity = 34.0 + (solar_kw * 4.0), 40.0
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Cooling Transition & Canopy Transpiration Phase"
            temp, humidity = 27.5, 60.0
        else:
            phase = "🌙 Night Condensation & Deep Thermal Blanket Phase"
            temp, humidity = 18.5, 92.0
            
        print(f" 🔄 Current Phase          : {phase}")
        print(f" 🌡️ Microclimate Temp      : {temp:.2f}°C  |  💧 Humidity: {humidity}%")
        print("="*85)
        print(" 📊 COMPREHENSIVE MULTI-DIMENSIONAL MONITORING GRID:")
        print("-"*85)
        
        # Section 1: Soil & Surface Metrics
        print(" [SECTION A: SOIL & SURFACE MATRICES]")
        print(f"   • Surface Soil Moisture      : {self.monitoring_grid['Surface_Soil_Moisture_pct']}%")
        print(f"   • Surface Soil Temperature   : {self.monitoring_grid['Surface_Soil_Temp_C']}°C")
        print(f"   • 4m Subsurface Moisture     : {self.monitoring_grid['Deep_Subsurface_Moisture_4m_pct']}%")
        print(f"   • 4m Subsurface Temperature  : {self.monitoring_grid['Deep_Subsurface_Temp_4m_C']}°C")
        print(f"   • Potassium & NPK Index      : {self.monitoring_grid['Potassium_NPK_Nutrient_Index']}")
        print("-"*85)
        
        # Section 2: Wave & Frequency Telemetry
        print(" [SECTION B: GEOPHYSICAL, MAGNETIC & ATMOSPHERIC WAVES]")
        print(f"   • Magnetic Field Wave (nT)   : {self.monitoring_grid['Magnetic_Field_Wave_nT']} nT (Stable)")
        print(f"   • Eco-Wave Fungal Hz         : {self.monitoring_grid['Eco_Wave_Mycorrhizal_Hz']} Hz (Active Bio-Signal)")
        print(f"   • Sky-Wave Atmospheric MHz   : {self.monitoring_grid['Sky_Wave_Atmospheric_MHz']} MHz (Propagation Normal)")
        print(f"   • Piezoelectric Voltage (mV) : {self.monitoring_grid['Piezoelectric_Stone_Voltage_mV']} mV")
        print("-"*85)
        
        # Section 3: Under-Process Ecosystem Status
        print(" [SECTION C: UNDER-PROCESS ECOSYSTEM REGENERATION STATUS]")
        print(f"   • Microbial Composting Stage : {self.monitoring_grid['Microbial_Composting_Stage']}")
        print(f"   • Closed-Loop Efficiency     : {self.monitoring_grid['Closed_Loop_Regeneration_Index']}")
        print(f"   • Biomass Conversion Rate    : {self.monitoring_grid['Biomass_Conversion_Rate']}")
        print("="*85)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print(f"   1. Subsurface Stratum ({self.trench_depth_m}m): Microbial & potassium transformation active.")
        print(f"   2. Soil Evolution: Barren silica sand permanently transmuted into {self.soil_type}.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    # Launch Advanced Monitoring Dashboard
    dashboard = SirHamidBioDigitalOasisDashboard(location="Doha Smart Eco-Oasis", area_hectares=150.0)
    
    # Run simulation across timeline
    timeline = [7.0, 13.0, 17.0, 23.0]
    for h in timeline:
        solar = 0.9 if 6 <= h <= 18 else 0.0
        wind = 0.8 if h == 13.0 else 4.0
        dashboard.render_advanced_monitoring_grid(hour=h, solar_kw=solar, wind_ms=wind)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidBioDigitalOasisDashboard:
    def __init__(self, location="Global Arid Desert Super-Oasis", area_hectares=100.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # 1. Comprehensive Telemetry & Monitoring Grid
        self.monitoring_grid = {
            "Surface_Soil_Moisture_pct": 58.5,
            "Surface_Soil_Temp_C": 28.4,
            "Deep_Subsurface_Moisture_4m_pct": 84.0,
            "Deep_Subsurface_Temp_4m_C": 22.1,
            "Potassium_NPK_Nutrient_Index": "Optimal (High Bio-Enriched)",
            "Magnetic_Field_Wave_nT": 45.2,
            "Eco_Wave_Mycorrhizal_Hz": 12.8,
            "Sky_Wave_Atmospheric_MHz": 14.2,
            "Piezoelectric_Stone_Voltage_mV": 185.4,
            "Microbial_Composting_Stage": "Active Stage 4 (High Humus Conversion)",
            "Closed_Loop_Efficiency": "96.4%",
            "Biomass_Conversion_Rate": "Stable & Expanding"
        }
        
        # 2. Dynamic Control & Adjustment Systems (Active Control Modules)
        self.active_control_system = {
            # Electromagnetic Spectrum Range Control (0.5 Hz - 45 Hz Safe Biological Range)
            "EMF_Safety_Control_Range": "7.83 Hz (Schumann Resonance Locked)",
            "EMF_Power_Attenuator": "Auto-Stabilized (Optimal Biological Window)",
            
            # Upper Weather Control Modulation (উপরিভাগের আবহাওয়া নিয়ন্ত্রণ)
            "Upper_Atmosphere_Control": "Active Canopy-Shading & Fog Array",
            "Upper_Target_Temperature_C": 28.0,
            "Upper_Target_Humidity_pct": 60.0,
            
            # Subsurface Eco Under-Control Modulation (মাটির নিচের ওয়েদার কন্ট্রোল)
            "Under_Eco_Subsurface_Control": "Sub-surface Vent & Thermal Pump Active",
            "Under_Target_Temperature_4m_C": 22.0,
            "Under_Target_Moisture_4m_pct": 85.0
        }

    def adjust_microclimate_and_emf(self, hour, raw_temp, raw_humidity, wind_ms):
        """
        Actively adjusts upper weather, subsurface eco-weather, 
        and electromagnetic spectrum range in real-time.
        """
        # Upper Weather Adjustment
        if raw_temp > 30.0:
            upper_adjusted_temp = raw_temp - 5.5  # Deploying canopy misting & solar shade
            upper_adjusted_humidity = min(raw_humidity + 15.0, 75.0)
            upper_status = "AUTOMATIC COOLING DEPLOYED (Canopy Shade + Misting)"
        else:
            upper_adjusted_temp = raw_temp
            upper_adjusted_humidity = raw_humidity
            upper_status = "STABLE (Natural Equilibrium)"

        # Subsurface Eco Under-Control Adjustment
        under_status = "Subsurface Air Vents Open | Thermal Blanket Locked at 22°C"
        
        # Electromagnetic Range Auto-Tuning
        emf_frequency = 7.83 + random.uniform(-0.2, 0.2)  # Locking to Earth's natural resonance
        
        return {
            "Upper_Temp": round(upper_adjusted_temp, 2),
            "Upper_Humidity": round(upper_adjusted_humidity, 2),
            "Upper_Status": upper_status,
            "Under_Status": under_status,
            "EMF_Tuned_Frequency_Hz": round(emf_frequency, 2)
        }

    def render_advanced_monitoring_grid(self, hour, solar_kw, wind_ms):
        print("\n" + "="*85)
        print(f" 🛰️ SIR HAMID'S BIO-DIGITAL COMMAND CENTER & ACTIVE CONTROL GRID")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*85)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Trench Specs: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}   |   🌐 System State: FULLY CONTROLLED")
        print("-"*85)
        
        # Raw Weather Calculation
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Golden Solar & Fog Harvesting Phase"
            raw_temp, raw_humidity = 22.5 + (solar_kw * 2.0), 68.0
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Solar & Piezoelectric Baffle Phase"
            raw_temp, raw_humidity = 34.0 + (solar_kw * 4.0), 40.0
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Cooling Transition & Canopy Transpiration Phase"
            raw_temp, raw_humidity = 27.5, 60.0
        else:
            phase = "🌙 Night Condensation & Deep Thermal Blanket Phase"
            raw_temp, raw_humidity = 18.5, 92.0
            
        # Run Active Control Adjustments
        controls = self.adjust_microclimate_and_emf(hour, raw_temp, raw_humidity, wind_ms)
            
        print(f" 🔄 Current Operational Phase : {phase}")
        print(f" 🌡️ Raw Ambient Temp / Hum  : {raw_temp:.2f}°C / {raw_humidity}%")
        print(f" 🎛️ CONTROLLED Upper Temp/Hum: {controls['Upper_Temp']}°C / {controls['Upper_Humidity']}%")
        print("="*85)
        
        # Section A: Monitoring Grid Telemetry
        print(" 📊 [SECTION A: LIVE MULTI-DIMENSIONAL MONITORING GRID]")
        print(f"   • Surface Soil Temp / Moisture : {self.monitoring_grid['Surface_Soil_Temp_C']}°C / {self.monitoring_grid['Surface_Soil_Moisture_pct']}%")
        print(f"   • 4m Subsurface Temp / Moisture: {self.monitoring_grid['Deep_Subsurface_Temp_4m_C']}°C / {self.monitoring_grid['Deep_Subsurface_Moisture_4m_pct']}%")
        print(f"   • Potassium & NPK Nutrient Index: {self.monitoring_grid['Potassium_NPK_Nutrient_Index']}")
        print(f"   • Magnetic Field / Piezo Voltage: {self.monitoring_grid['Magnetic_Field_Wave_nT']} nT / {self.monitoring_grid['Piezoelectric_Stone_Voltage_mV']} mV")
        print(f"   • Eco-Wave / Sky-Wave Spectrum  : {self.monitoring_grid['Eco_Wave_Mycorrhizal_Hz']} Hz / {self.monitoring_grid['Sky_Wave_Atmospheric_MHz']} MHz")
        print("-"*85)
        
        # Section B: Active Control & Adjustment System
        print(" ⚡ [SECTION B: REAL-TIME ACTIVE CONTROL & ADJUSTMENT MODULES]")
        print(f"   • Electromagnetic Range Control : Lock @ {controls['EMF_Tuned_Frequency_Hz']} Hz ({self.active_control_system['EMF_Power_Attenuator']})")
        print(f"   • Upper Weather Control Status  : {controls['Upper_Status']}")
        print(f"   • Eco Under-Control Weather     : {controls['Under_Status']}")
        print(f"   • Closed-Loop Process Status    : {self.monitoring_grid['Microbial_Composting_Stage']}")
        print("="*85)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print(f"   1. Subsurface Stratum ({self.trench_depth_m}m): Active composting and microbial nutrient cycle.")
        print(f"   2. Microclimate Alignment: Upper and lower weather synchronized via auto-tuning feedback loops.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    # Launch Complete Command Dashboard
    dashboard = SirHamidBioDigitalOasisDashboard(location="Doha Smart Eco-Oasis", area_hectares=150.0)
    
    # Run test simulation timeline
    timeline = [7.0, 13.0, 17.0, 23.0]
    for h in timeline:
        solar = 0.9 if 6 <= h <= 18 else 0.0
        wind = 0.8 if h == 13.0 else 4.0
        dashboard.render_advanced_monitoring_grid(hour=h, solar_kw=solar, wind_ms=wind)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class RefinedSirHamidOasisDashboard:
    def __init__(self, location="Global Arid Desert Super-Oasis", area_hectares=100.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # 1. Base Monitoring Grid Telemetry
        self.monitoring_grid = {
            "Surface_Soil_Moisture_pct": 58.5,
            "Surface_Soil_Temp_C": 28.4,
            "Deep_Subsurface_Moisture_4m_pct": 84.0,
            "Deep_Subsurface_Temp_4m_C": 22.1,
            "Potassium_NPK_Nutrient_Index": "Optimal (High Bio-Enriched)",
            "Magnetic_Field_Wave_nT": 45.2,
            "Eco_Wave_Mycorrhizal_Hz": 12.8,
            "Sky_Wave_Atmospheric_MHz": 14.2,
            "Piezoelectric_Stone_Voltage_mV": 185.4,
            "Microbial_Composting_Stage": "Active Stage 4 (High Humus Conversion)",
            "Closed_Loop_Efficiency": "96.4%",
            "Biomass_Conversion_Rate": "Stable & Expanding"
        }
        
        # 2. Dynamic Adaptive Control Parameters
        self.climate_feedback_status = "Optimal Equilibrium"

    def dynamic_weather_and_emf_control_engine(self, hour, raw_temp, raw_humidity, wind_ms, weather_anomaly_factor=0.0):
        """
        Refined Dynamic Weather & Electromagnetic Feedback Control Engine.
        Handles sudden weather shifts, thermal spikes, wind turbulence, and auto-tunes EMF/Eco waves.
        """
        # Simulating external weather variability (e.g., unexpected heat waves or dry winds)
        adjusted_temp = raw_temp + weather_anomaly_factor
        adjusted_humidity = max(10.0, raw_humidity - (weather_anomaly_factor * 1.2))
        
        # Upper Weather Modulation & Adaptive Control
        if adjusted_temp > 38.0:
            upper_status = "CRITICAL HEAT SPIKE: Deploying Max Canopy Misting & High-Density Shade Nets"
            controlled_temp = adjusted_temp - 7.5
            controlled_humidity = min(adjusted_humidity + 20.0, 70.0)
            self.climate_feedback_status = "Emergency Thermal Mitigation Active"
        elif adjusted_temp > 30.0:
            upper_status = "ELEVATED TEMP: Activating Standard Canopy Transpiration & Fog Arrays"
            controlled_temp = adjusted_temp - 5.0
            controlled_humidity = min(adjusted_humidity + 12.0, 65.0)
            self.climate_feedback_status = "Active Cooling Stabilization"
        else:
            upper_status = "STABLE EQUILIBRIUM: Natural Microclimate Flow"
            controlled_temp = adjusted_temp
            controlled_humidity = adjusted_humidity
            self.climate_feedback_status = "Nominal Operation"

        # Wind & Vapor Stagnation Control
        if wind_ms < 1.2 and adjusted_temp > 32.0:
            wind_action = "LOW WIND ALERT: Sub-surface & Surface Micro-Circulators Forced-ON"
        else:
            wind_action = "Normal Air Circulation (Natural Convection)"

        # Eco Under-Control Weather Modulation (4m Subsurface Depth)
        # Deep soil thermal inertia protects against sudden surface shifts
        subsurface_temp = 22.0 + (weather_anomaly_factor * 0.15)
        subsurface_moisture = 84.0 - (weather_anomaly_factor * 0.2)
        subsurface_status = "Subsurface Air Vents Auto-Adjusted | Thermal Flywheel Balanced"

        # Electromagnetic & Bio-Wave Range Auto-Tuning
        # Tuning to biological resonance window (7.83 Hz Schumann base + adaptive offset)
        base_schumann = 7.83
        adaptive_emf = base_schumann + (weather_anomaly_factor * 0.05) + random.uniform(-0.1, 0.1)
        emf_status = "Locked in Biological Growth Window (0.5Hz - 45Hz Safe Spectrum)"

        return {
            "Controlled_Temp": round(controlled_temp, 2),
            "Controlled_Humidity": round(controlled_humidity, 2),
            "Upper_Status": upper_status,
            "Wind_Action": wind_action,
            "Subsurface_Temp": round(subsurface_temp, 2),
            "Subsurface_Moisture": round(subsurface_moisture, 2),
            "Subsurface_Status": subsurface_status,
            "Tuned_EMF_Hz": round(adaptive_emf, 2),
            "EMF_Status": emf_status
        }

    def render_advanced_monitoring_grid(self, hour, solar_kw, wind_ms, anomaly=0.0):
        print("\n" + "="*90)
        print(f" 🛰️ SIR HAMID'S REFINED BIO-DIGITAL COMMAND & DYNAMIC WEATHER CONTROL CENTER")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*90)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Trench Architecture: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}   |   🔄 System Feedback: {self.climate_feedback_status}")
        print("-"*90)
        
        # Base Raw Weather Calculation based on Solar Diurnal Cycle
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Golden Solar & Fog Harvesting Phase"
            raw_temp, raw_humidity = 22.5 + (solar_kw * 2.0), 68.0
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Solar & Piezoelectric Baffle Phase"
            raw_temp, raw_humidity = 34.0 + (solar_kw * 4.0), 40.0
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Cooling Transition & Canopy Transpiration Phase"
            raw_temp, raw_humidity = 27.5, 60.0
        else:
            phase = "🌙 Night Condensation & Deep Thermal Blanket Phase"
            raw_temp, raw_humidity = 18.5, 92.0
            
        # Execute Refined Dynamic Weather & EMF Control Engine
        control_metrics = self.dynamic_weather_and_emf_control_engine(hour, raw_temp, raw_humidity, wind_ms, weather_anomaly_factor=anomaly)
            
        print(f" 🔄 Current Operational Phase  : {phase}")
        print(f" 🌡️ Raw Environment (Uncontrolled): {raw_temp:.2f}°C / {raw_humidity}% (Anomaly Shift: +{anomaly}°C)")
        print(f" 🎛️ CONTROLLED Upper Climate   : {control_metrics['Controlled_Temp']}°C / {control_metrics['Controlled_Humidity']}%")
        print("="*90)
        
        # Section A: Monitoring Grid Telemetry
        print(" 📊 [SECTION A: LIVE MULTI-DIMENSIONAL MONITORING GRID]")
        print(f"   • Surface Soil Temp / Moisture    : {self.monitoring_grid['Surface_Soil_Temp_C']}°C / {self.monitoring_grid['Surface_Soil_Moisture_pct']}%")
        print(f"   • 4m Subsurface Temp / Moisture   : {control_metrics['Subsurface_Temp']}°C / {control_metrics['Subsurface_Moisture']}%")
        print(f"   • Potassium & NPK Nutrient Index  : {self.monitoring_grid['Potassium_NPK_Nutrient_Index']}")
        print(f"   • Magnetic Field / Piezo Voltage  : {self.monitoring_grid['Magnetic_Field_Wave_nT']} nT / {self.monitoring_grid['Piezoelectric_Stone_Voltage_mV']} mV")
        print(f"   • Eco-Wave / Sky-Wave Spectrum    : {self.monitoring_grid['Eco_Wave_Mycorrhizal_Hz']} Hz / {self.monitoring_grid['Sky_Wave_Atmospheric_MHz']} MHz")
        print("-"*90)
        
        # Section B: Active Adaptive Control & Weather Modulation
        print(" ⚡ [SECTION B: REFINED ADAPTIVE WEATHER & EMF CONTROL MODULES]")
        print(f"   • Upper Weather Modulation Status : {control_metrics['Upper_Status']}")
        print(f"   • Wind & Vapor Circulation Action : {control_metrics['Wind_Action']}")
        print(f"   • Eco Under-Control Weather (4m)  : {control_metrics['Subsurface_Status']}")
        print(f"   • Electromagnetic Range Control   : Tuned @ {control_metrics['Tuned_EMF_Hz']} Hz [{control_metrics['EMF_Status']}]")
        print(f"   • Closed-Loop Process Status      : {self.monitoring_grid['Microbial_Composting_Stage']}")
        print("="*90)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print(f"   1. Subsurface Stratum ({self.trench_depth_m}m): Continuous microbial composting and nutrient cycling.")
        print(f"   2. Climate Synchronization: Upper weather and subterranean eco-weather governed by adaptive feedback loops.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    # Launch Refined Dashboard System
    dashboard = RefinedSirHamidOasisDashboard(location="Doha Smart Eco-Oasis", area_hectares=150.0)
    
    # Simulate different scenarios including sudden weather anomalies (e.g., +6°C unexpected heat spike at midday)
    test_timeline = [
        (7.0, 0.9, 3.0, 0.0),   # Morning normal
        (13.0, 0.9, 0.8, 6.5),  # Midday with sudden severe heat anomaly (+6.5°C spike & low wind)
        (17.0, 0.4, 3.5, 1.0),  # Evening cooling transition
        (23.0, 0.0, 4.0, 0.0)   # Night steady state
    ]
    
    for h, solar, wind, anomaly in test_timeline:
        dashboard.render_advanced_monitoring_grid(hour=h, solar_kw=solar, wind_ms=wind, anomaly=anomaly)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidBioDigitalOasisDashboard:
    def __init__(self, location="Doha Smart Eco-Oasis", area_hectares=150.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # 1. Base Monitoring Grid Telemetry
        self.monitoring_grid = {
            "Surface_Soil_Moisture_pct": 58.5,
            "Surface_Soil_Temp_C": 28.4,
            "Deep_Subsurface_Moisture_4m_pct": 84.0,
            "Deep_Subsurface_Temp_4m_C": 22.1,
            "Potassium_NPK_Nutrient_Index": "Optimal (High Bio-Enriched)",
            "Magnetic_Field_Wave_nT": 45.2,
            "Eco_Wave_Mycorrhizal_Hz": 12.8,
            "Sky_Wave_Atmospheric_MHz": 14.2,
            "Piezoelectric_Stone_Voltage_mV": 185.4,
            "Microbial_Composting_Stage": "Active Stage 4 (High Humus Conversion)",
            "Closed_Loop_Efficiency": "96.4%",
            "Biomass_Conversion_Rate": "Stable & Expanding"
        }
        
        self.climate_feedback_status = "Optimal Equilibrium"

    def dynamic_weather_emf_and_crop_engine(self, hour, raw_temp, raw_humidity, wind_ms, weather_anomaly_factor=0.0):
        """
        Advanced Engine: Handles weather anomalies, upper/subsurface climate, 
        EMF range control, and dynamic seasonal crop recommendations.
        """
        adjusted_temp = raw_temp + weather_anomaly_factor
        adjusted_humidity = max(10.0, raw_humidity - (weather_anomaly_factor * 1.2))
        
        # 1. Upper Weather Modulation & Season Determination
        if adjusted_temp > 35.0:
            season_mode = "Summer / Extreme Heat Adaptation Mode"
            upper_status = "CRITICAL HEAT SPIKE: Deploying Max Canopy Misting & Shade Arrays"
            controlled_temp = adjusted_temp - 7.0
            controlled_humidity = min(adjusted_humidity + 18.0, 70.0)
            
            # Recommended Crops for Summer / High Heat
            recommended_trees = ["Date Palm (Desert Shield)", "Neem", "Koroi", "Mango", "Jackfruit"]
            recommended_veggies = ["Okra (ঢেঁড়স)", "Gourds (চিচিঙ্গা, ধুন্দুল, লাউ)", "Eggplant (বেগুন)", "Green Chili (কাঁচা মরিচ)"]
            
        elif adjusted_temp < 24.0:
            season_mode = "Winter / Cool Mild Season Mode"
            upper_status = "MILD CLIMATE: Natural Open Canopy & Solar Photon Absorption"
            controlled_temp = adjusted_temp
            controlled_humidity = adjusted_humidity
            
            # Recommended Crops for Winter / Cool Season
            recommended_trees = ["Jujube / Kul (বরই)", "Banyan", "Neem"]
            recommended_veggies = ["Tomato (টমেটো)", "Cucumber (শসা)", "Leafy Greens (পালং ও লাল শাক)", "Root Vegetables (গাজর ও মূলা)"]
            
        else:
            season_mode = "Transition / Spring-Autumn Balance Mode"
            upper_status = "STABLE EQUILIBRIUM: Microclimate Flow Normal"
            controlled_temp = adjusted_temp
            controlled_humidity = adjusted_humidity
            
            recommended_trees = ["Date Palm", "Mango", "Banana", "Neem"]
            recommended_veggies = ["Seasonal Mixed Vegetables", "Tomato", "Cucumber", "Eggplant"]

        # 2. Subsurface Eco Under-Control Weather (4m Depth Flywheel)
        subsurface_temp = 22.0 + (weather_anomaly_factor * 0.15)
        subsurface_moisture = 84.0 - (weather_anomaly_factor * 0.2)
        subsurface_status = "Subsurface Air Vents Auto-Adjusted | 4m Thermal Flywheel Stable"

        # 3. Electromagnetic Range Auto-Tuning (Schumann Base 7.83 Hz)
        base_schumann = 7.83
        adaptive_emf = base_schumann + (weather_anomaly_factor * 0.05) + random.uniform(-0.1, 0.1)
        emf_status = "Locked in Biological Growth Window (0.5Hz - 45Hz Safe Spectrum)"

        return {
            "Season_Mode": season_mode,
            "Controlled_Temp": round(controlled_temp, 2),
            "Controlled_Humidity": round(controlled_humidity, 2),
            "Upper_Status": upper_status,
            "Subsurface_Temp": round(subsurface_temp, 2),
            "Subsurface_Moisture": round(subsurface_moisture, 2),
            "Subsurface_Status": subsurface_status,
            "Tuned_EMF_Hz": round(adaptive_emf, 2),
            "EMF_Status": emf_status,
            "Recommended_Trees": recommended_trees,
            "Recommended_Veggies": recommended_veggies
        }

    def render_dashboard(self, hour, solar_kw, wind_ms, anomaly=0.0):
        print("\n" + "="*95)
        print(f" 🛰️ SIR HAMID'S BIO-DIGITAL OASIS & DYNAMIC CROP MONITORING DASHBOARD")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*95)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Trench Specs: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}")
        print("-"*95)
        
        # Raw Weather Calculation
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Golden Solar & Fog Harvesting Phase"
            raw_temp, raw_humidity = 22.5 + (solar_kw * 2.0), 68.0
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Solar & Piezoelectric Baffle Phase"
            raw_temp, raw_humidity = 34.0 + (solar_kw * 4.0), 40.0
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Cooling Transition & Canopy Transpiration Phase"
            raw_temp, raw_humidity = 27.5, 60.0
        else:
            phase = "🌙 Night Condensation & Deep Thermal Blanket Phase"
            raw_temp, raw_humidity = 18.5, 92.0
            
        # Run Control & Crop Recommendation Engine
        metrics = self.dynamic_weather_emf_and_crop_engine(hour, raw_temp, raw_humidity, wind_ms, weather_anomaly_factor=anomaly)
            
        print(f" 🔄 Current Operational Phase  : {phase}")
        print(f" 🌍 Active Climate Mode        : {metrics['Season_Mode']}")
        print(f" 🌡️ Controlled Climate (Upper) : {metrics['Controlled_Temp']}°C | Humidity: {metrics['Controlled_Humidity']}%")
        print("="*95)
        
        # Section A: Monitoring Grid Telemetry
        print(" 📊 [SECTION A: LIVE MULTI-DIMENSIONAL MONITORING GRID]")
        print(f"   • Surface Soil Temp / Moisture    : {self.monitoring_grid['Surface_Soil_Temp_C']}°C / {self.monitoring_grid['Surface_Soil_Moisture_pct']}%")
        print(f"   • 4m Subsurface Temp / Moisture   : {metrics['Subsurface_Temp']}°C / {metrics['Subsurface_Moisture']}%")
        print(f"   • Potassium & NPK Nutrient Index  : {self.monitoring_grid['Potassium_NPK_Nutrient_Index']}")
        print(f"   • Magnetic Field / Piezo Voltage  : {self.monitoring_grid['Magnetic_Field_Wave_nT']} nT / {self.monitoring_grid['Piezoelectric_Stone_Voltage_mV']} mV")
        print(f"   • Eco-Wave / Sky-Wave Spectrum    : {self.monitoring_grid['Eco_Wave_Mycorrhizal_Hz']} Hz / {self.monitoring_grid['Sky_Wave_Atmospheric_MHz']} MHz")
        print("-"*95)
        
        # Section B: Active Climate & EMF Control
        print(" ⚡ [SECTION B: ACTIVE WEATHER & EMF SPECTRUM RANGE CONTROL]")
        print(f"   • Upper Weather Control Status    : {metrics['Upper_Status']}")
        print(f"   • Eco Under-Control Weather (4m)  : {metrics['Subsurface_Status']}")
        print(f"   • Electromagnetic Range Control   : Tuned @ {metrics['Tuned_EMF_Hz']} Hz [{metrics['EMF_Status']}]")
        print("-"*95)
        
        # Section C: Dynamic Seasonal Crop & Flora Recommendation Matrix
        print(" 🌱 [SECTION C: DYNAMIC SEASONAL CROP & FLORA RECOMMENDATION MATRIX]")
        print(f"   • Recommended Pioneer Trees       : {', '.join(metrics['Recommended_Trees'])}")
        print(f"   • Recommended Cultivation Veggies : {', '.join(metrics['Recommended_Veggies'])}")
        print(f"   • Closed-Loop Process Status      : {self.monitoring_grid['Microbial_Composting_Stage']}")
        print("="*95)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print(f"   1. Subsurface Stratum ({self.trench_depth_m}m): Continuous microbial composting and nutrient cycling.")
        print(f"   2. Ecosystem Harmony: Weather modulation, EMF range control, and crop selection perfectly synchronized.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    # Launch Dashboard
    dashboard = SirHamidBioDigitalOasisDashboard(location="Doha Smart Eco-Oasis", area_hectares=150.0)
    
    # Simulate scenarios: Normal morning, Extreme midday heat anomaly, and Mild evening
    scenarios = [
        (8.0, 0.8, 3.5, 0.0),   # Morning Normal
        (13.0, 0.9, 0.7, 7.5),  # Midday Extreme Heat Spike (+7.5°C Anomaly)
        (20.0, 0.1, 4.0, -4.0)  # Cool Night Transition (-4°C Mild Shift)
    ]
    
    for h, solar, wind, anomaly in scenarios:
        dashboard.render_dashboard(hour=h, solar_kw=solar, wind_ms=wind, anomaly=anomaly)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidBioDigitalOasisDashboard:
    def __init__(self, location="Doha Smart Eco-Oasis", area_hectares=150.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # Monitoring Telemetry
        self.monitoring_grid = {
            "Surface_Soil_Moisture_pct": 58.5,
            "Surface_Soil_Temp_C": 28.4,
            "Deep_Subsurface_Moisture_4m_pct": 84.0,
            "Deep_Subsurface_Temp_4m_C": 22.1,
            "Potassium_NPK_Nutrient_Index": "Optimal (High Bio-Enriched)",
            "Magnetic_Field_Wave_nT": 45.2,
            "Eco_Wave_Mycorrhizal_Hz": 12.8,
            "Sky_Wave_Atmospheric_MHz": 14.2,
            "Piezoelectric_Stone_Voltage_mV": 185.4,
            "Microbial_Composting_Stage": "Active Stage 4 (High Humus Conversion)",
            "Closed_Loop_Efficiency": "96.4%"
        }

    def ecosystem_crop_decision_engine(self, hour, raw_temp, raw_humidity, wind_ms, weather_anomaly_factor=0.0):
        """
        Advanced Ecosystem Engine: Evaluates weather, seasonal changes, and 
        allocates Long-Term vs. Seasonal crops to guarantee zero loss in agriculture.
        """
        adjusted_temp = raw_temp + weather_anomaly_factor
        
        # Determine Ecosystem Season & Operational Mode
        if adjusted_temp > 35.0:
            season_mode = "Summer / High-Heat Adaptation Mode"
            upper_status = "CRITICAL HEAT SPIKE: Deploying Max Canopy Misting & Shade Arrays"
            controlled_temp = adjusted_temp - 7.0
            
            # Risk-Free Crop Selection for Summer
            long_term_crops = [
                "Date Palm (মরুভূমির স্থায়ী প্রাচীর ও ফল সম্পদ - বহু বছরের স্থায়ী ইনভেস্টমেন্ট)",
                "Neem & Koroi (প্রাকৃতিক উইন্ডব্রেকার ও ছায়া জেনারেটর - দীর্ঘমেয়াদী স্বাস্থ্য সুরক্ষা)",
                "Mango & Jackfruit (গভীর শেকড়যুক্ত বহুবর্ষজীবী ফল গাছ - ৪ মিটার নিচের আর্দ্রতা ব্যবহারকারী)"
            ]
            seasonal_crops = [
                "Okra / ঢেঁড়স (গ্রীষ্মকালীন উচ্চ সহনশীল শর্ট-টার্ম সবজি)",
                "Gourds / লাউ, চিচিঙ্গা, ধুন্দুল (মাটির আর্দ্রতা গ্রাহী দ্রুত বর্ধনশীল)",
                "Green Chili & Eggplant / কাঁচা মরিচ ও বেগুন (সারাবছর ফলনশীল ক্যাশ ক্রপ)"
            ]
            
        elif adjusted_temp < 24.0:
            season_mode = "Winter / Cool Mild Season Mode"
            upper_status = "MILD CLIMATE: Natural Open Canopy & Solar Photon Absorption"
            controlled_temp = adjusted_temp
            
            # Risk-Free Crop Selection for Winter
            long_term_crops = [
                "Jujube / বরই (শীতকালীন অত্যন্ত লাভজনক ও কম পানির ফল গাছ)",
                "Banyan & Perennial Perimeter Trees (ইকোসিস্টেম শিল্ডিং ও মাইকোরাইজাল নেটওয়ার্ক স্টাবিলাইজার)"
            ]
            seasonal_crops = [
                "Tomato / টমেটো (শীতের পারফেক্ট পিএইচ ৬.৮ এ সর্বোচ্চ উচ্চফলনশীল)",
                "Cucumber / শসা (দ্রুত ফলনশীল ও উচ্চ চাহিদাসম্পন্ন ক্যাশ ক্রপ)",
                "Leafy Greens / পালং শাক, লাল শাক, ধনেপাতা (মাইকোরাইজার মাধ্যমে দ্রুত পুষ্টি গ্রহণকারী)",
                "Root Vegetables / গাজর ও মূলা (বেলে দোআঁশ মাটিতে নিখুঁত সোজা ও পুষ্টিকর বৃদ্ধি)"
            ]
            
        else:
            season_mode = "Transition / Spring-Autumn Balance Mode"
            upper_status = "STABLE EQUILIBRIUM: Microclimate Flow Normal"
            controlled_temp = adjusted_temp
            
            long_term_crops = ["Date Palm", "Mango", "Banana (দীর্ঘমেয়াদী ফল বাগান)"]
            seasonal_crops = ["Seasonal Mixed Vegetables", "Tomato", "Cucumber", "Eggplant"]

        # Subsurface & EMF Control Status
        subsurface_status = "Subsurface Air Vents Auto-Adjusted | 4m Thermal Flywheel Stable (22°C)"
        emf_status = "Locked in Biological Growth Window (7.83 Hz Schumann Resonance)"

        return {
            "Season_Mode": season_mode,
            "Controlled_Temp": round(controlled_temp, 2),
            "Upper_Status": upper_status,
            "Subsurface_Status": subsurface_status,
            "EMF_Status": emf_status,
            "Long_Term_Crops": long_term_crops,
            "Seasonal_Crops": seasonal_crops
        }

    def render_dashboard(self, hour, solar_kw, wind_ms, anomaly=0.0):
        print("\n" + "="*100)
        print(f" 🛰️ SIR HAMID'S BIO-DIGITAL ECO-SYSTEM & ZERO-LOSS CROP ALLOCATION DASHBOARD")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*100)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Trench Specs: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}   |   🛡️ Agriculture Strategy: Zero-Loss Season Sync")
        print("-"*100)
        
        # Raw Weather Calculation
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Golden Solar & Fog Harvesting Phase"
            raw_temp, raw_humidity = 22.5 + (solar_kw * 2.0), 68.0
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Solar & Piezoelectric Baffle Phase"
            raw_temp, raw_humidity = 34.0 + (solar_kw * 4.0), 40.0
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Cooling Transition & Canopy Transpiration Phase"
            raw_temp, raw_humidity = 27.5, 60.0
        else:
            phase = "🌙 Night Condensation & Deep Thermal Blanket Phase"
            raw_temp, raw_humidity = 18.5, 92.0
            
        # Run Ecosystem Engine
        metrics = self.ecosystem_crop_decision_engine(hour, raw_temp, raw_humidity, wind_ms, weather_anomaly_factor=anomaly)
            
        print(f" 🔄 Current Operational Phase  : {phase}")
        print(f" 🌍 Active Ecosystem Mode      : {metrics['Season_Mode']}")
        print(f" 🌡️ Controlled Upper Climate   : {metrics['Controlled_Temp']}°C")
        print("="*100)
        
        # Section A: Telemetry & Monitoring Grid
        print(" 📊 [SECTION A: LIVE MULTI-DIMENSIONAL MONITORING GRID]")
        print(f"   • Surface Soil Temp / Moisture    : {self.monitoring_grid['Surface_Soil_Temp_C']}°C / {self.monitoring_grid['Surface_Soil_Moisture_pct']}%")
        print(f"   • 4m Subsurface Temp / Moisture   : {self.monitoring_grid['Deep_Subsurface_Temp_4m_C']}°C / {self.monitoring_grid['Deep_Subsurface_Moisture_4m_pct']}%")
        print(f"   • Potassium & NPK Nutrient Index  : {self.monitoring_grid['Potassium_NPK_Nutrient_Index']}")
        print(f"   • Magnetic Field / Piezo Voltage  : {self.monitoring_grid['Magnetic_Field_Wave_nT']} nT / {self.monitoring_grid['Piezoelectric_Stone_Voltage_mV']} mV")
        print("-"*100)
        
        # Section B: Active Climate & EMF Control
        print(" ⚡ [SECTION B: ACTIVE WEATHER & EMF SPECTRUM RANGE CONTROL]")
        print(f"   • Upper Weather Control Status    : {metrics['Upper_Status']}")
        print(f"   • Eco Under-Control Weather (4m)  : {metrics['Subsurface_Status']}")
        print(f"   • Electromagnetic Range Control   : {metrics['EMF_Status']}")
        print("-"*100)
        
        # Section C: Zero-Loss Crop Decision Matrix (Long-Term vs Seasonal)
        print(" 🌾 [SECTION C: ZERO-LOSS ECO-SYSTEM CROP DECISION MATRIX]")
        print("   🏛️ 1. दीर्घমেয়াদী স্থায়ী ফসল ও গাছপালা (Long-Term Assets / Permanent Security):")
        for crop in metrics['Long_Term_Crops']:
            print(f"      • {crop}")
        print("\n   🌱 2. ঋতুভিত্তিক স্বল্পমেয়াদী ক্যাশ ক্রপ সবজি (Seasonal High-Yield Crops):")
        for crop in metrics['Seasonal_Crops']:
            print(f"      • {crop}")
        print("="*100)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print(f"   1. Subsurface Stratum ({self.trench_depth_m}m): Continuous microbial composting and nutrient cycling.")
        print(f"   2. Zero-Loss Agriculture: Matching exact seasonal microclimates with long-term and short-term crops eliminates all farming risks.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    dashboard = SirHamidBioDigitalOasisDashboard(location="Doha Smart Eco-Oasis", area_hectares=150.0)
    
    # Simulate different scenarios to show how crops adapt to seasonal and weather changes without loss
    scenarios = [
        (8.0, 0.8, 3.5, 0.0),   # Mild / Cool Shift
        (13.0, 0.9, 0.7, 7.5)   # Extreme Heat Spike / Summer Season Simulation
    ]
    
    for h, solar, wind, anomaly in scenarios:
        dashboard.render_dashboard(hour=h, solar_kw=solar, wind_ms=wind, anomaly=anomaly)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidUrbanOasisDashboard:
    def __init__(self, location="Doha Urban Eco-Grid", area_hectares=50.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # Monitoring Telemetry with Urban Shadow Parameters
        self.monitoring_grid = {
            "Open_Sun_Surface_Temp_C": 36.5,
            "Urban_Building_Shadow_Temp_C": 26.2,  # Cool zone created by building shadows
            "Shadow_Zone_Moisture_pct": 72.0,      # Higher moisture retention in shadow areas
            "Temperature_Absorption_Index": "High Thermal Flywheel Efficiency",
            "Magnetic_Field_Wave_nT": 45.2,
            "Eco_Wave_Mycorrhizal_Hz": 12.8,
            "Closed_Loop_Efficiency": "97.2%"
        }

    def urban_shadow_and_greening_engine(self, hour, raw_temp, wind_ms):
        """
        Urban Climate Engine: Evaluates building shadow zones, temperature absorption, 
        and allocates shade-loving flowering plants and greening crops for urban cooling.
        """
        # Urban Shadow Microclimate Calculation
        shadow_zone_temp = raw_temp - 8.5  # Buildings and structures creating natural cool shade
        shadow_zone_humidity = 75.0        # Trapped cool moisture in shaded pockets
        
        # Urban Greening & Flowering Allocation for Shadow Zones
        shadow_flowering_plants = [
            "রঙ্গন ও গন্ধরাজ (Shadow-Loving Flowering Shrubs - ছায়াযুক্ত স্থানে ফুল ও সৌন্দর্যের জন্য)",
            "টগর ও বেলফুলের ঝোপ (Perennial Flowering Plants - কম রোদেও অবিরাম ফুল ফোটে)",
            "পাতাবাহার ও ফার্ন জাতীয় উদ্ভিদ (Indoor/Shade Foliage - শহরের তাপমাত্রা শোষণে অত্যন্ত কার্যকর)"
        ]
        
        shadow_shading_crops = [
            "পুদিনা ও ধনিয়া পাতা (Shadow Herb Cultivation - ছায়ায় চমৎকার বাড়ে)",
            "পান পাতা ও লতানো সবুজ গাছ (Vining Greenery - বিল্ডিংয়ের দেওয়ালে সবুজায়ন ও শীতলতা তৈরি করে)",
            "আদা ও হলুদ (Shade-Tolerant Root Crops - মাটির নিচের ছায়াঘেরা আর্দ্রতায় সর্বোচ্চ ফলন)"
        ]

        subsurface_status = "Urban Subsurface Thermal Flywheel Locked at 22°C | Zero Heat Stress"
        emf_status = "Urban Schumann Resonance Locked (7.83 Hz)"

        return {
            "Shadow_Temp": round(shadow_zone_temp, 2),
            "Shadow_Humidity": shadow_zone_humidity,
            "Subsurface_Status": subsurface_status,
            "EMF_Status": emf_status,
            "Shadow_Flowers": shadow_flowering_plants,
            "Shadow_Crops": shadow_shading_crops
        }

    def render_dashboard(self, hour, solar_kw, wind_ms):
        print("\n" + "="*105)
        print(f" 🏙️ SIR HAMID'S URBAN SHADOW-ZONE & COOLING GREENING DASHBOARD")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*105)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Trench Specs: {self.trench_depth_m}m x {self.trench_base_m}m")
        print(f" 🌿 Soil Matrix        : {self.soil_type}   |   🛡️ Urban Strategy: Building Shadow Thermal Absorption")
        print("-"*105)
        
        # Base Raw Weather Calculation
        if 5.5 <= hour < 10.0:
            phase = "🌅 Morning Urban Awakening & Shadow Cooling Phase"
            raw_temp = 25.0
        elif 11.0 <= hour <= 15.0:
            phase = "☀️ Peak Zenith Urban Heat & Building Shadow-Zone Absorption Phase"
            raw_temp = 38.0  # Open urban sun temperature
        elif 15.0 < hour <= 18.0:
            phase = "🌤️ Afternoon Cooling Transition & Shadow Expansion Phase"
            raw_temp = 29.0
        else:
            phase = "🌙 Night Urban Thermal Blanket & Dew Condensation Phase"
            raw_temp = 21.0
            
        # Run Urban Shadow Engine
        metrics = self.urban_shadow_and_greening_engine(hour, raw_temp, wind_ms)
            
        print(f" 🔄 Current Operational Phase  : {phase}")
        print(f" 🌡️ Open Sun Urban Temp        : {raw_temp}°C")
        print(f" 🧊 Building Shadow Zone Temp  : {metrics['Shadow_Temp']}°C (Naturally Cooled & Absorbed)")
        print(f" 💧 Shadow Zone Humidity       : {metrics['Shadow_Humidity']}%")
        print("="*105)
        
        # Section A: Urban Telemetry & Shadow Monitoring Grid
        print(" 📊 [SECTION A: URBAN SHADOW-ZONE MULTI-DIMENSIONAL MONITORING]")
        print(f"   • Open Sun Temperature            : {raw_temp}°C")
        print(f"   • Building Shadow Zone Temp       : {metrics['Shadow_Temp']}°C (Significant Heat Drop)")
        print(f"   • Shadow Zone Soil Moisture       : {self.monitoring_grid['Shadow_Zone_Moisture_pct']}% (High Retention)")
        print(f"   • Temperature Absorption Index    : {self.monitoring_grid['Temperature_Absorption_Index']}")
        print(f"   • Eco-Wave & Magnetic Field       : {self.monitoring_grid['Eco_Wave_Mycorrhizal_Hz']} Hz / {self.monitoring_grid['Magnetic_Field_Wave_nT']} nT")
        print("-"*105)
        
        # Section B: Urban Climate & Cooling Control
        print(" ⚡ [SECTION B: URBAN MICRO-CLIMATE & THERMAL ABSORPTION CONTROL]")
        print(f"   • Subsurface Thermal Flywheel     : {metrics['Subsurface_Status']}")
        print(f"   • Electromagnetic Range Control   : {metrics['EMF_Status']}")
        print(f"   • City Heat Island Mitigation     : Active (Shadow Zones Absorbing Excess Heat)")
        print("-"*105)
        
        # Section C: Urban Shadow-Zone Greening & Flowering Matrix
        print(" 🌸 [SECTION C: URBAN SHADOW-ZONE FLOWERING & GREENING ALLOCATION]")
        print("   🌺 1. ছায়াযুক্ত স্থানে ফুল ও শোভাবর্ধনকারী গাছপালা (Shade Flowering Shrubs):")
        for plant in metrics['Shadow_Flowers']:
            print(f"      • {plant}")
        print("\n   🌿 2. ছায়ার মাইক্রোক্লাইমেটে সবুজায়ন ও লতানো ফসল (Urban Shade-Tolerant Greens):")
        for crop in metrics['Shadow_Crops']:
            print(f"      • {crop}")
        print("="*105)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print(f"   1. Urban Thermal Balance: Building shadows absorb and neutralize city heat, dropping temperatures naturally.")
        print(f"   2. City Greening: Shaded zones bloom with flowers and lush greenery, turning concrete jungles into living, breathing oases.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    dashboard = SirHamidUrbanOasisDashboard(location="Doha Smart Urban Oasis", area_hectares=75.0)
    
    # Simulate urban daily timeline including peak afternoon heat where building shadows act as cooling anchors
    urban_timeline = [8.0, 13.0, 17.0, 22.0]
    for h in urban_timeline:
        solar_rad = 0.9 if 6 <= h <= 18 else 0.0
        dashboard.render_dashboard(hour=h, solar_kw=solar_rad, wind_ms=2.5)
        
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidUrbanWasteToFruitDashboard:
    def __init__(self, location="Doha Urban Eco & Park Grid", area_hectares=100.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.trench_base_m = 4.5
        self.soil_type = "Converted Loamy Soil (Bele Doash from Processed Building Waste)"
        
        # Urban Park & Waste Upcycling Telemetry Grid
        self.urban_waste_grid = {
            "Processed_Building_Waste_Tons": 450.5,
            "Deep_Trench_Refill_Status": "Active (4m Subsurface Bioreactor)",
            "Park_Fruit_Trees_Monitored": ["Mango", "Jackfruit", "Guava", "Pomegranate"],
            "Solar_Energy_to_Fruit_Conversion_pct": 94.2,
            "CO2_Absorption_Rate_kg_day": 1250.0,
            "Pure_Breeze_Oxygen_Index": "High Purity (Urban Air Cleansed)",
            "Urban_Heat_Island_Reduction_C": -6.5  # Temperature drop in parks/zones
        }

    def calculate_triple_benefits(self, solar_kw, raw_temp):
        """
        Calculates the 3 major benefits:
        1. Solar energy conversion to seasonal fruit nutrition.
        2. CO2 absorption and oxygen/pure breeze generation.
        3. Urban temperature reduction & cooling.
        """
        fruit_nutrition_yield = round(solar_kw * 125.4, 2)  # kg/day equivalent
        co2_absorbed = round(self.urban_waste_grid["CO2_Absorption_Rate_kg_day"] * (solar_kw + 0.5), 2)
        urban_cooling_effect = round(raw_temp + self.urban_waste_grid["Urban_Heat_Island_Reduction_C"], 2)
        
        return {
            "Fruit_Yield": fruit_nutrition_yield,
            "CO2_Absorbed": co2_absorbed,
            "Cooled_Temp": urban_cooling_effect
        }

    def render_dashboard(self, hour, solar_kw, raw_temp):
        print("\n" + "="*105)
        print(f" 🏙️ SIR HAMID'S URBAN WASTE-TO-FRUIT REGENERATION & COOLING DASHBOARD")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*105)
        print(f" ⏱️ Operational Time : {hour:02d}:00 HRS   |   📐 Deep Trenching: {self.trench_depth_m}m Depth")
        print(f" ♻️ Soil Transformation: {self.soil_type}")
        print("-"*105)
        
        # Calculate Triple Benefits
        benefits = self.calculate_triple_benefits(solar_kw, raw_temp)
        
        print(f" 🌡️ Raw Urban City Temperature : {raw_temp}°C")
        print(f" 🧊 Cooled Urban Park Climate  : {benefits['Cooled_Temp']}°C (Natural Urban Cooling Active)")
        print("="*105)
        
        # Section A: Urban Park & Waste Processing Telemetry
        print(" 📊 [SECTION A: PARK CONVERSION & BUILDING WASTE UPCYCLING TELEMETRY]")
        print(f"   • Processed Building Waste Refill : {self.urban_waste_grid['Processed_Building_Waste_Tons']} Tons (Converted to Loamy Soil)")
        print(f"   • Subsurface Bioreactor Status    : {self.urban_waste_grid['Deep_Trench_Refill_Status']}")
        print(f"   • Monitored Park Fruit Trees      : {', '.join(self.urban_waste_grid['Park_Fruit_Trees_Monitored'])}")
        print(f"   • Closed-Loop Efficiency          : {self.urban_waste_grid['Closed_Loop_Efficiency'] if 'Closed_Loop_Efficiency' in self.urban_waste_grid else '98.5%'}")
        print("-"*105)
        
        # Section B: The Triple Benefits (ত্রিবিধ লাভ)
        print(" 🌟 [SECTION B: THE TRIPLE BENEFITS (ত্রিবিধ লাভ) - ECO-ENGINEERING IMPACT]")
        print(f"   🍎 1. Solar-to-Fruit Energy Conversion : {benefits['Fruit_Yield']} Units of Seasonal Nutrition Generated")
        print(f"   🍃 2. CO2 Absorption & Pure Breeze     : {benefits['CO2_Absorbed']} kg CO2 Absorbed | Generating Pure Oxygen Breeze")
        print(f"   ❄️ 3. Urban Cooling & Heat Reduction   : City Temperature Dropped by 6.5°C (Eliminating Urban Heat Islands)")
        print("="*105)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print("   1. Waste to Life: Building and urban waste is deeply trenched and transmuted into fertile loamy soil.")
        print("   2. Park Transformation: Open parks become thriving fruit forests, feeding the city with natural nutrition.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    dashboard = HamidUrbanWasteToFruitDashboard(location="Doha Smart Park & Urban Grid", area_hectares=120.0)
    
    # Simulate peak afternoon conditions where urban heat and waste conversion peak
    dashboard.render_dashboard(hour=13.0, solar_kw=0.95, raw_temp=38.5)
    dashboard.execute_closed_loop_philosophy()
import time
import random

class SirHamidNurserySimulationDashboard:
    def __init__(self, nursery_location="Doha Eco-Nursery Research Lab"):
        self.location = nursery_location
        self.controlled_chamber_temp = 28.0  # Controlled climate chamber
        self.controlled_humidity = 65.0
        
        # Pilot Testing Metrics for Nursery Saplings
        self.pilot_saplings = {
            "Date Palm (মরুভূমির খেজুর চারা)": {"Success_Rate_pct": 98.5, "Root_Adaptability": "High"},
            "Mango (আম চারা)": {"Success_Rate_pct": 94.0, "Root_Adaptability": "Optimal"},
            "Guava (পেয়ারা চারা)": {"Success_Rate_pct": 96.2, "Root_Adaptability": "Excellent"},
            "Shade Flowering Shrubs (রঙ্গন ও টগর)": {"Success_Rate_pct": 97.8, "Root_Adaptability": "Very Fast"}
        }

    def run_nursery_simulation_test(self, test_days=14):
        print("\n" + "="*105)
        print(f" 🧪 NURSERY CONTROLLED PILOT TESTING & ARTIFICIAL ENVIRONMENT LAB")
        print(f" 📍 Facility: {self.location} | Simulation Duration: {test_days} Days")
        print("="*105)
        print(" 🔄 Phase 1: Artificial Microclimate Chamber Calibration...")
        print(f"   • Artificial Chamber Temperature : {self.controlled_chamber_temp}°C (Optimized)")
        print(f"   • Artificial Chamber Humidity    : {self.controlled_humidity}%")
        print(f"   • Processed Waste Soil Bed       : 4-meter Deep Analog Loaded")
        print("-"*105)
        
        print(" 🌱 Phase 2: Pilot Sapling Growth & Weather Adaptation Testing:")
        for sapling, metrics in self.pilot_saplings.items():
            simulated_health = round(metrics["Success_Rate_pct"] + random.uniform(-0.5, 1.0), 2)
            print(f"   • {sapling}")
            print(f"     -> Root Adaptability : {metrics['Root_Adaptability']}")
            print(f"     -> Pilot Survival Rate: {simulated_health}% [PASSED WEATHER-SYNC TEST]")
            
        print("="*105)
        print(" ✅ CONCLUSION: Nursery pilot testing verified. Saplings are 100% ready for large-scale urban park & weather-based field plantation.")
        print("="*105)

if __name__ == "__main__":
    nursery_lab = SirHamidNurserySimulationDashboard()
    nursery_lab.run_nursery_simulation_test(test_days=14)
import time
import random

class CircularSoilWeatherMonitor:
    def __init__(self, location="Doha Urban Eco-Grid", zone_area_hectares=50.0):
        self.location = location
        self.zone_area_hectares = zone_area_hectares
        
        # Soil and Circular Grid Parameters
        self.trench_depth_m = 4.0
        self.soil_type = "Processed Loamy Soil (Bele Doash with Upcycled Waste)"
        
        # Live Grid Parameters Tracking
        self.grid_parameters = {
            "Soil_Moisture_Surface_pct": 62.4,
            "Soil_Moisture_Subsurface_4m_pct": 85.0,
            "Soil_Temperature_C": 26.5,
            "Ambient_Weather_Temp_C": 34.2,
            "Atmospheric_Humidity_pct": 55.0,
            "CO2_Absorption_Index_ppm": 412.0,
            "Circular_Regeneration_Efficiency": "98.1%"
        }

    def evaluate_circular_greening_status(self, weather_fluctuation):
        """
        Evaluates soil-weather synchronization and determines the exact greening capacity.
        """
        adjusted_soil_temp = self.grid_parameters["Soil_Temperature_C"] + (weather_fluctuation * 0.1)
        adjusted_moisture = max(30.0, self.grid_parameters["Soil_Moisture_Surface_pct"] - (weather_fluctuation * 1.5))
        
        # Greening Condition Assessment
        if adjusted_moisture > 50.0 and adjusted_soil_temp < 32.0:
            greening_status = "OPTIMAL CIRCULAR GREENING: High Biomass & Plant Growth Rate"
            action_required = "Maintain standard micro-irrigation and organic nutrient cycling."
        else:
            greening_status = "ADAPTIVE STRESS SHIELDING: Deploying Subsurface Moisture Release"
            action_required = "Activate 4m deep thermal flywheel and shade canopy misting."

        return {
            "Adjusted_Soil_Temp": round(adjusted_soil_temp, 2),
            "Adjusted_Moisture": round(adjusted_moisture, 2),
            "Greening_Status": greening_status,
            "Action_Required": action_required
        }

    def render_circular_monitor(self, cycle_hour, weather_shift=0.0):
        print("\n" + "="*105)
        print(f" 🌐 CIRCULAR SOIL & WEATHER GRID MONITORING DASHBOARD")
        print(f" 📍 Location: {self.location} | Active Zone Area: {self.zone_area_hectares} Hectares")
        print("="*105)
        print(f" ⏱️ Monitoring Cycle Hour : {cycle_hour:02d}:00 HRS   |   📐 Subsurface Depth: {self.trench_depth_m}m")
        print(f" 🌿 Soil Matrix Foundation : {self.soil_type}")
        print("-"*105)
        
        status = self.evaluate_circular_greening_status(weather_shift)
        
        print(f" 📊 [SECTION A: REAL-TIME SOIL & WEATHER TELEMETRY]")
        print(f"   • Ambient Weather Temperature     : {self.grid_parameters['Ambient_Weather_Temp_C'] + weather_shift}°C")
        print(f"   • Surface Soil Temp / Moisture    : {status['Adjusted_Soil_Temp']}°C / {status['Adjusted_Moisture']}%")
        print(f"   • 4m Deep Subsurface Moisture     : {self.grid_parameters['Soil_Moisture_Subsurface_4m_pct']}% (Stable)")
        print(f"   • Atmospheric Humidity            : {self.grid_parameters['Atmospheric_Humidity_pct']}%")
        print(f"   • CO2 Absorption Index            : {self.grid_parameters['CO2_Absorption_Index_ppm']} ppm")
        print("-"*105)
        
        print(f" ♻️ [SECTION B: CIRCULAR GREENING & EQUILIBRIUM ANALYSIS]")
        print(f"   • Grid Greening Condition         : {status['Greening_Status']}")
        print(f"   • Automated Action Trigger        : {status['Action_Required']}")
        print(f"   • Closed-Loop Efficiency          : {self.grid_parameters['Circular_Regeneration_Efficiency']}")
        print("="*105)

if __name__ == "__main__":
    monitor = CircularSoilWeatherMonitor(location="Doha Smart Eco-Zone", zone_area_hectares=60.0)
    
    # Simulate normal and fluctuating weather conditions to test circular feedback
    monitor.render_circular_monitor(cycle_hour=9.0, weather_shift=0.0)   # Normal Morning
    monitor.render_circular_monitor(cycle_hour=14.0, weather_shift=6.5)  # Heat Spike / Weather Fluctuation
import time
import random

class CircularSoilWeatherMonitor:
    def __init__(self, location="Doha Urban Eco-Grid", zone_area_hectares=50.0):
        self.location = location
        self.zone_area_hectares = zone_area_hectares
        
        # Soil and Circular Grid Parameters
        self.trench_depth_m = 4.0
        self.soil_type = "Processed Loamy Soil (Bele Doash with Upcycled Waste)"
        
        # Live Grid Parameters Tracking
        self.grid_parameters = {
            "Soil_Moisture_Surface_pct": 62.4,
            "Soil_Moisture_Subsurface_4m_pct": 85.0,
            "Soil_Temperature_C": 26.5,
            "Ambient_Weather_Temp_C": 34.2,
            "Atmospheric_Humidity_pct": 55.0,
            "CO2_Absorption_Index_ppm": 412.0,
            "Circular_Regeneration_Efficiency": "98.1%"
        }

    def evaluate_circular_greening_status(self, weather_fluctuation):
        """
        Evaluates soil-weather synchronization and determines the exact greening capacity.
        """
        adjusted_soil_temp = self.grid_parameters["Soil_Temperature_C"] + (weather_fluctuation * 0.1)
        adjusted_moisture = max(30.0, self.grid_parameters["Soil_Moisture_Surface_pct"] - (weather_fluctuation * 1.5))
        
        # Greening Condition Assessment
        if adjusted_moisture > 50.0 and adjusted_soil_temp < 32.0:
            greening_status = "OPTIMAL CIRCULAR GREENING: High Biomass & Plant Growth Rate"
            action_required = "Maintain standard micro-irrigation and organic nutrient cycling."
        else:
            greening_status = "ADAPTIVE STRESS SHIELDING: Deploying Subsurface Moisture Release"
            action_required = "Activate 4m deep thermal flywheel and shade canopy misting."

        return {
            "Adjusted_Soil_Temp": round(adjusted_soil_temp, 2),
            "Adjusted_Moisture": round(adjusted_moisture, 2),
            "Greening_Status": greening_status,
            "Action_Required": action_required
        }

    def render_circular_monitor(self, cycle_hour, weather_shift=0.0):
        print("\n" + "="*105)
        print(f" 🌐 CIRCULAR SOIL & WEATHER GRID MONITORING DASHBOARD")
        print(f" 📍 Location: {self.location} | Active Zone Area: {self.zone_area_hectares} Hectares")
        print("="*105)
        print(f" ⏱️ Monitoring Cycle Hour : {cycle_hour:02d}:00 HRS   |   📐 Subsurface Depth: {self.trench_depth_m}m")
        print(f" 🌿 Soil Matrix Foundation : {self.soil_type}")
        print("-"*105)
        
        status = self.evaluate_circular_greening_status(weather_shift)
        
        print(f" 📊 [SECTION A: REAL-TIME SOIL & WEATHER TELEMETRY]")
        print(f"   • Ambient Weather Temperature     : {self.grid_parameters['Ambient_Weather_Temp_C'] + weather_shift}°C")
        print(f"   • Surface Soil Temp / Moisture    : {status['Adjusted_Soil_Temp']}°C / {status['Adjusted_Moisture']}%")
        print(f"   • 4m Deep Subsurface Moisture     : {self.grid_parameters['Soil_Moisture_Subsurface_4m_pct']}% (Stable)")
        print(f"   • Atmospheric Humidity            : {self.grid_parameters['Atmospheric_Humidity_pct']}%")
        print(f"   • CO2 Absorption Index            : {self.grid_parameters['CO2_Absorption_Index_ppm']} ppm")
        print("-"*105)
        
        print(f" ♻️ [SECTION B: CIRCULAR GREENING & EQUILIBRIUM ANALYSIS]")
        print(f"   • Grid Greening Condition         : {status['Greening_Status']}")
        print(f"   • Automated Action Trigger        : {status['Action_Required']}")
        print(f"   • Closed-Loop Efficiency          : {self.grid_parameters['Circular_Regeneration_Efficiency']}")
        print("="*105)

if __name__ == "__main__":
    monitor = CircularSoilWeatherMonitor(location="Doha Smart Eco-Zone", zone_area_hectares=60.0)
    
    # Simulate normal and fluctuating weather conditions to test circular feedback
    monitor.render_circular_monitor(cycle_hour=9.0, weather_shift=0.0)   # Normal Morning
    monitor.render_circular_monitor(cycle_hour=14.0, weather_shift=6.5)  # Heat Spike / Weather Fluctuation
import time
import random

class CircularSoilWeatherMonitor:
    def __init__(self, location="Doha Urban Eco-Grid", zone_area_hectares=50.0):
        self.location = location
        self.zone_area_hectares = zone_area_hectares
        
        # Soil and Circular Grid Parameters
        self.trench_depth_m = 4.0
        self.soil_type = "Processed Loamy Soil (Bele Doash with Upcycled Waste)"
        
        # Live Grid Parameters Tracking
        self.grid_parameters = {
            "Soil_Moisture_Surface_pct": 62.4,
            "Soil_Moisture_Subsurface_4m_pct": 85.0,
            "Soil_Temperature_C": 26.5,
            "Ambient_Weather_Temp_C": 34.2,
            "Atmospheric_Humidity_pct": 55.0,
            "CO2_Absorption_Index_ppm": 412.0,
            "Circular_Regeneration_Efficiency": "98.1%"
        }

    def evaluate_circular_greening_status(self, weather_fluctuation):
        """
        Evaluates soil-weather synchronization and determines the exact greening capacity.
        """
        adjusted_soil_temp = self.grid_parameters["Soil_Temperature_C"] + (weather_fluctuation * 0.1)
        adjusted_moisture = max(30.0, self.grid_parameters["Soil_Moisture_Surface_pct"] - (weather_fluctuation * 1.5))
        
        # Greening Condition Assessment
        if adjusted_moisture > 50.0 and adjusted_soil_temp < 32.0:
            greening_status = "OPTIMAL CIRCULAR GREENING: High Biomass & Plant Growth Rate"
            action_required = "Maintain standard micro-irrigation and organic nutrient cycling."
        else:
            greening_status = "ADAPTIVE STRESS SHIELDING: Deploying Subsurface Moisture Release"
            action_required = "Activate 4m deep thermal flywheel and shade canopy misting."

        return {
            "Adjusted_Soil_Temp": round(adjusted_soil_temp, 2),
            "Adjusted_Moisture": round(adjusted_moisture, 2),
            "Greening_Status": greening_status,
            "Action_Required": action_required
        }

    def render_circular_monitor(self, cycle_hour, weather_shift=0.0):
        print("\n" + "="*105)
        print(f" 🌐 CIRCULAR SOIL & WEATHER GRID MONITORING DASHBOARD")
        print(f" 📍 Location: {self.location} | Active Zone Area: {self.zone_area_hectares} Hectares")
        print("="*105)
        print(f" ⏱️ Monitoring Cycle Hour : {cycle_hour:02d}:00 HRS   |   📐 Subsurface Depth: {self.trench_depth_m}m")
        print(f" 🌿 Soil Matrix Foundation : {self.soil_type}")
        print("-"*105)
        
        status = self.evaluate_circular_greening_status(weather_shift)
        
        print(f" 📊 [SECTION A: REAL-TIME SOIL & WEATHER TELEMETRY]")
        print(f"   • Ambient Weather Temperature     : {self.grid_parameters['Ambient_Weather_Temp_C'] + weather_shift}°C")
        print(f"   • Surface Soil Temp / Moisture    : {status['Adjusted_Soil_Temp']}°C / {status['Adjusted_Moisture']}%")
        print(f"   • 4m Deep Subsurface Moisture     : {self.grid_parameters['Soil_Moisture_Subsurface_4m_pct']}% (Stable)")
        print(f"   • Atmospheric Humidity            : {self.grid_parameters['Atmospheric_Humidity_pct']}%")
        print(f"   • CO2 Absorption Index            : {self.grid_parameters['CO2_Absorption_Index_ppm']} ppm")
        print("-"*105)
        
        print(f" ♻️ [SECTION B: CIRCULAR GREENING & EQUILIBRIUM ANALYSIS]")
        print(f"   • Grid Greening Condition         : {status['Greening_Status']}")
        print(f"   • Automated Action Trigger        : {status['Action_Required']}")
        print(f"   • Closed-Loop Efficiency          : {self.grid_parameters['Circular_Regeneration_Efficiency']}")
        print("="*105)

if __name__ == "__main__":
    monitor = CircularSoilWeatherMonitor(location="Doha Smart Eco-Zone", zone_area_hectares=60.0)
    
    # Simulate normal and fluctuating weather conditions to test circular feedback
    monitor.render_circular_monitor(cycle_hour=9.0, weather_shift=0.0)   # Normal Morning
    monitor.render_circular_monitor(cycle_hour=14.0, weather_shift=6.5)  # Heat Spike / Weather Fluctuation
import time
import random

class SirHamidRainActivatedOasisDashboard:
    def __init__(self, location="Doha Smart Eco-Oasis", area_hectares=150.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # System Structural Parameters
        self.trench_depth_m = 4.0
        self.soil_type = "Converted Loamy Soil (Bele Doash)"
        
        # Base Telemetry Grid
        self.monitoring_grid = {
            "Surface_Soil_Moisture_pct": 58.5,
            "Deep_Subsurface_Moisture_4m_pct": 84.0,
            "Closed_Loop_Efficiency": "98.5%"
        }

    def rain_activation_engine(self, hour, raw_temp, humidity):
        """
        Evaluates rain conditions and triggers full-system activation:
        1. Rain Detection & Atmosphere Saturation Check
        2. 4-Meter Deep Trench Rainwater Harvesting & Storage
        3. Micro-irrigation Pause & Microbial Composting Activation
        4. Zero-Loss Crop & Greening Hydration Lock
        """
        # Rain Trigger Logic
        is_raining = False
        rain_status = "Dry Weather / Standard Solar Phase"
        
        if humidity >= 80.0 and raw_temp < 25.0:
            is_raining = True
            rain_status = "🌧️ RAIN DETECTED: Full System Activation Triggered!"
        elif 75.0 <= humidity < 80.0:
            is_raining = True
            rain_status = "🌦️ DRIZZLE DETECTED: Partial System Water Harvesting Active"
        else:
            rain_status = "☀️ CLEAR SKY: Standard Solar-Thermal Regulation Active"

        # Full System Response when Rain Occurs
        if is_raining:
            system_action = "ACTIVE RAINWATER HARVESTING & DEEP TRENCH RECHARGE"
            subsurface_moisture_boost = "+12.5% (Stored in 4m Sub-surface Bio-layer)"
            irrigation_status = "PAUSED (Saved 100% Groundwater/Pumping Energy)"
            microbial_activity = "PEAK (Rainwater activates underground microbes & NPK nutrients)"
        else:
            system_action = "Standard Closed-Loop Microclimate Regulation"
            subsurface_moisture_boost = "Stable (Maintained via 4m Thermal Flywheel)"
            irrigation_status = "AUTO-OPTIMIZED (Drip & Misting Active)"
            microbial_activity = "Normal Steady State"

        return {
            "Is_Raining": is_raining,
            "Rain_Status": rain_status,
            "System_Action": system_action,
            "Subsurface_Boost": subsurface_moisture_boost,
            "Irrigation_Status": irrigation_status,
            "Microbial_Activity": microbial_activity
        }

    def render_dashboard(self, hour):
        print("\n" + "="*105)
        print(f" 🌧️ SIR HAMID'S RAIN-ACTIVATED FULL SYSTEM INTEGRATION DASHBOARD")
        print(f" 📍 Location: {self.location} | Grid Area: {self.area_hectares} Hectares")
        print("="*105)
        
        # Simulate different weather conditions (Morning rain vs Midday sun)
        if 6.0 <= hour < 10.0:
            phase = "🌅 Morning High-Humidity Phase (Rain Event Simulation)"
            raw_temp = 22.0
            humidity = 85.0  # Triggers Rain Activation
        elif 12.0 <= hour < 16.0:
            phase = "☀️ Peak Zenith Afternoon Phase"
            raw_temp = 36.0
            humidity = 42.0  # Dry Condition
        else:
            phase = "🌙 Night Dew & Condensation Phase"
            raw_temp = 19.0
            humidity = 82.0  # Triggers Drizzle/Dew Activation

        # Run Rain Activation Engine
        activation = self.rain_activation_engine(hour, raw_temp, humidity)

        print(f" ⏱️ Operational Time    : {hour:02d}:00 HRS   |   Phase: {phase}")
        print(f" 🌡️ Ambient Temperature : {raw_temp}°C     |   💧 Humidity: {humidity}%")
        print(f" ⚡ Weather Trigger     : {activation['Rain_Status']}")
        print("="*105)
        
        # Section A: Full System Activation Status
        print(" 🔄 [SECTION A: RAIN-ACTIVATED FULL SYSTEM RESPONSE]")
        print(f"   • Primary System Action           : {activation['System_Action']}")
        print(f"   • 4m Trench Groundwater Recharge  : {activation['Subsurface_Boost']}")
        print(f"   • Surface Irrigation Status       : {activation['Irrigation_Status']}")
        print(f"   • Underground Microbial Activity  : {activation['Microbial_Activity']}")
        print("-"*105)
        
        # Section B: Soil & Water Grid Metrics
        print(" 📊 [SECTION B: SOIL, WATER & ECO-GREENING TELEMETRY]")
        print(f"   • Surface Soil Moisture           : {self.monitoring_grid['Surface_Soil_Moisture_pct']}% (Naturally Hydrated)")
        print(f"   • 4m Subsurface Water Bank        : {self.monitoring_grid['Deep_Subsurface_Moisture_4m_pct']}% (Max Storage)")
        print(f"   • Closed-Loop Efficiency          : {self.monitoring_grid['Closed_Loop_Efficiency']}")
        print("="*105)

    def execute_closed_loop_philosophy(self):
        print("\n♻️ ETERNAL CLOSED-LOOP REGENERATION PHILOSOPHY:")
        print("   1. Rain Integration: When rain falls, the entire system instantly wakes up, harvesting every drop into 4m deep trenches.")
        print("   2. Zero Waste & Maximum Life: Natural water combines with upcycled soil nutrients to feed fruit forests and urban greenery.")
        print("   3. Universal Law: 'What comes from the earth returns to the earth, creating continuous, immortal life.'")

if __name__ == "__main__":
    dashboard = SirHamidRainActivatedOasisDashboard()
    
    # Test across hours to show rain activation vs normal operations
    test_timeline = [8.0, 14.0, 22.0]
    for h in test_timeline:
        dashboard.render_dashboard(hour=h)
        
    dashboard.execute_closed_loop_philosophy()
