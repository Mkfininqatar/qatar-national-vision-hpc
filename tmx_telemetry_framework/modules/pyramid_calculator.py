"""
Pyramid Geometry & Logistics Calculator
=======================================
This module calculates the total volume, mass, average block weight,
and daily placement rate for pyramid architecture (e.g., Khufu's Pyramid).
"""

class PyramidCalculator:
    def __init__(self, base_length: float, height: float, total_blocks: int, density: float = 2.5):
        """
        :param base_length: Base side length in meters
        :param height: Height of the pyramid in meters
        :param total_blocks: Estimated number of stone blocks
        :param density: Average density of limestone in metric tons/m³ (default: 2.5)
        """
        self.base_length = base_length
        self.height = height
        self.total_blocks = total_blocks
        self.density = density

    def calculate_volume(self) -> float:
        """Calculates volume of a square pyramid: V = (1/3) * base^2 * height"""
        return (self.base_length ** 2) * self.height / 3.0

    def calculate_total_mass(self) -> float:
        """Calculates total mass in metric tons"""
        return self.calculate_volume() * self.density

    def calculate_avg_block_weight(self) -> dict:
        """Calculates average weight per block in metric tons and kilograms"""
        total_mass = self.calculate_total_mass()
        avg_weight_tons = total_mass / self.total_blocks
        avg_weight_kg = avg_weight_tons * 1000.0
        return {
            "tons": round(avg_weight_tons, 2),
            "kg": round(avg_weight_kg, 2)
        }

    def construction_logistics(self, years: int) -> dict:
        """Calculates blocks required per day/hour assuming continuous construction"""
        total_days = years * 365
        blocks_per_day = self.total_blocks / total_days
        blocks_per_hour = blocks_per_day / 24.0
        
        return {
            "total_days": total_days,
            "blocks_per_day": round(blocks_per_day, 2),
            "blocks_per_hour": round(blocks_per_hour, 2)
        }

if __name__ == "__main__":
    # Great Pyramid of Giza Parameters
    pyramid = PyramidCalculator(
        base_length=230.4,  # meters
        height=146.6,       # meters
        total_blocks=2300000
    )

    volume = pyramid.calculate_volume()
    total_mass = pyramid.calculate_total_mass()
    block_weight = pyramid.calculate_avg_block_weight()
    logistics = pyramid.construction_logistics(years=20)

    print("=" * 50)
    print(" 🏛️  GREAT PYRAMID OF GIZA - MATHEMATICAL MODEL")
    print("=" * 50)
    print(f"Total Volume          : {volume:,.2f} m³")
    print(f"Total Estimated Mass  : {total_mass:,.2f} Metric Tons")
    print(f"Average Block Weight  : {block_weight['kg']} kg ({block_weight['tons']} tons)")
    print("-" * 50)
    print(" ⏱️  CONSTRUCTION LOGISTICS (20 Year Timeline)")
    print("-" * 50)
    print(f"Placement Rate (Daily): {logistics['blocks_per_day']} blocks/day")
    print(f"Placement Rate (Hourly): {logistics['blocks_per_hour']} blocks/hour")
    print("=" * 50)
