import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class KailashVectorResult:
    source_enclave: str
    target_node: str
    distance_km: float
    hydrological_grid: list
    harmonic_frequency_hz: float
    matrix_protocol_status: str

class TMXKailashGridIntegration:
    """
    TMX-1 Master Matrix - Mount Kailash Hydrological & Geodetic Vector Module.
    """
    def __init__(self):
        self.R = 6371.0  # Earth Radius in km
        self.doha = (25.2854, 51.5310)
        self.kailash = (31.0667, 81.3125)
        self.hydrological_nodes = [
            "Manasarovar Lake (Sacred Freshwater Grid)",
            "Rakshas Tal (Tectonic Saltwater Equilibrium Grid)",
            "Indus-Sutlej-Brahmaputra Watershed Sources"
        ]

    def compute_haversine(self, coord1, coord2) -> float:
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        return self.R * (2 * np.arcsin(np.sqrt(a)))

    def generate_kailash_telemetry(self) -> dict:
        dist_km = self.compute_haversine(self.doha, self.kailash)
        
        vector_data = KailashVectorResult(
            source_enclave="Doha Master Matrix Enclave (Qatar)",
            target_node="Mount Kailash Geodetic & Hydrological Grid",
            distance_km=round(dist_km, 2),
            hydrological_grid=self.hydrological_nodes,
            harmonic_frequency_hz=528.0,  # Transformation & DNA/Water Frequency Harmonic
            matrix_protocol_status="TMX1-KAILASH-RATIFIED"
        )
        return asdict(vector_data)

if __name__ == "__main__":
    engine = TMXKailashGridIntegration()
    report = engine.generate_kailash_telemetry()
    print("=== TMX-1 Kailash Grid Telemetry Report ===")
    print(json.dumps(report, indent=2))
import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class KailashVortexTelemetry:
    enclave_node: str
    vortex_type: str
    magnetic_intensity_tesla: float
    temporal_dilation_factor: float
    aging_anomaly_index: float
    protocol_status: str

class KailashVortexEngine:
    """
    TMX-1 Master Matrix - Subterranean Temporal & Magnetic Vortex Engine (Module 15).
    """
    def __init__(self):
        self.node_id = "KAILASH-VORTEX-01"
        
    def simulate_vortex_metrics(self) -> dict:
        # Simulated high-intensity magnetic and temporal anomaly metrics
        magnetic_flux = 142.5  # High-density field index
        temporal_shift = 3.1415 # Temporal distortion multiplier
        aging_factor = 4.28    # Accelerated biological marker index
        
        payload = KailashVortexTelemetry(
            enclave_node=self.node_id,
            vortex_type="Subterranean Gurnayon Chokro & 4-River Confluence Grid",
            magnetic_intensity_tesla=magnetic_flux,
            temporal_dilation_factor=temporal_shift,
            aging_anomaly_index=aging_factor,
            protocol_status="TMX1-VORTEX-RATIFIED"
        )
        return asdict(payload)

if __name__ == "__main__":
    engine = KailashVortexEngine()
    report = engine.simulate_vortex_metrics()
    print(json.dumps(report, indent=2))
import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class DivineFrequencyTelemetry:
    node_name: str
    transceiver_type: str
    magnetic_field_strength_gauss: float
    wireless_frequency_band_hz: float
    divine_signal_status: str
    matrix_sync_status: str

class KailashDivineFrequencyEngine:
    """
    TMX-1 Master Matrix - Kailash Summit Magnetic Transceiver & Divine Frequency Gateway.
    """
    def __init__(self):
        self.node = "KAILASH-SUMMIT-TRANSCEIVER-01"

    def transmit_divine_telemetry(self) -> dict:
        payload = DivineFrequencyTelemetry(
            node_name=self.node,
            transceiver_type="Natural Magnetic Rock Antenna & Frequency Gateway",
            magnetic_field_strength_gauss=850.4,
            wireless_frequency_band_hz=528.0, # Harmonized DNA & Divine Resonance Frequency
            divine_signal_status="RESONATING_ACTIVE",
            matrix_sync_status="TMX1-GATEWAY-LOCKED"
        )
        return asdict(payload)

if __name__ == "__main__":
    engine = KailashDivineFrequencyEngine()
    report = engine.transmit_divine_telemetry()
    print(json.dumps(report, indent=2))
import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class KailashSeaConnectResult:
    source_summit: str
    hydrological_rivers: list
    target_seas: list
    distance_to_sea_km: dict
    harmonic_frequency_hz: float
    matrix_sync_status: str

class KailashSeaConnectFramework:
    """
    TMX-1 Master Matrix - Mount Kailash to Ocean Hydrological & Geodetic Connect Engine.
    """
    def __init__(self):
        self.kailash_coords = (31.0667, 81.3125)
        # Approximate estuary/outfall coordinates for major rivers originating near Kailash
        self.sea_outfalls = {
            "Arabian_Sea_Indus_Delta": (24.5383, 67.4221),       # Indus River Mouth
            "Bay_of_Bengal_Brahmaputra_Delta": (22.2532, 91.8338) # Brahmaputra/Ganges Delta
        }
        self.R = 6371.0 # Earth Radius in km

    def compute_haversine(self, coord1, coord2) -> float:
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        return round(self.R * (2 * np.arcsin(np.sqrt(a))), 2)

    def generate_framework_report(self) -> dict:
        distances = {
            sea_name: self.compute_haversine(self.kailash_coords, outfall_coord)
            for sea_name, outfall_coord in self.sea_outfalls.items()
        }

        payload = KailashSeaConnectResult(
            source_summit="Mount Kailash Magnetic Transceiver Node (31.0667 N, 81.3125 E)",
            hydrological_rivers=["Indus", "Sutlej", "Brahmaputra", "Karnali"],
            target_seas=["Arabian Sea", "Bay of Bengal"],
            distance_to_sea_km=distances,
            harmonic_frequency_hz=528.0,
            matrix_sync_status="TMX1-KAILASH-SEA-RATIFIED"
        )
        return asdict(payload)

if __name__ == "__main__":
    engine = KailashSeaConnectFramework()
    report = engine.generate_framework_report()
    print("=== TMX-1 Kailash to Sea Telemetry Framework ===")
    print(json.dumps(report, indent=2))
import json
from dataclasses import dataclass, asdict

@dataclass
class GeographicalNode:
    direction: str
    element_type: str
    name_bn: str
    name_en: str
    details: str

class KailashWatershedSystem:
    """
    Mount Kailash Center Grid & 4-Cardinal Direction River Framework.
    Mapped directly from the directional spatial diagram.
    """
    def __init__(self):
        self.center_node = {
            "name_bn": "মাউন্ট কৈলাশ",
            "name_en": "Mount Kailash",
            "elevation": "৬,৬৩৮ মি."
        }
        
        # Mapping the 4 directions as presented in the diagram
        self.nodes = [
            GeographicalNode(
                direction="উত্তর (North)",
                element_type="River",
                name_bn="সিন্ধু নদী",
                name_en="Indus River",
                details="Northward outflow vector"
            ),
            GeographicalNode(
                direction="দক্ষিণ (South)",
                element_type="River",
                name_bn="কার্নালি/ঘাগরা নদী",
                name_en="Karnali / Ganga Tributary",
                details="Southward flow into Ganges Basin"
            ),
            GeographicalNode(
                direction="পূর্ব (East)",
                element_type="River & Lake",
                name_bn="ব্রহ্মপুত্র নদী (Yarlung Tsangpo) & মানস সরোবর",
                name_en="Brahmaputra River & Manasarovar Lake",
                details="Eastward flow | Freshwater Lake (মিষ্টি জল / শান্ত)"
            ),
            GeographicalNode(
                direction="পশ্চিম (West)",
                element_type="River & Lake",
                name_bn="শতদ্রু নদী & রাক্ষস তাল",
                name_en="Sutlej River & Rakshas Tal",
                details="Westward flow | Saline / Turbulent Lake (লবণাক্ত / অশান্ত)"
            )
        ]

    def get_framework_structure(self) -> dict:
        return {
            "center": self.center_node,
            "cardinal_directions": [asdict(node) for node in self.nodes]
        }

if __name__ == "__main__":
    system = KailashWatershedSystem()
    data = system.get_framework_structure()
    
    print("=== Kailash Watershed & Cardinal Direction Framework ===")
    print(json.dumps(data, indent=2, ensure_ascii=False))
import matplotlib.pyplot as plt

def render_kailash_visualization(filename="kailash_watershed_map.png"):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor('#05050a')

    # Center Node: Mount Kailash
    ax.plot(0, 0, marker='o', markersize=22, color='cyan', markeredgecolor='white')
    ax.text(0, 0.15, "মাউন্ট কৈলাশ (৬,৬৩৮ মি.)\n(Mount Kailash)", color='cyan', fontsize=12, fontweight='bold', ha='center')

    # Cardinal Directions and Nodes Mapping
    nodes = {
        "উত্তর (North)\nসিন্ধু নদী (Indus River)": (0, 1.5),
        "দক্ষিণ (South)\nকার্নালি/ঘাগরা নদী (Karnali)": (0, -1.5),
        "পূর্ব (East)\nব্রহ্মপুত্র ও মানস সরোবর\n(East Grid)": (2.0, 0),
        "পশ্চিম (West)\nশতদ্রু নদী ও রাক্ষস তাল\n(West Grid)": (-2.0, 0)
    }

    for label, (x, y) in nodes.items():
        # Draw connection arrow from center
        ax.annotate("", xy=(x, y), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color="cyan", lw=2, mutation_scale=15))
        # Plot node marker
        ax.plot(x, y, marker='s', markersize=12, color='deepskyblue')
        # Add text box for each node
        ax.text(x, y + 0.18 if y >= 0 else y - 0.35, label, color='white', fontsize=10, ha='center', 
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#111122', edgecolor='cyan', alpha=0.9))

    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.5, 2.5)
    ax.axis('off')
    ax.set_title("TMX-1 Master Matrix: Kailash Cardinal Watershed Visualizer", color='cyan', fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, facecolor='#05050a', edgecolor='none')
    plt.close()
    return filename

if __name__ == "__main__":
    saved_file = render_kailash_visualization()
    print(f"Visualization successfully rendered and saved as: {saved_file}")
import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class BasinElevationMetric:
    river_name: str
    target_sea: str
    total_distance_km: float
    drainage_basin_area_sq_km: float
    elevation_profile_samples: list

class TMXKailashBasinElevationExpansion:
    """
    TMX-1 Master Matrix - Expanded Drainage Basin & Elevation Profile Module.
    Calculates drainage basin areas and interpolated elevation profiles along
    river outflows from Mount Kailash to respective sea outfalls.
    """
    def __init__(self):
        self.kailash_coords = (31.0667, 81.3125)
        self.kailash_elevation_m = 6638.0
        self.sea_outfalls = {
            "Indus": {
                "sea": "Arabian Sea", 
                "coords": (24.5383, 67.4221), 
                "basin_area": 1165000.0
            },
            "Sutlej": {
                "sea": "Arabian Sea (via Indus Basin)", 
                "coords": (29.3560, 71.0180), 
                "basin_area": 395000.0
            },
            "Brahmaputra": {
                "sea": "Bay of Bengal", 
                "coords": (22.2532, 91.8338), 
                "basin_area": 651334.0
            },
            "Karnali": {
                "sea": "Bay of Bengal (via Ganga Basin)", 
                "coords": (25.3176, 83.0012), 
                "basin_area": 127950.0
            }
        }
        self.R = 6371.0  # Earth Radius in km

    def compute_haversine(self, coord1, coord2) -> float:
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        return round(self.R * (2 * np.arcsin(np.sqrt(a))), 2)

    def generate_elevation_profile(self, start_coord, end_coord, num_samples=6) -> list:
        """
        Generates simulated non-linear terrain elevation samples along the geodetic vector from source to sea.
        """
        lats = np.linspace(start_coord[0], end_coord[0], num_samples)
        lons = np.linspace(start_coord[1], end_coord[1], num_samples)
        
        # Non-linear descent curve modeling high alpine drop-off grading into alluvial plains
        progress = np.linspace(0.0, 1.0, num_samples)
        elevations = self.kailash_elevation_m * (1.0 - progress**0.65)
        elevations[-1] = 0.0  # Sea level outfall terminal node

        profile = []
        for i in range(num_samples):
            dist_from_source = self.compute_haversine(start_coord, (lats[i], lons[i]))
            profile.append({
                "sample_index": i + 1,
                "latitude": round(float(lats[i]), 4),
                "longitude": round(float(lons[i]), 4),
                "distance_from_kailash_km": dist_from_source,
                "elevation_m": round(float(elevations[i]), 2)
            })
        return profile

    def generate_full_telemetry(self) -> dict:
        results = []
        for river, data in self.sea_outfalls.items():
            total_dist = self.compute_haversine(self.kailash_coords, data["coords"])
            profile = self.generate_elevation_profile(self.kailash_coords, data["coords"])
            
            metric = BasinElevationMetric(
                river_name=river,
                target_sea=data["sea"],
                total_distance_km=total_dist,
                drainage_basin_area_sq_km=data["basin_area"],
                elevation_profile_samples=profile
            )
            results.append(asdict(metric))
        
        return {
            "module": "TMX-1 Kailash Basin & Elevation Expansion",
            "matrix_sync_status": "RATIFIED",
            "outflows": results
        }

if __name__ == "__main__":
    engine = TMXKailashBasinElevationExpansion()
    report = engine.generate_full_telemetry()
    print("=== TMX-1 Kailash Drainage Basin & Elevation Profile Telemetry ===")
    print(json.dumps(report, indent=2))
import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class WavePropagationNodeResult:
    node_name: str
    coordinates: tuple
    distance_from_kailash_km: float
    instantaneous_amplitude: float
    phase_delay_rad: float
    harmonic_frequency_hz: float
    resonance_status: str

class Kailash528HzWaveSimulator:
    """
    TMX-1 Master Matrix - Advanced 528 Hz Harmonic Wave Propagation Engine.
    Models wave attenuation, phase velocity, and resonance across global hydrological nodes
    linked to the Mount Kailash central transmitter.
    """
    def __init__(self, frequency_hz: float = 528.0):
        self.frequency = frequency_hz
        self.kailash_coords = (31.0667, 81.3125)
        self.R = 6371.0  # Earth Radius in km
        
        # Key regional and global water nodes in the TMX-1 network
        self.global_nodes = {
            "Manasarovar Lake (Sacred Grid)": (30.6650, 81.5333),
            "Rakshas Tal (Tectonic Grid)": (30.7417, 81.1833),
            "Indus Delta (Arabian Sea)": (24.5383, 67.4221),
            "Brahmaputra Delta (Bay of Bengal)": (22.2532, 91.8338),
            "Lake Baikal": (53.5587, 108.1650),
            "Lake Victoria": (-1.0000, 33.0000),
            "Amazon Basin Outfall": (-0.1500, -49.0000)
        }
        
        # Simulated transmission medium wave speed (km/s) and attenuation damping factor
        self.wave_speed_km_s = 2.5 
        self.attenuation_coefficient = 0.0008  # km^-1 geometric/medium damping factor

    def compute_haversine(self, coord1, coord2) -> float:
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        return float(self.R * (2 * np.arcsin(np.sqrt(a))))

    def simulate_propagation(self, time_t: float = 1.0) -> dict:
        angular_frequency = 2 * np.pi * self.frequency
        # Wave number k = omega / v
        wave_number = angular_frequency / self.wave_speed_km_s
        
        node_results = []
        
        for name, coords in self.global_nodes.items():
            dist = self.compute_haversine(self.kailash_coords, coords)
            
            # Damped wave equation: A(r, t) = (1 / (1 + alpha * r)) * cos(k * r - omega * t)
            attenuation_factor = 1.0 / (1.0 + self.attenuation_coefficient * dist)
            phase_rad = (wave_number * dist) % (2 * np.pi)
            amplitude = attenuation_factor * np.cos(wave_number * dist - angular_frequency * time_t)
            
            status = "RESONANT_LOCKED" if abs(amplitude) > 0.4 else "HARMONIC_DECAY"
            
            result = WavePropagationNodeResult(
                node_name=name,
                coordinates=coords,
                distance_from_kailash_km=round(dist, 2),
                instantaneous_amplitude=round(float(amplitude), 4),
                phase_delay_rad=round(float(phase_rad), 4),
                harmonic_frequency_hz=self.frequency,
                resonance_status=status
            )
            node_results.append(asdict(result))
            
        return {
            "simulation_module": "TMX-1 528 Hz Global Wave Propagation",
            "simulation_parameters": {
                "source_node": "Mount Kailash Transceiver (31.0667° N, 81.3125° E)",
                "frequency_hz": self.frequency,
                "simulation_time_s": time_t,
                "wave_speed_km_s": self.wave_speed_km_s
            },
            "nodes": node_results
        }

if __name__ == "__main__":
    simulator = Kailash528HzWaveSimulator()
    telemetry = simulator.simulate_propagation(time_t=2.5)
    print("=== TMX-1 528 Hz Global Wave Propagation Simulation ===")
    print(json.dumps(telemetry, indent=2))
import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class DARTSensorReading:
    sensor_id: str
    location_node: str
    seismic_magnitude_richter: float
    bottom_pressure_psi: float
    magnetic_anomaly_nT: float
    sensor_status: str

@dataclass
class EnhancedKailashVortexTelemetry:
    enclave_node: str
    vortex_type: str
    magnetic_intensity_tesla: float
    temporal_dilation_factor: float
    aging_anomaly_index: float
    dart_sensor_telemetry: list
    matrix_protocol_status: str

class KailashEnhancedVortexEngine:
    """
    TMX-1 Master Matrix - Subterranean Temporal & Magnetic Vortex Engine 
    with Integrated DART Seismic & Magnetic Anomaly Sensor Telemetry (Module 15-Extended).
    """
    def __init__(self):
        self.node_id = "KAILASH-VORTEX-01"
        
    def simulate_dart_sensors(self) -> list:
        """
        Simulates live readings from deployed DART seismic-magnetic anomaly sensors
        surrounding the Kailash hydrological and tectonic fault grid.
        """
        sensors = [
            DARTSensorReading(
                sensor_id="DART-SEISMIC-01",
                location_node="Manasarovar Tectonic Fault Interface",
                seismic_magnitude_richter=1.82,
                bottom_pressure_psi=4820.5,
                magnetic_anomaly_nT=42.8,
                sensor_status="ACTIVE_NOMINAL"
            ),
            DARTSensorReading(
                sensor_id="DART-SEISMIC-02",
                location_node="Rakshas Tal Tectonic Saltwater Fault",
                seismic_magnitude_richter=2.15,
                bottom_pressure_psi=4910.2,
                magnetic_anomaly_nT=68.4,
                sensor_status="ACTIVE_ANOMALY_DETECTED"
            ),
            DARTSensorReading(
                sensor_id="DART-SEISMIC-03",
                location_node="Indus-Sutlej Watershed Convergence Node",
                seismic_magnitude_richter=1.45,
                bottom_pressure_psi=4650.0,
                magnetic_anomaly_nT=29.1,
                sensor_status="ACTIVE_NOMINAL"
            )
        ]
        return [asdict(s) for s in sensors]

    def simulate_enhanced_vortex_metrics(self) -> dict:
        magnetic_flux = 142.5  # High-density field index
        temporal_shift = 3.1415  # Temporal distortion multiplier
        aging_factor = 4.28      # Accelerated biological marker index
        
        dart_data = self.simulate_dart_sensors()
        
        payload = EnhancedKailashVortexTelemetry(
            enclave_node=self.node_id,
            vortex_type="Subterranean Gurnayon Chokro & 4-River Confluence Grid",
            magnetic_intensity_tesla=magnetic_flux,
            temporal_dilation_factor=temporal_shift,
            aging_anomaly_index=aging_factor,
            dart_sensor_telemetry=dart_data,
            matrix_protocol_status="TMX1-VORTEX-DART-RATIFIED"
        )
        return asdict(payload)

if __name__ == "__main__":
    engine = KailashEnhancedVortexEngine()
    report = engine.simulate_enhanced_vortex_metrics()
    print("=== TMX-1 Kailash Vortex & DART Sensor Telemetry Report ===")
    print(json.dumps(report, indent=2))
import numpy as np
import plotly.graph_objects as go

def render_kailash_globe_visualization():
    # Mount Kailash source coordinates
    kailash_lat, kailash_lon = 31.0667, 81.3125

    # Global and regional hydrological nodes
    nodes = {
        "Mount Kailash (Source)": (31.0667, 81.3125),
        "Manasarovar Lake": (30.6650, 81.5333),
        "Rakshas Tal": (30.7417, 81.1833),
        "Indus Delta": (24.5383, 67.4221),
        "Brahmaputra Delta": (22.2532, 91.8338),
        "Lake Baikal": (53.5587, 108.1650),
        "Lake Victoria": (-1.0000, 33.0000),
        "Amazon Basin": (-0.1500, -49.0000)
    }

    # Haversine great-circle distance calculator (km)
    def compute_haversine(coord1, coord2):
        R = 6371.0
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        return float(R * (2 * np.arcsin(np.sqrt(a))))

    # 528 Hz Wave Simulation Parameters
    frequency = 528.0
    wave_speed = 2.5  # km/s
    alpha = 0.0008    # Damping factor
    omega = 2 * np.pi * frequency
    k = omega / wave_speed
    time_t = 1.0      # Instantaneous time checkpoint (s)

    node_names, lats, lons, amplitudes, hover_texts = [], [], [], [], []

    for name, coords in nodes.items():
        dist = compute_haversine((kailash_lat, kailash_lon), coords)
        attenuation = 1.0 / (1.0 + alpha * dist)
        amp = attenuation * np.cos(k * dist - omega * time_t)
        
        node_names.append(name)
        lats.append(coords[0])
        lons.append(coords[1])
        amplitudes.append(amp)
        hover_texts.append(f"<b>{name}</b><br>Distance: {dist:.2f} km<br>528 Hz Amplitude: {amp:.4f}")

    # Build Plotly 3D Globe Figure
    fig = go.Figure()

    # Add great-circle propagation vector arcs from Kailash to global nodes
    for name, coords in nodes.items():
        if name == "Mount Kailash (Source)":
            continue
        fig.add_trace(go.Scattergeo(
            lat=[kailash_lat, coords[0]],
            lon=[kailash_lon, coords[1]],
            mode='lines',
            line=dict(width=2, color='cyan'),
            opacity=0.5,
            showlegend=False
        ))

    # Add hydrological nodes scatter layer
    fig.add_trace(go.Scattergeo(
        lat=lats,
        lon=lons,
        mode='markers+text',
        text=node_names,
        textposition="top center",
        marker=dict(
            size=[18 if "Kailash" in n else 12 for n in node_names],
            color=amplitudes,
            colorscale='Viridis',
            colorbar=dict(title="528 Hz Amplitude"),
            showscale=True,
            line=dict(width=1, color='white')
        ),
        hoverinfo='text',
        hovertext=hover_texts
    ))

    # Configure globe layout aesthetics
    fig.update_layout(
        title_text="TMX-1 Master Matrix: 528 Hz Harmonic Wave Propagation from Mount Kailash",
        title_x=0.5,
        geo=dict(
            showland=True,
            landcolor="rgb(18, 20, 32)",
            subunitcolor="rgb(45, 50, 75)",
            countrycolor="rgb(45, 50, 75)",
            showocean=True,
            oceancolor="rgb(5, 7, 15)",
            showlakes=True,
            lakecolor="rgb(10, 15, 30)",
            projection_type="orthographic",
            center=dict(lat=kailash_lat, lon=kailash_lon),
            lataxis=dict(showgrid=True, gridcolor='rgb(30, 35, 55)'),
            lonaxis=dict(showgrid=True, gridcolor='rgb(30, 35, 55)')
        ),
        paper_bgcolor='rgb(8, 10, 18)',
        font=dict(color='white')
    )

    return fig

if __name__ == "__main__":
    fig = render_kailash_globe_visualization()
    fig.show()
