import time
import random

class EcoEngineeringSystem:
    def __init__(self, location="Doha Desert Oasis", area_hectares=5.0):
        self.location = location
        self.area_hectares = area_hectares
        
        # Soil & Stratigraphy (Step 1)
        self.trench_depth_m = 4.0  # 3-5 meters
        self.trench_base_m = 4.5   # 4-5 meters
        self.soil_type = "Sandy Desert -> Converted Loamy Soil (Bele Doash)"
        self.organic_layers = ["Human Waste Refuse", "Kitchen Organic Waste", "Animal Waste + Beneficial Microbes"]
        
        # Hydrology & Filtration (Step 2)
        self.seawater_channel_active = True
        self.rock_filtration_efficiency = 0.88 # 88% sodium/salt reduction via stone/baffle beds
        self.desalination_rate = "Solar Evaporation & Vapor Condensation"
        
        # Hardy Perimeter Shield Trees (Step 4)
        self.perimeter_trees = ["Date Palm", "Neem", "Jujube (Ber)", "Koroi", "Banyan"]
        
        # Central Agricultural Core Crops (Step 5)
        self.central_crops = ["Mango", "Jackfruit", "Banana", "Seasonal Vegetables (Tomato, Cucumber, Eggplant)"]

    def simulate_diurnal_cycle(self, hour, solar_radiation_kw_m2, wind_speed_ms):
        """
        Simulates the 24-hour Diurnal Solar-Thermal, Wind, and Condensation Loop.
        """
        print(f"\n--- [Telemetry & Eco-Simulation Time: {hour:02d}:00 HRS] ---")
        
        # Morning Pure Energy Phase (5:30 AM - 10:00 AM)
        if 5.5 <= hour < 10.0:
            print("🌅 Morning Golden Solar Phase (5:30 - 10:00):")
            print("   -> Pure photon energy active; stomata open for peak photosynthesis.")
            print("   -> Underground microbial activity awakened in the animal/kitchen waste layer.")
            microclimate_temp = 23.0 + (solar_radiation_kw_m2 * 2)
            humidity = 60.0
            
        # Peak Zenith Phase (11:00 AM - 3:00 PM)
        elif 11.0 <= hour <= 15.0:
            print("☀️ Peak Zenith Solar Phase (11:00 - 15:00):")
            print("   -> Maximum solar radiation overhead. High vaporization rate triggered.")
            print("   -> Seawater channels absorbing excess heat; rock filters purifying water.")
            if wind_speed_ms < 1.5:
                print("   ⚠️ WARNING: Low wind speed! Stagnant hot vapor detected. Activating micro-agitators.")
            microclimate_temp = 36.0 + (solar_radiation_kw_m2 * 4)  # Mitigated compared to 50°C raw desert
            humidity = 40.0
            
        # Cooling Transition Phase (3:00 PM - 6:00 PM)
        elif 15.0 < hour <= 18.0:
            print("🌤️ Cooling Transition Phase (15:00 - 18:00):")
            print("   -> Declining sun angle. Perimeter canopy trees transpiring moisture.")
            microclimate_temp = 29.0
            humidity = 55.0
            
        # Night Condensation & Dew Hydration Phase (Night Cycle)
        else:
            print("🌙 Night Condensation & Dew Hydration Loop:")
            print("   -> Floating water vapor condensing into dew/fog.")
            print("   -> Surface soil hydration active. Thermal blanket locking deep warmth.")
            microclimate_temp = 20.0
            humidity = 85.0
            
        return {"Temperature_C": round(microclimate_temp, 2), "Humidity_pct": humidity}

    def execute_closed_loop_cycle(self):
        """
        Executes the Eternal Closed-Loop Philosophy:
        Soil -> Plant -> Consumption -> Organic/Animal Waste -> Bacterial Composting -> Loamy Soil.
        """
        print("\n♻️ Executing Closed-Loop Organic Regeneration Cycle:")
        print(f"   1. Deep Stratum ({self.trench_depth_m}m depth): Composting animal & kitchen waste via bacteria.")
        print(f"   2. Soil Conversion: Sandy desert transformed into high-yield {self.soil_type}.")
        print("   3. Plant Growth: Perimeter shield trees & central crops absorb nutrients.")
        print("   4. Result: 'What comes from the earth returns to the earth, creating continuous life.'")

# ==========================================
# RUNNING THE MASTER SYSTEM SIMULATION
# ==========================================
if __name__ == "__main__":
    # Initialize our custom Desert Eco-Engineering System
    oasis_system = EcoEngineeringSystem(location="Doha Reclamation Zone", area_hectares=10.0)
    
    print(f"🌱 Initializing Master Blueprint for: {oasis_system.location}")
    print(f"📐 Trench Dimensions: {oasis_system.trench_depth_m}m Depth x {oasis_system.trench_base_m}m Base")
    print(f"🛡️ Perimeter Shields: {', '.join(oasis_system.perimeter_trees)}")
    print(f"🌾 Central Crops: {', '.join(oasis_system.central_crops)}")
    
    # Simulate different hours of the day to test telemetry & weather adjustments
    test_hours = [7.0, 13.0, 16.5, 23.0]
    
    for h in test_hours:
        solar_rad = 0.8 if 6 <= h <= 18 else 0.0
        wind = 0.8 if h == 13.0 else 3.5  # Simulate low wind at 1 PM to test vapor stagnation alert
        
        metrics = oasis_system.simulate_diurnal_cycle(hour=h, solar_radiation_kw_m2=solar_rad, wind_speed_ms=wind)
        print(f"   [Telemetry Metrics] Temp: {metrics['Temperature_C']}°C | Humidity: {metrics['Humidity_pct']}%")
        
    # Execute the biological closed loop
    oasis_system.execute_closed_loop_cycle()
