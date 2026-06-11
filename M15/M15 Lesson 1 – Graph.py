# LESSON NAME: M15 Lesson 1 – Graph

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Create an Edge-List representation for a simple Social Network 
# connection router map and validate if a direct friendship edge exists between two users.
# ==========================================
class SocialEdgeListGraph:
    def __init__(self):
        self.edge_list = []

    def add_friendship(self, user1, user2):
        self.edge_list.append((user1, user2))
        print(f"Friendship logged: {user1} <--> {user2}")

    def check_direct_connection(self, user1, user2):
        print(f"Checking direct link between {user1} and {user2}...")
        return (user1, user2) in self.edge_list or (user2, user1) in self.edge_list

print("--- Activity 1: Social Edge-List Registry ---")
network = SocialEdgeListGraph()
network.add_friendship("Alice", "Bob")
network.add_friendship("Bob", "Charlie")
print(f"Connection status: {network.check_direct_connection('Alice', 'Charlie')}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a production-grade Adjacency Matrix implementation for a 
# city flight routing map supporting directed, weighted routes with dynamic lookup indexing.
# ==========================================
class CityFlightMatrixGraph:
    def __init__(self, cities_list):
        self.cities = cities_list
        self.size = len(cities_list)
        self.matrix = [[0] * self.size for _ in range(self.size)]
        self.city_map = {city: i for i, city in enumerate(cities_list)}

    def register_flight(self, source, destination, cost):
        if source in self.city_map and destination in self.city_map:
            u, v = self.city_map[source], self.city_map[destination]
            self.matrix[u][v] = cost
            print(f"Flight Added: {source} -> {destination} costing ${cost}")

    def display_matrix_ledger(self):
        print("\nFlight Routing Matrix Ledger:")
        for r in self.matrix:
            print(r)

print("\n--- Activity 2: Flight Route Adjacency Matrix ---")
locations = ["Delhi", "Mumbai", "Bangalore"]
flight_grid = CityFlightMatrixGraph(locations)
flight_grid.register_flight("Delhi", "Mumbai", 450)
flight_grid.register_flight("Mumbai", "Bangalore", 300)
flight_grid.display_matrix_ledger()
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an optimization tracking script that analyzes structural footprints 
# (memory allocation size benchmarks) between Matrix layouts vs Edge Lists across large datasets.
# ==========================================
import sys

def profile_graph_footprints():
    nodes_count = 100
    # Simulate Edge List memory consumption footprint
    edge_list_mock = [(i, i+1) for i in range(nodes_count - 1)]
    # Simulate Adjacency Matrix memory allocation footprint
    matrix_mock = [[0] * nodes_count for _ in range(nodes_count)]
    
    print("Graph Representation Profile Evaluation:")
    print(f" * Edge List Storage Allocation Object Size: {sys.getsizeof(edge_list_mock)} bytes")
    print(f" * Adjacency Matrix Row-Space Storage Grid Size: {sys.getsizeof(matrix_mock)} bytes")

print("\n--- Activity 3: Structural Footprint Benchmarker ---")
profile_graph_footprints()
print("-" * 40)