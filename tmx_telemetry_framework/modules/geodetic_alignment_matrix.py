import numpy as np
import json
from dataclasses import dataclass, asdict

@dataclass
class GeodeticVectorResult:
    source_location: str
    target_location: str
    distance_km: float
    azimuth_bearing_deg: float
    frequency_432_nodes: float
    frequency_528_nodes: float
    protocol_status: str

class DohaGeodeticMatrix:
    """
    TMX-1 Master Matrix - Doha to Giza & Jerusalem Geodetic & Frequency Engine.
    """
    def __init__(self):
        self.R = 6371.0  # Earth radius in km
        self.c = 299792458.0  # Wave propagation constant in m/s
        self.doha = (25.2854, 51.5310)
        self.giza = (29.9773, 31.1325)
        self.jerusalem = (31.7683, 35.2137)

    def compute_haversine(self, coord1, coord2) -> float:
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
        c_val = 2 * np.arcsin(np.sqrt(a))
        return self.R * c_val

    def compute_bearing(self, coord1, coord2) -> float:
        lat1, lon1 = map(np.radians, coord1)
        lat2, lon2 = map(np.radians, coord2)
        dlon = lon2 - lon1
        x = np.sin(dlon) * np.cos(lat2)
        y = np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(dlon)
        bearing = np.arctan2(x, y)
        return float((np.degrees(bearing) + 360) % 360)

    def analyze_frequency_nodes(self, distance_km: float) -> tuple:
        dist_m = distance_km * 1000.0
        lam_432 = self.c / 432.0
        lam_528 = self.c / 528.0
        return round(dist_m / lam_432, 2), round(dist_m / lam_528, 2)

    def generate_matrix_report(self) -> dict:
        dist_giza = self.compute_haversine(self.doha, self.giza)
        bear_giza = self.compute_bearing(self.doha, self.giza)
        n432_g, n528_g = self.analyze_frequency_nodes(dist_giza)

        dist_jer = self.compute_haversine(self.doha, self.jerusalem)
        bear_jer = self.compute_bearing(self.doha, self.jerusalem)
        n432_j, n528_j = self.analyze_frequency_nodes(dist_jer)

        return {
            "Doha_to_Giza": asdict(GeodeticVectorResult(
                source_location="Doha Enclave (Qatar)",
                target_location="Giza Pyramid Complex (Egypt)",
                distance_km=round(dist_giza, 2),
                azimuth_bearing_deg=round(bear_giza, 2),
                frequency_432_nodes=n432_g,
                frequency_528_nodes=n528_g,
                protocol_status="Giza_Grid_v2.1 - Verified"
            )),
            "Doha_to_Jerusalem": asdict(GeodeticVectorResult(
                source_location="Doha Enclave (Qatar)",
                target_location="Jerusalem Complex",
                distance_km=round(dist_jer, 2),
                azimuth_bearing_deg=round(bear_jer, 2),
                frequency_432_nodes=n432_j,
                frequency_528_nodes=n528_j,
                protocol_status="Giza_Grid_v2.1 - Verified"
            ))
        }

if __name__ == "__main__":
    matrix = DohaGeodeticMatrix()
    report = matrix.generate_matrix_report()
    print(json.dumps(report, indent=2))
