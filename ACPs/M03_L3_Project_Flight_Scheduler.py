# Module 3 Lesson 3: After-Class Project
# Project Name: International Flight Departure Array Runway Indexer

class FlightDepartureMatrix:
    def __init__(self):
        self.runway_matrix = []

    def manifest_flight_route(self, callsign, destination_airport, scheduled_departure_epoch):
        self.runway_matrix.append((callsign, destination_airport, scheduled_departure_epoch))
        self.runway_matrix.sort(key=lambda flight: flight[2])

    def drop_cancelled_flight(self, target_callsign):
        self.runway_matrix = [f for f in self.runway_matrix if f[0] != target_callsign]

if __name__ == "__main__":
    airport = FlightDepartureMatrix()
    airport.manifest_flight_route("AI-101", "DEL", 1712832000)
    airport.manifest_flight_route("AA-440", "JFK", 1712828400)
    print(f"Current Chronological Runway Manifest Index: {airport.runway_matrix}")