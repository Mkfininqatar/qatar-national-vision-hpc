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
