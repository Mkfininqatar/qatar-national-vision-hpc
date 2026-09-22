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
