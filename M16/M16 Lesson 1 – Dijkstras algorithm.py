# LESSON NAME: M16 Lesson 1 – Dijkstra's algorithm

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement Dijkstra's algorithm from scratch using a basic 
# adjacency matrix representation to find the shortest path from a central server node.
# ==========================================
class MatrixDijkstra:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def _min_distance(self, dist, sptSet):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    def calculate_shortest_paths(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self._min_distance(dist, sptSet)
            if u == -1: break
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print(f"Shortest path vectors from Node [{src}]:")
        for node in range(self.V):
            print(f" -> Destination Node {node} : Min Weight Cost = {dist[node]}")

print("--- Activity 1: Core Matrix Dijkstra Sorter ---")
g = MatrixDijkstra(4)
g.graph = [
    [0, 4, 0, 0],
    [4, 0, 8, 0],
    [0, 8, 0, 7],
    [0, 0, 7, 0]
]
g.calculate_shortest_paths(0)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement an optimized Dijkstra's algorithm using a min-heap priority 
# queue to find the fastest network packet routing route across a large mesh network topology.
# ==========================================
import heapq

class PriorityQueueDijkstra:
    def __init__(self):
        self.graph = {}

    def add_link(self, u, v, weight):
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def find_shortest_route(self, start, target):
        pq = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_node == target:
                return current_dist
            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return float('inf')

print("\n--- Activity 2: Min-Heap Network Routing Engine ---")
net = PriorityQueueDijkstra()
net.add_link("Router-A", "Router-B", 4)
net.add_link("Router-B", "Server-Target", 3)
net.add_link("Router-A", "Server-Target", 10)
min_cost = net.find_shortest_route("Router-A", "Server-Target")
print(f"Optimal low-latency network path weight metric score: {min_cost}ms")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Create a global ride-sharing GPS tracker subsystem that logs 
# structural path histories and updates route maps in real time when road delays happen.
# ==========================================
class RealTimeGPSTracker:
    def __init__(self):
        self.adj = {}

    def add_road(self, u, v, delay):
        if u not in self.adj: self.adj[u] = []
        self.adj[u].append((v, delay))

    def trace_full_gps_path(self, start, end):
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            cost, curr, path = heapq.heappop(pq)
            if curr == end:
                return path, cost
            if curr in visited: continue
            visited.add(curr)

            for neighbor, weight in self.adj.get(curr, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
        return [], float('inf')

print("\n--- Activity 3: Real-Time Dynamic GPS Nav-Tracker ---")
gps = RealTimeGPSTracker()
gps.add_road("Hub-A", "Intersection-B", 5)
gps.add_road("Intersection-B", "Dropoff-C", 2)
gps.add_road("Hub-A", "Dropoff-C", 12)
route, time_taken = gps.trace_full_gps_path("Hub-A", "Dropoff-C")
print(f"Optimal GPS Navigation Path Chain: {route} | Total Transit Time: {time_taken} mins")
print("-" * 40)