# LESSON NAME: M16 Lesson 2 – Bellman-Ford algorithm

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement the standard Bellman-Ford edge relaxation algorithm 
# to calculate short-path values from a source point inside a directed network.
# ==========================================
class BellmanFordStandard:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def process_distances(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges V - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        print(f"Bellman-Ford calculation vectors from Node [{src}]:")
        for i in range(self.V):
            print(f" -> Vertex {i} minimum routing expense: {dist[i]}")

print("--- Activity 1: Standard Bellman-Ford Core Sorter ---")
bf = BellmanFordStandard(3)
bf.add_edge(0, 1, 5)
bf.add_edge(1, 2, -2)
bf.add_edge(0, 2, 7)
bf.process_distances(0)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create a financial currency exchange arbitrage detection terminal 
# that flags negative cycles inside foreign currency conversion logs.
# ==========================================
class ExchangeArbitrageDetector:
    def __init__(self, currency_count):
        self.V = currency_count
        self.edges = []

    def log_exchange_rate(self, from_c, to_c, weight_log):
        self.edges.append((from_c, to_c, weight_log))

    def detect_arbitrage_loop(self, src=0):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # V-th relaxation to scan for a negative cycle
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print(f"⚠️ NEGATIVE VALUE LOOP CORRUPTION FLASHED: Arbitrage route found at edge {u}->{v}!")
                return True
        return False

print("\n--- Activity 2: Currency Arbitrage Loop Radar ---")
radar = ExchangeArbitrageDetector(3)
radar.log_exchange_rate(0, 1, 1)
radar.log_exchange_rate(1, 2, -5)
radar.log_exchange_rate(2, 0, 2) # Formulates negative product sequence
print(f"Is active money exploit loop present in registry? {radar.detect_arbitrage_loop()}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a robust multi-point distributed Distance Vector Routing engine 
# that stops tracking metrics safely when infinity loops or unreachable routes occur.
# ==========================================
class DistanceVectorRouter:
    def __init__(self, node_list):
        self.nodes = node_list
        self.edges = []

    def configure_link(self, u, v, weight):
        self.edges.append((u, v, weight))

    def compute_vector_map(self, gateway_source):
        dist = {node: float('inf') for node in self.nodes}
        dist[gateway_source] = 0

        for _ in range(len(self.nodes) - 1):
            updated = False
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated: break # Optimization for early exit

        return dist

print("\n--- Activity 3: Autonomous Distance Vector Router Engine ---")
network_nodes = ["A", "B", "C", "D"]
router = DistanceVectorRouter(network_nodes)
router.configure_link("A", "B", 2)
router.configure_link("B", "C", 4)
router.configure_link("C", "D", -3)
print(f"Final compiled stable routing table vector for Node A: {router.compute_vector_map('A')}")
print("-" * 40)