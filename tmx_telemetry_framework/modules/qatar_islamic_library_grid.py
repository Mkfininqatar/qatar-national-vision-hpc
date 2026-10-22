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
