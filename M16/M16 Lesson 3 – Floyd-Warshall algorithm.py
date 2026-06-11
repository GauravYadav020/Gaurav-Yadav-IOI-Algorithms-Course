# LESSON NAME: M16 Lesson 3 – Floyd-Warshall algorithm

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement standard triple-nested loop Floyd-Warshall algorithms 
# from scratch to calculate all-pairs shortest paths for structural node configurations.
# ==========================================
def run_floyd_warshall_all_pairs(matrix_grid):
    v = len(matrix_grid)
    dist = [list(row) for row in matrix_grid]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print("All-Pairs shortest path distribution table map:")
    for row in dist:
        print(row)
    return dist

print("--- Activity 1: All-Pairs Shortest Path Framework ---")
INF = float('inf')
initial_map = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
run_floyd_warshall_all_pairs(initial_map)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a city transit network lookup system that finds structural route 
# hops across multi-station commuter infrastructure plans.
# ==========================================
class CityTransitNetworkMap:
    def __init__(self, city_labels):
        self.cities = city_labels
        self.size = len(city_labels)
        self.INF = float('inf')
        self.matrix = [[self.INF] * self.size for _ in range(self.size)]
        for i in range(self.size): self.matrix[i][i] = 0
        self.indices = {city: i for i, city in enumerate(city_labels)}

    def add_transit_line(self, s, d, cost):
        u, v = self.indices[s], self.indices[d]
        self.matrix[u][v] = cost

    def compile_lookup_engine(self):
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])

    def query_commute_cost(self, s, d):
        u, v = self.indices[s], self.indices[d]
        res = self.matrix[u][v]
        return res if res != self.INF else "No direct path routes registered."

print("\n--- Activity 2: City Transit Network Lookup Engine ---")
transit = CityTransitNetworkMap(["S1", "S2", "S3"])
transit.add_transit_line("S1", "S2", 2)
transit.add_transit_line("S2", "S3", 3)
transit.compile_lookup_engine()
print(f"Transit ticket expense value from station S1 to S3: {transit.query_commute_cost('S1', 'S3')} units")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Create a high-performance system routing optimizer that flags 
# negative cycles to prevent software crashes during multi-node calculations.
# ==========================================
def advanced_safety_matrix_processor(graph_grid):
    n = len(graph_grid)
    dist = [list(r) for r in graph_grid]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Scan diagonal components for negative numbers indicating a negative loop structural anomaly
    for i in range(n):
        if dist[i][i] < 0:
            print(f"🚨 EXCEPTION ERROR DETECTED: Node index tracking loop {i} is trapped inside a negative feedback path cycle!")
            return None
    return dist

print("\n--- Activity 3: Hardware System Routing Loop Safeguard ---")
corrupted_grid = [
    [0, 1, float('inf')],
    [float('inf'), 0, -5],
    [-2, float('inf'), 0] # Completes negative execution ring loops
]
advanced_safety_matrix_processor(corrupted_grid)
print("-" * 40)