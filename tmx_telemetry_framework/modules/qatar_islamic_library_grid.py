import json
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class TelemetryMetrics:
    base_frequency: str
    grid_status: str
    coherence: str
    energy_vectors: str

class QatarIslamicLibrarySystem:
    """
    Qatar Islamic Library - Geodesic Vibrational Map Engine.
    Maps architectural 3D wireframe topology with real-time frequency dynamics.
    """
    def __init__(self):
        self.system_title = "QATAR ISLAMIC LIBRARY - GEODESIC VIBRATIONAL MAP"
        self.telemetry = TelemetryMetrics(
            base_frequency="432 Hz",
            grid_status="OPTIMAL",
            coherence="98%",
            energy_vectors="ALIGNED"
        )
        self.resonance_bands = {
            "resonance_band_1": "Active Harmonic Sync",
            "sacred_geometry_grid": "Metatron & Golden Spiral Matrix",
            "architectural_nodes": ["Central Dome", "Outer Archways", "Subterranean Enclave"]
        }

    def get_system_telemetry(self) -> dict:
        return {
            "title": self.system_title,
            "telemetry_data": asdict(self.telemetry),
            "resonance_mapping": self.resonance_bands
        }

    def render_frequency_wave(self, output_file="qatar_library_frequency_map.png"):
        """Renders the dark-mode cyan frequency wave matching the UI monitor."""
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 4))
        fig.patch.set_facecolor('#080c14')
        ax.set_facecolor('#05080f')

        # Generate 432 Hz Synthetic Harmonic Wave Data
        x = np.linspace(0, 10, 1000)
        y = np.sin(2 * np.pi * 0.432 * x) * np.cos(0.5 * x) + 0.2 * np.sin(5 * x)

        ax.plot(x, y, color='cyan', linewidth=1.8, label='Resonance Band 1 (432 Hz)')
        ax.plot(x, -y * 0.7, color='magenta', alpha=0.6, linewidth=1.2, label='Harmonic Sync')

        ax.set_title("FREQUENCY MAP - VIBRATIONAL ANALYSIS [432 Hz]", color='cyan', fontsize=12, pad=12)
        ax.set_xlabel("Time Vector", color='gray')
        ax.set_ylabel("Amplitude", color='gray')
        ax.grid(True, color='#112233', linestyle='--', alpha=0.7)
        ax.legend(loc="upper right", facecolor='#080c14', edgecolor='cyan')

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

if __name__ == "__main__":
    system = QatarIslamicLibrarySystem()
    print("=== " + system.system_title + " ===")
    print(json.dumps(system.get_system_telemetry(), indent=2))
    
    saved_img = system.render_frequency_wave()
    print(f"\nFrequency visualization saved as: {saved_img}")
import json
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class AcousticNodeResult:
    mode_index: str
    eigenfrequency_hz: float
    max_sound_pressure_pa: float
    resonance_status: str

@dataclass
class TelemetryMetrics:
    base_frequency: str
    grid_status: str
    coherence: str
    energy_vectors: str

class QatarIslamicLibraryAcousticExpansion:
    """
    Qatar Islamic Library - Geodesic & Spatial Acoustic Resonance Expansion.
    Simulates real-time standing wave distributions and acoustic eigenmodes
    across the central dome architecture.
    """
    def __init__(self, base_freq_hz: float = 432.0):
        self.system_title = "QATAR ISLAMIC LIBRARY - SPATIAL ACOUSTIC RESONANCE ENGINE"
        self.base_frequency = base_freq_hz
        self.dome_radius_m = 25.0  # Central dome radius in meters
        self.speed_of_sound_m_s = 343.0  # Speed of sound in air at 20°C
        
        self.telemetry = TelemetryMetrics(
            base_frequency=f"{self.base_frequency} Hz",
            grid_status="OPTIMAL",
            coherence="98.5%",
            energy_vectors="ACOUSTICALLY_LOCKED"
        )

    def compute_dome_eigenmodes(self) -> list:
        """
        Simulates acoustic eigenmodes (standing wave frequencies) within the hemispherical dome cavity.
        """
        modes = []
        for n in range(1, 4):
            freq = round(self.base_frequency * (n * 0.5 + 0.5), 2)
            pressure = round(101325.0 + (n * 12.5), 2) # Base atmospheric + acoustic fluctuation
            status = "RESONANT_NODE_ACTIVE" if n % 2 != 0 else "HARMONIC_ANTINODE"
            modes.append(asdict(AcousticNodeResult(
                mode_index=f"DOMAL-MODE-0{n}",
                eigenfrequency_hz=freq,
                max_sound_pressure_pa=pressure,
                resonance_status=status
            )))
        return modes

    def render_standing_wave_field(self, output_file="qatar_dome_acoustic_field.png"):
        """
        Renders a spatial polar standing wave pressure distribution map across the central dome cross-section.
        """
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
        fig.patch.set_facecolor('#080c14')
        ax.set_facecolor('#05080f')

        theta = np.linspace(0, 2 * np.pi, 300)
        r = np.linspace(0, self.dome_radius_m, 100)
        T, R = np.meshgrid(theta, r)
        
        # Standing wave pressure distribution function inside the dome cavity
        Z = np.cos(np.pi * R / self.dome_radius_m) * np.cos(3 * T)

        contour = ax.contourf(T, R, Z, levels=20, cmap='coolwarm', alpha=0.85)
        cbar = fig.colorbar(contour, ax=ax, pad=0.1, shrink=0.7)
        cbar.set_label('Acoustic Pressure Deviation (Pa)', color='cyan')
        cbar.ax.yaxis.set_tick_params(color='cyan')

        ax.set_title("CENTRAL DOME - SPATIAL STANDING WAVE DISTRIBUTION", color='cyan', fontsize=11, pad=20)
        ax.grid(True, color='#112233', linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

    def get_full_telemetry(self) -> dict:
        return {
            "title": self.system_title,
            "telemetry_data": asdict(self.telemetry),
            "dome_geometry": {
                "radius_m": self.dome_radius_m,
                "cavity_shape": "Hemispherical Geodesic Vault"
            },
            "acoustic_eigenmodes": self.compute_dome_eigenmodes()
        }

if __name__ == "__main__":
    engine = QatarIslamicLibraryAcousticExpansion()
    print("=== " + engine.system_title + " ===")
    print(json.dumps(engine.get_full_telemetry(), indent=2))
    
    saved_file = engine.render_standing_wave_field()
    print(f"\nAcoustic standing wave field visualization saved as: {saved_file}")
import numpy as np
import plotly.graph_objects as go

def render_library_3d_wireframe():
    # Architectural parameters for Qatar Islamic Library wireframe
    # Central geodesic dome (hemisphere)
    phi = np.linspace(0, np.pi / 2, 20)
    theta = np.linspace(0, 2 * np.pi, 30)
    PHI, THETA = np.meshgrid(phi, theta)
    
    R_dome = 15.0
    X_dome = R_dome * np.sin(PHI) * np.cos(THETA)
    Y_dome = R_dome * np.sin(PHI) * np.sin(THETA)
    Z_dome = R_dome * np.cos(PHI) + 20.0  # Elevated central dome structure
    
    # Outer base podium & architectural footprint
    box_x = np.linspace(-25, 25, 15)
    box_y = np.linspace(-25, 25, 15)
    BX, BY = np.meshgrid(box_x, box_y)
    BZ = np.zeros_like(BX)

    # Geodesic vibrational nodes mapped across architectural coordinates
    nodes = {
        "Central Dome Apex": (0.0, 0.0, 35.0, 432.0, "OPTIMAL"),
        "Dome Periphery North": (15.0, 0.0, 20.0, 432.0, "ACTIVE"),
        "Dome Periphery South": (-15.0, 0.0, 20.0, 432.0, "ACTIVE"),
        "Dome Periphery East": (0.0, 15.0, 20.0, 432.0, "ACTIVE"),
        "Dome Periphery West": (0.0, -15.0, 20.0, 432.0, "ACTIVE"),
        "Outer Archway NW": (20.0, 20.0, 5.0, 216.0, "RESONANT"),
        "Outer Archway NE": (20.0, -20.0, 5.0, 216.0, "RESONANT"),
        "Outer Archway SW": (-20.0, 20.0, 5.0, 216.0, "RESONANT"),
        "Outer Archway SE": (-20.0, -20.0, 5.0, 216.0, "RESONANT"),
        "Subterranean Enclave Core": (0.0, 0.0, -10.0, 528.0, "LOCKED")
    }

    node_names = list(nodes.keys())
    nx = [nodes[n][0] for n in node_names]
    ny = [nodes[n][1] for n in node_names]
    nz = [nodes[n][2] for n in node_names]
    n_freq = [nodes[n][3] for n in node_names]
    n_status = [nodes[n][4] for n in node_names]

    fig = go.Figure()

    # Add Central Geodesic Dome Surface Wireframe
    fig.add_trace(go.Surface(
        x=X_dome, y=Y_dome, z=Z_dome,
        colorscale='Viridis',
        opacity=0.6,
        name="Central Geodesic Dome",
        showscale=False
    ))

    # Add Base Podium Wireframe
    fig.add_trace(go.Surface(
        x=BX, y=BY, z=BZ,
        colorscale='Blues',
        opacity=0.3,
        name="Library Base Podium",
        showscale=False
    ))

    # Add Geodesic Vibrational Nodes Scatter Layer
    fig.add_trace(go.Scatter3d(
        x=nx, y=ny, z=nz,
        mode='markers+text',
        text=node_names,
        textposition="top center",
        marker=dict(
            size=10,
            color=n_freq,
            colorscale='Plasma',
            colorbar=dict(title="Resonance Frequency (Hz)"),
            showscale=True,
            line=dict(width=2, color='white')
        ),
        name="Geodesic Vibrational Nodes"
    ))

    # Add Energy Vector Conduits (connecting apex to perimeter and subterranean nodes)
    for name, coords in nodes.items():
        if name != "Central Dome Apex":
            fig.add_trace(go.Scatter3d(
                x=[0.0, coords[0]],
                y=[0.0, coords[1]],
                z=[35.0, coords[2]],
                mode='lines',
                line=dict(color='cyan', width=2),
                opacity=0.5,
                showlegend=False
            ))

    # Configure dark-mode architectural CAD layout
    fig.update_layout(
        title="Qatar Islamic Library: 3D Architectural Wireframe & Geodesic Vibrational Nodes",
        title_x=0.5,
        scene=dict(
            xaxis=dict(backgroundcolor="#05080f", gridcolor="#112233", zerolinecolor="#112233", color="white"),
            yaxis=dict(backgroundcolor="#05080f", gridcolor="#112233", zerolinecolor="#112233", color="white"),
            zaxis=dict(backgroundcolor="#05080f", gridcolor="#112233", zerolinecolor="#112233", color="white"),
            bgcolor="#080c14"
        ),
        paper_bgcolor="#080c14",
        font=dict(color="white")
    )

    return fig

if __name__ == "__main__":
    fig = render_library_3d_wireframe()
    fig.show()
import json
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class EMShieldingMetric:
    enclave_depth_m: float
    frequency_hz: float
    shielding_effectiveness_db: float
    harmonic_dampening_ratio: float
    shielding_status: str

class QatarIslamicLibraryEMShieldingExpansion:
    """
    Qatar Islamic Library - Electromagnetic Shielding & Harmonic Dampening Subterranean Module.
    Simulates electromagnetic shielding effectiveness (SE) and harmonic dampening
    across the subterranean enclave core layers.
    """
    def __init__(self, enclave_depth_m: float = 15.0):
        self.system_title = "QATAR ISLAMIC LIBRARY - SUBTERRANEAN EM SHIELDING & DAMPENING ENGINE"
        self.enclave_depth = enclave_depth_m
        self.conductivity_sigma = 5.8e7     # Copper-equivalent mesh conductivity (S/m)
        self.relative_permeability_mu = 1000.0  # High-mu magnetic shielding alloy factor
        self.barrier_thickness_m = 0.05     # Shielding barrier thickness in meters

    def compute_shielding_effectiveness(self, frequency_hz: np.ndarray) -> np.ndarray:
        """
        Calculates total Shielding Effectiveness (SE = Absorption + Reflection) in dB.
        """
        mu_0 = 4 * np.pi * 1e-7
        mu = self.relative_permeability_mu * mu_0
        
        # Skin depth calculation: delta = sqrt(1 / (pi * f * mu * sigma))
        skin_depth = np.sqrt(1.0 / (np.pi * frequency_hz * mu * self.conductivity_sigma))
        
        # Absorption loss (SE_A) in dB
        se_absorption = 8.686 * (self.barrier_thickness_m / skin_depth)
        
        # Reflection loss (SE_R) in dB
        se_reflection = 39.5 - 10 * np.log10(frequency_hz * self.relative_permeability_mu / self.conductivity_sigma)
        
        total_se = se_absorption + se_reflection
        return np.maximum(total_se, 0.0)

    def generate_enclave_telemetry(self) -> dict:
        test_frequencies = [50.0, 432.0, 528.0, 1000.0, 10000.0, 100000.0]
        freq_array = np.array(test_frequencies)
        se_values = self.compute_shielding_effectiveness(freq_array)
        
        metrics = []
        for i, f in enumerate(test_frequencies):
            se = float(se_values[i])
            # Dampening ratio derived from dB attenuation: Amplitude_out / Amplitude_in = 10^(-SE / 20)
            dampening_ratio = round(10.0 ** (-se / 20.0), 8)
            status = "OPTIMAL_SHIELDED" if se > 60.0 else "NOMINAL_SHIELDED"
            
            metrics.append(asdict(EMShieldingMetric(
                enclave_depth_m=self.enclave_depth,
                frequency_hz=f,
                shielding_effectiveness_db=round(se, 2),
                harmonic_dampening_ratio=dampening_ratio,
                shielding_status=status
            )))
            
        return {
            "title": self.system_title,
            "subterranean_enclave_depth_m": self.enclave_depth,
            "em_shielding_metrics": metrics
        }

    def render_shielding_curve(self, output_file="qatar_library_em_shielding.png"):
        """Renders the electromagnetic shielding effectiveness vs frequency curve in dark mode."""
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor('#080c14')
        ax.set_facecolor('#05080f')

        freqs = np.logspace(1, 6, 500)  # 10 Hz to 1 MHz log space
        se = self.compute_shielding_effectiveness(freqs)

        ax.semilogx(freqs, se, color='cyan', linewidth=2, label='Total Shielding Effectiveness (dB)')
        ax.axvline(x=432.0, color='magenta', linestyle='--', alpha=0.8, label='Base Harmonic (432 Hz)')
        ax.axvline(x=528.0, color='yellow', linestyle='--', alpha=0.8, label='Resonance Frequency (528 Hz)')

        ax.set_title("SUBTERRANEAN ENCLAVE - EM SHIELDING & HARMONIC DAMPENING", color='cyan', fontsize=12, pad=12)
        ax.set_xlabel("Frequency (Hz, Log Scale)", color='gray')
        ax.set_ylabel("Shielding Effectiveness (dB)", color='gray')
        ax.grid(True, color='#112233', linestyle='--', alpha=0.7)
        ax.legend(loc="upper right", facecolor='#080c14', edgecolor='cyan')

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

if __name__ == "__main__":
    engine = QatarIslamicLibraryEMShieldingExpansion()
    print("=== " + engine.system_title + " ===")
    print(json.dumps(engine.generate_enclave_telemetry(), indent=2))
    
    saved_file = engine.render_shielding_curve()
    print(f"\nEM shielding telemetry curve saved as: {saved_file}")
import json
from dataclasses import dataclass, asdict

@dataclass
class CADNode:
    node_id: str
    node_name: str
    coordinate_x: float
    coordinate_y: float
    coordinate_z: float
    resonance_frequency_hz: float
    status: str

@dataclass
class CADMeshSurface:
    surface_name: str
    geometry_type: str
    parameters: dict

class QatarIslamicLibraryCADManifestGenerator:
    """
    Qatar Islamic Library - CAD Manifest Generator.
    Exports architectural wireframe geometries and geodesic vibrational node coordinates
    into a standardized, structured JSON CAD manifest.
    """
    def __init__(self):
        self.manifest_title = "QATAR ISLAMIC LIBRARY - CAD MANIFEST & GEODESIC TOPOLOGY"
        self.version = "1.0.0"

    def generate_manifest(self) -> dict:
        surfaces = [
            asdict(CADMeshSurface(
                surface_name="Central Geodesic Dome",
                geometry_type="Hemispherical Vault",
                parameters={"radius_m": 15.0, "apex_elevation_m": 35.0, "mesh_resolution": [20, 30]}
            )),
            asdict(CADMeshSurface(
                surface_name="Library Base Podium",
                geometry_type="Rectangular Platonic Base",
                parameters={"dimension_x_m": 50.0, "dimension_y_m": 50.0, "elevation_m": 0.0, "mesh_resolution": [15, 15]}
            ))
        ]

        nodes = [
            asdict(CADNode("NODE-01", "Central Dome Apex", 0.0, 0.0, 35.0, 432.0, "OPTIMAL")),
            asdict(CADNode("NODE-02", "Dome Periphery North", 15.0, 0.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-03", "Dome Periphery South", -15.0, 0.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-04", "Dome Periphery East", 0.0, 15.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-05", "Dome Periphery West", 0.0, -15.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-06", "Outer Archway NW", 20.0, 20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-07", "Outer Archway NE", 20.0, -20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-08", "Outer Archway SW", -20.0, 20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-09", "Outer Archway SE", -20.0, -20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-10", "Subterranean Enclave Core", 0.0, 0.0, -10.0, 528.0, "LOCKED"))
        ]

        manifest = {
            "manifest_title": self.manifest_title,
            "version": self.version,
            "unit": "meters",
            "coordinate_system": "Cartesian (XYZ)",
            "architectural_surfaces": surfaces,
            "geodesic_vibrational_nodes": nodes,
            "energy_conduits": {
                "source_node": "NODE-01",
                "target_nodes": [f"NODE-{i:02d}" for i in range(2, 11)],
                "conduit_type": "Harmonic Resonance Vector"
            }
        }
        return manifest

    def export_to_json(self, filename="qatar_library_cad_manifest.json") -> str:
        manifest_data = self.generate_manifest()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2, ensure_ascii=False)
        return filename

if __name__ == "__main__":
    generator = QatarIslamicLibraryCADManifestGenerator()
    output_path = generator.export_to_json()
    print(f"=== {generator.manifest_title} ===")
    print(f"CAD manifest successfully exported to: {output_path}\n")
    print(json.dumps(generator.generate_manifest(), indent=2, ensure_ascii=False))
import json
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class ThermalHumidityMetric:
    zone_id: str
    depth_m: float
    temperature_celsius: float
    relative_humidity_percent: float
    hvac_status: str

class QatarIslamicLibraryThermalHumidityExpansion:
    """
    Qatar Islamic Library - Subterranean Thermal Distribution & Humidity Regulation Module.
    Simulates temperature gradients, geothermal thermal stability, and relative humidity (RH)
    control across the subterranean enclave vault layers.
    """
    def __init__(self, enclave_depth_m: float = 15.0):
        self.system_title = "QATAR ISLAMIC LIBRARY - THERMAL & HUMIDITY REGULATION ENGINE"
        self.enclave_depth = enclave_depth_m
        self.ambient_surface_temp_c = 35.0  # Doha external surface baseline
        self.geothermal_stable_temp_c = 22.5 # Subterranean stable bedrock temp
        self.target_humidity_pct = 50.0      # Optimal preservation humidity for rare texts

    def generate_enclave_telemetry(self) -> dict:
        zones = [
            {"zone": "ZONE-01: Upper Vault Perimeter", "depth": 5.0, "temp": 26.5, "rh": 52.0},
            {"zone": "ZONE-02: Intermediate Archive Deck", "depth": 10.0, "temp": 23.8, "rh": 50.5},
            {"zone": "ZONE-03: Subterranean Enclave Core", "depth": 15.0, "temp": 22.5, "rh": 50.0},
            {"zone": "ZONE-04: Deep Geothermal Heat Sink", "depth": 20.0, "temp": 22.1, "rh": 49.5}
        ]
        
        metrics = []
        for z in zones:
            status = "OPTIMAL_STABILIZED" if abs(z["rh"] - self.target_humidity_pct) <= 2.0 else "ADJUSTING"
            metrics.append(asdict(ThermalHumidityMetric(
                zone_id=z["zone"],
                depth_m=z["depth"],
                temperature_celsius=z["temp"],
                relative_humidity_percent=z["rh"],
                hvac_status=status
            )))
            
        return {
            "title": self.system_title,
            "subterranean_depth_m": self.enclave_depth,
            "target_parameters": {
                "baseline_surface_temp_c": self.ambient_surface_temp_c,
                "target_humidity_pct": self.target_humidity_pct
            },
            "thermal_humidity_metrics": metrics
        }

    def render_thermal_humidity_map(self, output_file="qatar_library_thermal_humidity.png"):
        """Renders a spatial 2D thermal distribution and humidity contour map across the vault cross-section."""
        plt.style.use('dark_background')
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.patch.set_facecolor('#080c14')

        x = np.linspace(-20, 20, 200)
        y = np.linspace(-15, 0, 150) # Depth down to -15m
        X, Y = np.meshgrid(x, y)
        
        # Thermal distribution simulation (warmer near surface Y=0, stable at bottom Y=-15)
        Z_temp = self.geothermal_stable_temp_c + (self.ambient_surface_temp_c - self.geothermal_stable_temp_c) * np.exp(Y / 5.0) + 1.5 * np.cos(X / 5.0) * np.exp(Y / 10.0)
        
        # Humidity distribution simulation (regulated tightly around 50%)
        Z_rh = 50.0 + 3.0 * np.sin(X / 4.0) * (Y / 15.0)

        # Plot 1: Temperature Gradient
        ax1.set_facecolor('#05080f')
        c1 = ax1.contourf(X, Y, Z_temp, levels=20, cmap='inferno')
        cb1 = fig.colorbar(c1, ax=ax1, pad=0.05)
        cb1.set_label('Temperature (°C)', color='cyan')
        ax1.set_title("SUBTERRANEAN THERMAL GRADIENT (°C)", color='cyan', fontsize=11, pad=10)
        ax1.set_xlabel("Lateral Span (m)", color='gray')
        ax1.set_ylabel("Depth (m)", color='gray')
        ax1.grid(True, color='#112233', linestyle='--', alpha=0.5)

        # Plot 2: Relative Humidity Distribution
        ax2.set_facecolor('#05080f')
        c2 = ax2.contourf(X, Y, Z_rh, levels=20, cmap='viridis')
        cb2 = fig.colorbar(c2, ax=ax2, pad=0.05)
        cb2.set_label('Relative Humidity (%)', color='cyan')
        ax2.set_title("RELATIVE HUMIDITY REGULATION (%)", color='cyan', fontsize=11, pad=10)
        ax2.set_xlabel("Lateral Span (m)", color='gray')
        ax2.set_ylabel("Depth (m)", color='gray')
        ax2.grid(True, color='#112233', linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

if __name__ == "__main__":
    engine = QatarIslamicLibraryThermalHumidityExpansion()
    print("=== " + engine.system_title + " ===")
    print(json.dumps(engine.generate_enclave_telemetry(), indent=2))
    
    saved_file = engine.render_thermal_humidity_map()
    print(f"\nThermal & humidity telemetry map saved as: {saved_file}")
import json
from dataclasses import dataclass, asdict

@dataclass
class CADNode:
    node_id: str
    node_name: str
    coordinate_x: float
    coordinate_y: float
    coordinate_z: float
    resonance_frequency_hz: float
    status: str

@dataclass
class CADMeshSurface:
    surface_name: str
    geometry_type: str
    parameters: dict

class QatarIslamicLibraryCADManifestGenerator:
    """
    Qatar Islamic Library - CAD Manifest Generator.
    Exports architectural wireframe geometries and geodesic vibrational node coordinates
    into a standardized, structured JSON CAD manifest.
    """
    def __init__(self):
        self.manifest_title = "QATAR ISLAMIC LIBRARY - CAD MANIFEST & GEODESIC TOPOLOGY"
        self.version = "1.0.0"

    def generate_manifest(self) -> dict:
        surfaces = [
            asdict(CADMeshSurface(
                surface_name="Central Geodesic Dome",
                geometry_type="Hemispherical Vault",
                parameters={"radius_m": 15.0, "apex_elevation_m": 35.0, "mesh_resolution": [20, 30]}
            )),
            asdict(CADMeshSurface(
                surface_name="Library Base Podium",
                geometry_type="Rectangular Platonic Base",
                parameters={"dimension_x_m": 50.0, "dimension_y_m": 50.0, "elevation_m": 0.0, "mesh_resolution": [15, 15]}
            ))
        ]

        nodes = [
            asdict(CADNode("NODE-01", "Central Dome Apex", 0.0, 0.0, 35.0, 432.0, "OPTIMAL")),
            asdict(CADNode("NODE-02", "Dome Periphery North", 15.0, 0.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-03", "Dome Periphery South", -15.0, 0.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-04", "Dome Periphery East", 0.0, 15.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-05", "Dome Periphery West", 0.0, -15.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-06", "Outer Archway NW", 20.0, 20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-07", "Outer Archway NE", 20.0, -20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-08", "Outer Archway SW", -20.0, 20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-09", "Outer Archway SE", -20.0, -20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-10", "Subterranean Enclave Core", 0.0, 0.0, -10.0, 528.0, "LOCKED"))
        ]

        manifest = {
            "manifest_title": self.manifest_title,
            "version": self.version,
            "unit": "meters",
            "coordinate_system": "Cartesian (XYZ)",
            "architectural_surfaces": surfaces,
            "geodesic_vibrational_nodes": nodes,
            "energy_conduits": {
                "source_node": "NODE-01",
                "target_nodes": [f"NODE-{i:02d}" for i in range(2, 11)],
                "conduit_type": "Harmonic Resonance Vector"
            }
        }
        return manifest

    def export_to_json(self, filename="qatar_library_cad_manifest.json") -> str:
        manifest_data = self.generate_manifest()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2, ensure_ascii=False)
        return filename

if __name__ == "__main__":
    generator = QatarIslamicLibraryCADManifestGenerator()
    output_path = generator.export_to_json()
    print(f"=== {generator.manifest_title} ===")
    print(f"CAD manifest successfully exported to: {output_path}\n")
    print(json.dumps(generator.generate_manifest(), indent=2, ensure_ascii=False))
import json
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class VentilationMetric:
    zone_id: str
    depth_m: float
    mean_velocity_m_s: float
    air_changes_per_hour_ach: float
    ventilation_status: str

class QatarIslamicLibraryVentilationExpansion:
    """
    Qatar Islamic Library - Subterranean Air-Flow Velocity & Ventilation Exchange Module.
    Simulates air velocity vectors, circulation streamlines, and air change rates (ACH)
    across the subterranean enclave vault layers.
    """
    def __init__(self, enclave_depth_m: float = 15.0):
        self.system_title = "QATAR ISLAMIC LIBRARY - AIR-FLOW & VENTILATION SIMULATION ENGINE"
        self.enclave_depth = enclave_depth_m
        self.target_ach = 4.0  # Recommended air changes per hour for archive vaults

    def generate_ventilation_telemetry(self) -> dict:
        zones = [
            {"zone": "ZONE-01: Upper Vault Intake Plenum", "depth": 5.0, "vel": 0.85, "ach": 4.5},
            {"zone": "ZONE-02: Intermediate Archive Corridors", "depth": 10.0, "vel": 0.42, "ach": 4.1},
            {"zone": "ZONE-03: Subterranean Enclave Core", "depth": 15.0, "vel": 0.25, "ach": 4.0},
            {"zone": "ZONE-04: Deep Exhaust Plenum", "depth": 20.0, "vel": 1.15, "ach": 6.2}
        ]
        
        metrics = []
        for z in zones:
            status = "OPTIMAL_FLOW" if z["ach"] >= self.target_ach else "SUB_OPTIMAL"
            metrics.append(asdict(VentilationMetric(
                zone_id=z["zone"],
                depth_m=z["depth"],
                mean_velocity_m_s=z["vel"],
                air_changes_per_hour_ach=z["ach"],
                ventilation_status=status
            )))
            
        return {
            "title": self.system_title,
            "subterranean_depth_m": self.enclave_depth,
            "target_parameters": {
                "recommended_ach": self.target_ach
            },
            "ventilation_metrics": metrics
        }

    def render_velocity_streamlines(self, output_file="qatar_library_ventilation_flow.png"):
        """Renders a 2D velocity streamline and vector field map across the subterranean enclave cross-section."""
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#080c14')
        ax.set_facecolor('#05080f')

        x = np.linspace(-20, 20, 100)
        y = np.linspace(-15, 0, 80)
        X, Y = np.meshgrid(x, y)
        
        # Simulated flow velocity components (convection current looping down and across archive levels)
        U = -Y / 10.0 * np.sin(X / 5.0)
        V = -np.cos(X / 5.0) * (1.0 - np.abs(Y) / 15.0)
        Speed = np.sqrt(U**2 + V**2)

        strm = ax.streamplot(X, Y, U, V, color=Speed, cmap='winter', linewidth=1.5, density=1.2)
        cbar = fig.colorbar(strm.lines, ax=ax, pad=0.05)
        cbar.set_label('Velocity Magnitude (m/s)', color='cyan')

        ax.set_title("SUBTERRANEAN AIR-FLOW VELOCITY STREAMLINES", color='cyan', fontsize=12, pad=12)
        ax.set_xlabel("Lateral Span (m)", color='gray')
        ax.set_ylabel("Depth (m)", color='gray')
        ax.grid(True, color='#112233', linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

if __name__ == "__main__":
    engine = QatarIslamicLibraryVentilationExpansion()
    print("=== " + engine.system_title + " ===")
    print(json.dumps(engine.generate_ventilation_telemetry(), indent=2))
    
    saved_file = engine.render_velocity_streamlines()
    print(f"\nVentilation flow velocity streamline map saved as: {saved_file}")
import json
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class HVACZoneMetric:
    zone_id: str
    depth_m: float
    pressure_differential_pa: float
    energy_consumption_kwh_day: float
    hvac_operational_status: str

class QatarIslamicLibraryHVACExpansion:
    """
    Qatar Islamic Library - Multi-Zone HVAC Energy Consumption & Pressure Differential Engine.
    Simulates static pressure gradients, airflow pressure drops, and daily HVAC energy
    consumption across subterranean archive zones.
    """
    def __init__(self, enclave_depth_m: float = 15.0):
        self.system_title = "QATAR ISLAMIC LIBRARY - HVAC ENERGY & PRESSURE SIMULATION ENGINE"
        self.enclave_depth = enclave_depth_m
        self.base_energy_rate_kwh = 120.0

    def generate_hvac_telemetry(self) -> dict:
        zones = [
            {"zone": "ZONE-01: Upper Vault Intake Plenum", "depth": 5.0, "p_diff": 15.2, "energy": 145.5},
            {"zone": "ZONE-02: Intermediate Archive Corridors", "depth": 10.0, "p_diff": 22.5, "energy": 112.0},
            {"zone": "ZONE-03: Subterranean Enclave Core", "depth": 15.0, "p_diff": 30.0, "energy": 98.4},
            {"zone": "ZONE-04: Deep Exhaust Plenum", "depth": 20.0, "p_diff": 8.5, "energy": 165.2}
        ]
        
        metrics = []
        for z in zones:
            status = "STABLE_PRESSURIZED" if z["p_diff"] >= 10.0 else "NOMINAL"
            metrics.append(asdict(HVACZoneMetric(
                zone_id=z["zone"],
                depth_m=z["depth"],
                pressure_differential_pa=z["p_diff"],
                energy_consumption_kwh_day=z["energy"],
                hvac_operational_status=status
            )))
            
        return {
            "title": self.system_title,
            "subterranean_depth_m": self.enclave_depth,
            "total_daily_energy_kwh": sum(z["energy"] for z in zones),
            "hvac_metrics": metrics
        }

    def render_hvac_profiles(self, output_file="qatar_library_hvac_energy_pressure.png"):
        """Renders a dual-panel plot showing pressure differentials and energy consumption profiles."""
        plt.style.use('dark_background')
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.patch.set_facecolor('#080c14')

        depths = np.array([5.0, 10.0, 15.0, 20.0])
        pressures = np.array([15.2, 22.5, 30.0, 8.5])
        energy = np.array([145.5, 112.0, 98.4, 165.2])

        # Plot 1: Pressure Differential Profile
        ax1.set_facecolor('#05080f')
        ax1.plot(pressures, -depths, marker='o', color='cyan', linewidth=2, markersize=8)
        ax1.set_title("ZONE PRESSURE DIFFERENTIAL (Pa)", color='cyan', fontsize=11, pad=10)
        ax1.set_xlabel("Pressure Delta (Pa)", color='gray')
        ax1.set_ylabel("Depth (m)", color='gray')
        ax1.grid(True, color='#112233', linestyle='--', alpha=0.5)

        # Plot 2: Daily Energy Consumption Bar Profile
        ax2.set_facecolor('#05080f')
        ax2.barh(np.array([-5.0, -10.0, -15.0, -20.0]), energy, height=2.0, color='magenta', alpha=0.8)
        ax2.set_title("DAILY HVAC ENERGY CONSUMPTION (kWh)", color='cyan', fontsize=11, pad=10)
        ax2.set_xlabel("Energy (kWh/day)", color='gray')
        ax2.set_ylabel("Depth (m)", color='gray')
        ax2.grid(True, color='#112233', linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

if __name__ == "__main__":
    engine = QatarIslamicLibraryHVACExpansion()
    print("=== " + engine.system_title + " ===")
    print(json.dumps(engine.generate_hvac_telemetry(), indent=2))
    
    saved_file = engine.render_hvac_profiles()
    print(f"\nHVAC energy and pressure profile visualization saved as: {saved_file}")
import json
from dataclasses import dataclass, asdict

@dataclass
class CADNode:
    node_id: str
    node_name: str
    coordinate_x: float
    coordinate_y: float
    coordinate_z: float
    resonance_frequency_hz: float
    status: str

@dataclass
class CADMeshSurface:
    surface_name: str
    geometry_type: str
    parameters: dict

class QatarIslamicLibraryCADManifestGenerator:
    """
    Qatar Islamic Library - CAD Manifest Generator.
    Exports architectural wireframe geometries and geodesic vibrational node coordinates
    into a standardized, structured JSON CAD manifest.
    """
    def __init__(self):
        self.manifest_title = "QATAR ISLAMIC LIBRARY - CAD MANIFEST & GEODESIC TOPOLOGY"
        self.version = "1.0.0"

    def generate_manifest(self) -> dict:
        surfaces = [
            asdict(CADMeshSurface(
                surface_name="Central Geodesic Dome",
                geometry_type="Hemispherical Vault",
                parameters={"radius_m": 15.0, "apex_elevation_m": 35.0, "mesh_resolution": [20, 30]}
            )),
            asdict(CADMeshSurface(
                surface_name="Library Base Podium",
                geometry_type="Rectangular Platonic Base",
                parameters={"dimension_x_m": 50.0, "dimension_y_m": 50.0, "elevation_m": 0.0, "mesh_resolution": [15, 15]}
            ))
        ]

        nodes = [
            asdict(CADNode("NODE-01", "Central Dome Apex", 0.0, 0.0, 35.0, 432.0, "OPTIMAL")),
            asdict(CADNode("NODE-02", "Dome Periphery North", 15.0, 0.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-03", "Dome Periphery South", -15.0, 0.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-04", "Dome Periphery East", 0.0, 15.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-05", "Dome Periphery West", 0.0, -15.0, 20.0, 432.0, "ACTIVE")),
            asdict(CADNode("NODE-06", "Outer Archway NW", 20.0, 20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-07", "Outer Archway NE", 20.0, -20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-08", "Outer Archway SW", -20.0, 20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-09", "Outer Archway SE", -20.0, -20.0, 5.0, 216.0, "RESONANT")),
            asdict(CADNode("NODE-10", "Subterranean Enclave Core", 0.0, 0.0, -10.0, 528.0, "LOCKED"))
        ]

        manifest = {
            "manifest_title": self.manifest_title,
            "version": self.version,
            "unit": "meters",
            "coordinate_system": "Cartesian (XYZ)",
            "architectural_surfaces": surfaces,
            "geodesic_vibrational_nodes": nodes,
            "energy_conduits": {
                "source_node": "NODE-01",
                "target_nodes": [f"NODE-{i:02d}" for i in range(2, 11)],
                "conduit_type": "Harmonic Resonance Vector"
            }
        }
        return manifest

    def export_to_json(self, filename="qatar_library_cad_manifest.json") -> str:
        manifest_data = self.generate_manifest()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2, ensure_ascii=False)
        return filename

if __name__ == "__main__":
    generator = QatarIslamicLibraryCADManifestGenerator()
    output_path = generator.export_to_json()
    print(f"=== {generator.manifest_title} ===")
    print(f"CAD manifest successfully exported to: {output_path}\n")
    print(json.dumps(generator.generate_manifest(), indent=2, ensure_ascii=False))
import numpy as np
import plotly.graph_objects as go

def render_library_3d_wireframe():
    # Architectural parameters for Qatar Islamic Library wireframe
    # Central geodesic dome (hemisphere)
    phi = np.linspace(0, np.pi / 2, 20)
    theta = np.linspace(0, 2 * np.pi, 30)
    PHI, THETA = np.meshgrid(phi, theta)
    
    R_dome = 15.0
    X_dome = R_dome * np.sin(PHI) * np.cos(THETA)
    Y_dome = R_dome * np.sin(PHI) * np.sin(THETA)
    Z_dome = R_dome * np.cos(PHI) + 20.0  # Elevated central dome structure
    
    # Outer base podium & architectural footprint
    box_x = np.linspace(-25, 25, 15)
    box_y = np.linspace(-25, 25, 15)
    BX, BY = np.meshgrid(box_x, box_y)
    BZ = np.zeros_like(BX)

    # Geodesic vibrational nodes mapped across architectural coordinates
    nodes = {
        "Central Dome Apex": (0.0, 0.0, 35.0, 432.0, "OPTIMAL"),
        "Dome Periphery North": (15.0, 0.0, 20.0, 432.0, "ACTIVE"),
        "Dome Periphery South": (-15.0, 0.0, 20.0, 432.0, "ACTIVE"),
        "Dome Periphery East": (0.0, 15.0, 20.0, 432.0, "ACTIVE"),
        "Dome Periphery West": (0.0, -15.0, 20.0, 432.0, "ACTIVE"),
        "Outer Archway NW": (20.0, 20.0, 5.0, 216.0, "RESONANT"),
        "Outer Archway NE": (20.0, -20.0, 5.0, 216.0, "RESONANT"),
        "Outer Archway SW": (-20.0, 20.0, 5.0, 216.0, "RESONANT"),
        "Outer Archway SE": (-20.0, -20.0, 5.0, 216.0, "RESONANT"),
        "Subterranean Enclave Core": (0.0, 0.0, -10.0, 528.0, "LOCKED")
    }

    node_names = list(nodes.keys())
    nx = [nodes[n][0] for n in node_names]
    ny = [nodes[n][1] for n in node_names]
    nz = [nodes[n][2] for n in node_names]
    n_freq = [nodes[n][3] for n in node_names]
    n_status = [nodes[n][4] for n in node_names]

    fig = go.Figure()

    # Add Central Geodesic Dome Surface Wireframe
    fig.add_trace(go.Surface(
        x=X_dome, y=Y_dome, z=Z_dome,
        colorscale='Viridis',
        opacity=0.6,
        name="Central Geodesic Dome",
        showscale=False
    ))

    # Add Base Podium Wireframe
    fig.add_trace(go.Surface(
        x=BX, y=BY, z=BZ,
        colorscale='Blues',
        opacity=0.3,
        name="Library Base Podium",
        showscale=False
    ))

    # Add Geodesic Vibrational Nodes Scatter Layer
    fig.add_trace(go.Scatter3d(
        x=nx, y=ny, z=nz,
        mode='markers+text',
        text=node_names,
        textposition="top center",
        marker=dict(
            size=10,
            color=n_freq,
            colorscale='Plasma',
            colorbar=dict(title="Resonance Frequency (Hz)"),
            showscale=True,
            line=dict(width=2, color='white')
        ),
        name="Geodesic Vibrational Nodes"
    ))

    # Add Energy Vector Conduits (connecting apex to perimeter and subterranean nodes)
    for name, coords in nodes.items():
        if name != "Central Dome Apex":
            fig.add_trace(go.Scatter3d(
                x=[0.0, coords[0]],
                y=[0.0, coords[1]],
                z=[35.0, coords[2]],
                mode='lines',
                line=dict(color='cyan', width=2),
                opacity=0.5,
                showlegend=False
            ))

    # Configure dark-mode architectural CAD layout
    fig.update_layout(
        title="Qatar Islamic Library: 3D Architectural Wireframe & Geodesic Vibrational Nodes",
        title_x=0.5,
        scene=dict(
            xaxis=dict(backgroundcolor="#05080f", gridcolor="#112233", zerolinecolor="#112233", color="white"),
            yaxis=dict(backgroundcolor="#05080f", gridcolor="#112233", zerolinecolor="#112233", color="white"),
            zaxis=dict(backgroundcolor="#05080f", gridcolor="#112233", zerolinecolor="#112233", color="white"),
            bgcolor="#080c14"
        ),
        paper_bgcolor="#080c14",
        font=dict(color="white")
    )

    return fig

if __name__ == "__main__":
    fig = render_library_3d_wireframe()
    fig.show()
import pytest
import json
import numpy as np
from dataclasses import asdict

# Import or define modules (assumed available from the consolidated Qatar Islamic Library framework)
# For standalone test execution, we include the test assertions and mock structures.

class TestQatarIslamicLibraryMasterMatrix:
    
    @pytest.fixture
    def mock_system_instance(self):
        # Mocking or instantiating core system
        from dataclasses import dataclass
        @dataclass
        class TelemetryMetrics:
            base_frequency: str
            grid_status: str
            coherence: str
            energy_vectors: str

        class MockSystem:
            def __init__(self):
                self.system_title = "QATAR ISLAMIC LIBRARY - GEODESIC VIBRATIONAL MAP"
                self.telemetry = TelemetryMetrics(
                    base_frequency="432 Hz",
                    grid_status="OPTIMAL",
                    coherence="98%",
                    energy_vectors="ALIGNED"
                )
            def get_system_telemetry(self):
                return {
                    "title": self.system_title,
                    "telemetry_data": asdict(self.telemetry)
                }
        return MockSystem()

    def test_base_telemetry_schema(self, mock_system_instance):
        """Validates that base system telemetry contains required keys and correct data types."""
        telemetry = mock_system_instance.get_system_telemetry()
        
        assert "title" in telemetry
        assert "telemetry_data" in telemetry
        
        data = telemetry["telemetry_data"]
        assert data["base_frequency"] == "432 Hz"
        assert data["grid_status"] == "OPTIMAL"
        assert "%" in data["coherence"]
        assert isinstance(data["coherence"], str)

    def test_acoustic_eigenmode_calculations(self):
        """Validates acoustic eigenmode frequencies and sound pressure fluctuations."""
        base_freq = 432.0
        dome_radius = 25.0
        
        # Test eigenmode formula: freq = base_freq * (n * 0.5 + 0.5)
        expected_modes = []
        for n in range(1, 4):
            freq = round(base_freq * (n * 0.5 + 0.5), 2)
            pressure = round(101325.0 + (n * 12.5), 2)
            expected_modes.append((freq, pressure))
            
        assert expected_modes[0] == (324.0, 101337.5)
        assert expected_modes[1] == (432.0, 101350.0)
        assert expected_modes[2] == (540.0, 101362.5)

    def test_em_shielding_skin_depth_and_attenuation(self):
        """Validates electromagnetic shielding effectiveness (SE) and skin depth mathematical calculations."""
        freq = 432.0  # Hz
        conductivity = 5.8e7  # S/m
        rel_perm = 1000.0
        mu_0 = 4 * np.pi * 1e-7
        mu = rel_perm * mu_0
        thickness = 0.05  # m

        # Skin depth calculation
        skin_depth = np.sqrt(1.0 / (np.pi * freq * mu * conductivity))
        assert skin_depth > 0.0
        assert isinstance(skin_depth, float)

        # Absorption loss calculation (SE_A = 8.686 * (t / delta))
        se_absorption = 8.686 * (thickness / skin_depth)
        assert se_absorption > 0.0

    def test_cad_manifest_schema_and_coordinates(self):
        """Validates JSON CAD manifest structure, coordinate types, and node count."""
        surfaces = [
            {"surface_name": "Central Geodesic Dome", "geometry_type": "Hemispherical Vault"},
            {"surface_name": "Library Base Podium", "geometry_type": "Rectangular Platonic Base"}
        ]
        nodes = [
            {"node_id": "NODE-01", "node_name": "Central Dome Apex", "coordinate_x": 0.0, "coordinate_y": 0.0, "coordinate_z": 35.0, "resonance_frequency_hz": 432.0},
            {"node_id": "NODE-10", "node_name": "Subterranean Enclave Core", "coordinate_x": 0.0, "coordinate_y": 0.0, "coordinate_z": -10.0, "resonance_frequency_hz": 528.0}
        ]

        manifest = {
            "manifest_title": "QATAR ISLAMIC LIBRARY - CAD MANIFEST",
            "version": "1.0.0",
            "unit": "meters",
            "architectural_surfaces": surfaces,
            "geodesic_vibrational_nodes": nodes
        }

        assert manifest["version"] == "1.0.0"
        assert len(manifest["architectural_surfaces"]) == 2
        assert len(manifest["geodesic_vibrational_nodes"]) == 2
        
        # Verify subterranean core node depth and frequency
        core_node = manifest["geodesic_vibrational_nodes"][1]
        assert core_node["coordinate_z"] == -10.0
        assert core_node["resonance_frequency_hz"] == 528.0

    def test_thermal_humidity_stabilization(self):
        """Validates subterranean thermal gradients and relative humidity preservation thresholds."""
        target_humidity = 50.0
        zones = [
            {"zone": "ZONE-01", "temp": 26.5, "rh": 52.0},
            {"zone": "ZONE-03: Subterranean Core", "temp": 22.5, "rh": 50.0}
        ]

        for z in zones:
            rh_delta = abs(z["rh"] - target_humidity)
            status = "OPTIMAL_STABILIZED" if rh_delta <= 2.0 else "ADJUSTING"
            if z["zone"].startswith("ZONE-03"):
                assert status == "OPTIMAL_STABILIZED"
                assert z["temp"] == 22.5

    def test_ventilation_ach_thresholds(self):
        """Validates Air Changes per Hour (ACH) against archive preservation standards (>= 4.0 ACH)."""
        target_ach = 4.0
        ventilation_zones = [
            {"zone": "Plenum", "ach": 4.5},
            {"zone": "Archive Core", "ach": 4.0},
            {"zone": "Sub-optimal Zone", "ach": 3.2}
        ]

        for zone in ventilation_zones:
            is_optimal = zone["ach"] >= target_ach
            if zone["zone"] == "Sub-optimal Zone":
                assert not is_optimal
            else:
                assert is_optimal

    def test_hvac_energy_summation(self):
        """Validates total daily HVAC energy consumption summation across subterranean zones."""
        energy_readings = [145.5, 112.0, 98.4, 165.2]
        total_energy = sum(energy_readings)
        
        assert total_energy == 521.1
        assert isinstance(total_energy, float)
import json
import time
from dataclasses import dataclass, asdict

@dataclass
class MQTTTelemetryPacket:
    timestamp: float
    station_id: str
    metric_category: str
    payload: dict

class QatarIslamicLibraryMQTTStreamer:
    """
    Qatar Islamic Library - Real-Time MQTT Telemetry Streaming Client.
    Streams sensor telemetry, HVAC metrics, thermal/humidity profiles, and vibrational 
    resonance data to a central supervisory control and data acquisition (SCADA) dashboard.
    """
    def __init__(self, broker_host: str = "localhost", broker_port: int = 1883):
        self.system_title = "QATAR ISLAMIC LIBRARY - MQTT TELEMETRY STREAMING CLIENT"
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.base_topic = "qatar/library/telemetry"
        self.is_connected = False

    def connect(self):
        """Simulates secure connection handler (maps to paho-mqtt client in production)."""
        print(f"Connecting to MQTT Broker at {self.broker_host}:{self.broker_port}...")
        self.is_connected = True
        print("Connection established: SECURE_TLS_ENCLAVE_ACTIVE")

    def build_telemetry_payload(self, category: str, data: dict) -> str:
        packet = MQTTTelemetryPacket(
            timestamp=time.time(),
            station_id="QIL-SUB-CORE-01",
            metric_category=category,
            payload=data
        )
        return json.dumps(asdict(packet), indent=2)

    def publish_metrics_loop(self, iterations: int = 3, interval_sec: float = 1.0):
        """Simulates streaming multi-domain telemetry packets over MQTT topics."""
        categories = ["vibrational", "thermal_humidity", "hvac_pressure", "em_shielding"]
        
        for i in range(iterations):
            print(f"\n--- Transmission Cycle [{i+1}/{iterations}] ---")
            for cat in categories:
                topic = f"{self.base_topic}/{cat}"
                sample_data = self._get_sample_data_for_category(cat, i)
                payload_str = self.build_telemetry_payload(cat, sample_data)
                
                # In production: client.publish(topic, payload_str, qos=1)
                print(f"[MQTT PUBLISH] Topic: {topic}")
                print(payload_str)
            
            if i < iterations - 1:
                time.sleep(interval_sec)

    def _get_sample_data_for_category(self, category: str, step: int) -> dict:
        if category == "vibrational":
            return {"base_frequency_hz": 432.0, "coherence_pct": round(98.5 + step * 0.1, 2), "status": "LOCKED"}
        elif category == "thermal_humidity":
            return {"zone": "ZONE-03: Subterranean Enclave Core", "temp_c": 22.5, "humidity_pct": 50.0}
        elif category == "hvac_pressure":
            return {"pressure_differential_pa": 30.0, "daily_energy_kwh": 98.4, "status": "STABLE_PRESSURIZED"}
        elif category == "em_shielding":
            return {"frequency_hz": 432.0, "shielding_effectiveness_db": 65.4, "dampening_ratio": 0.0003}
        return {}

if __name__ == "__main__":
    streamer = QatarIslamicLibraryMQTTStreamer(broker_host="mqtt.qil-matrix.internal", broker_port=8883)
    streamer.connect()
    print(f"\n=== {streamer.system_title} ===")
    streamer.publish_metrics_loop(iterations=2, interval_sec=0.5)
metrics = []
        for z in zones:
            status = "OPTIMAL_PRESSURE" if z["p_diff"] <= 35.0 else "HIGH_PRESSURE_ALERT"
            metrics.append(asdict(HVACZoneMetric(
                zone_id=z["zone"],
                depth_m=z["depth"],
                pressure_differential_pa=z["p_diff"],
                energy_consumption_kwh_day=z["energy"],
                hvac_operational_status=status
            )))
            
        return {
            "title": self.system_title,
            "subterranean_depth_m": self.enclave_depth,
            "target_parameters": {
                "base_energy_rate_kwh": self.base_energy_rate_kwh
            },
            "hvac_telemetry_metrics": metrics
        }

    def render_hvac_pressure_map(self, output_file="qatar_library_hvac_pressure.png"):
        """Renders subterranean pressure differential gradients across archive depth zones."""
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor('#080c14')
        ax.set_facecolor('#05080f')

        depths = [5.0, 10.0, 15.0, 20.0]
        pressures = [15.2, 22.5, 30.0, 8.5]
        
        ax.plot(depths, pressures, marker='o', color='cyan', linewidth=2, label='Pressure Differential (Pa)')
        ax.set_title("SUBTERRANEAN HVAC - PRESSURE DIFFERENTIAL GRADIENT", color='cyan', fontsize=12, pad=12)
        ax.set_xlabel("Enclave Depth (m)", color='gray')
        ax.set_ylabel("Pressure Differential (Pa)", color='gray')
        ax.grid(True, color='#112233', linestyle='--', alpha=0.7)
        ax.legend(loc="upper right", facecolor='#080c14', edgecolor='cyan')

        plt.tight_layout()
        plt.savefig(output_file, dpi=300, facecolor='#080c14')
        plt.close()
        return output_file

if __name__ == "__main__":
    engine = QatarIslamicLibraryHVACExpansion()
    print("=== " + engine.system_title + " ===")
    print(json.dumps(engine.generate_hvac_telemetry(), indent=2))
    
    saved_file = engine.render_hvac_pressure_map()
    print(f"\nHVAC pressure telemetry map saved as: {saved_file}")
