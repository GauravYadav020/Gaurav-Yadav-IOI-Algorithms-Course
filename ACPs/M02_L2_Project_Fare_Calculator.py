# Module 2 Lesson 2: After-Class Project
# Project Name: Dynamic Transit Network Distance Fare Evaluation Engine

class TransitFareEngine:
    def __init__(self, base_rate=4.50, cost_per_km=1.75, surge_multiplier=1.4):
        self.base_rate = base_rate
        self.per_km = cost_per_km
        self.surge = surge_multiplier

    def evaluate_trip_billing(self, total_distance_km, is_peak_hour_rush):
        if total_distance_km <= 0: return 0.0
        computed_subtotal = self.base_rate + (total_distance_km * self.per_km)
        if is_peak_hour_rush:
            computed_subtotal *= self.surge
        return round(computed_subtotal, 2)

if __name__ == "__main__":
    engine = TransitFareEngine()
    print(f"Calculated Dynamic Route Invoice Total: ${engine.evaluate_trip_billing(24.5, True)}")