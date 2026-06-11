# Module 6 Lesson 3: After-Class Project
# Project Name: Enterprise Autonomous Vehicle Fleet Abstract Management Framework

from abc import ABC, abstractmethod

class AbstractFleetVehicle(ABC):
    def __init__(self, asset_id, fuel_capacity):
        self.asset_id = asset_id
        self.fuel = fuel_capacity

    @abstractmethod
    def calculate_max_operational_range(self):
        pass

class CommercialCargoTruck(AbstractFleetVehicle):
    def __init__(self, asset_id, fuel_capacity, payload_weight_tons):
        super().__init__(asset_id, fuel_capacity)
        self.payload = payload_weight_tons

    def calculate_max_operational_range(self):
        # Heavy payload weight dynamically degrades standard distance mileage matrices
        efficiency_factor = 15.5 - (self.payload * 0.8)
        return round(self.fuel * max(2.0, efficiency_factor), 2)

if __name__ == "__main__":
    truck = CommercialCargoTruck("TRUCK-AX-44", 120, 8.5)
    print(f"Truck Asset operational travel range metric: {truck.calculate_max_operational_range()} KM")