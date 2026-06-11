# LESSON NAME: M15 Lesson 2 – Graph using adjacency list

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic dictionary-based Adjacency List to map out 
# a local server network topology schema, tracking server endpoints and their direct connections.
# ==========================================
class ServerNetworkTopology:
    def __init__(self):
        self.adj_list = {}

    def add_server(self, server_id):
        if server_id not in self.adj_list:
            self.adj_list[server_id] = []

    def connect_servers(self, s1, s2):
        self.add_server(s1)
        self.add_server(s2)
        self.adj_list[s1].append(s2)
        self.adj_list[s2].append(s1)
        print(f"Network cable routed: {s1} <===> {s2}")

    def display_topology(self):
        print("\nActive Server Topology Graph View:")
        for server, links in self.adj_list.items():
            print(f" Server [{server}] ---> Linked Enclaves: {links}")

print("--- Activity 1: Server Adjacency List Topology ---")
datacenter = ServerNetworkTopology()
datacenter.connect_servers("SRV-Alpha", "SRV-Beta")
datacenter.connect_servers("SRV-Beta", "SRV-Gateway")
datacenter.display_topology()
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Upgrade the Adjacency List into an advanced smart-routing system 
# capable of tracking path weights (latency delays in milliseconds) and node out-degrees.
# ==========================================
class LatencyNetworkGraph:
    def __init__(self):
        self.graph = {}

    def add_link(self, node_a, node_b, latency_ms):
        if node_a not in self.graph: self.graph[node_a] = []
        self.graph[node_a].append((node_b, latency_ms))
        print(f"Link Configured: {node_a} -> {node_b} ({latency_ms}ms latency)")

    def calculate_out_degree_metrics(self, node):
        links = self.graph.get(node, [])
        print(f"Node [{node}] Out-Degree Link Count: {len(links)}")
        return len(links)

print("\n--- Activity 2: Latency-Aware Weighted Adjacency List ---")
backbone = LatencyNetworkGraph()
backbone.add_link("Router-A", "Router-B", 12)
backbone.add_link("Router-A", "Cloud-Edge", 45)
backbone.calculate_out_degree_metrics("Router-A")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a scalable, production-grade Object-Oriented Graph Storage 
# Framework using custom Node/Vertex and Edge objects to maintain a data pipeline graph.
# ==========================================
class Vertex:
    def __init__(self, task_name):
        self.task_name = task_name
        self.dependencies = []

class DataPipelineFramework:
    def __init__(self):
        self.vertices = {}

    def register_task(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def link_dependency(self, upstream, downstream):
        self.register_task(upstream)
        self.register_task(downstream)
        self.vertices[upstream].dependencies.append(self.vertices[downstream])
        print(f"Pipeline flow dependency declared: {upstream} triggers {downstream}")

print("\n--- Activity 3: Object-Oriented Pipeline Framework ---")
pipeline = DataPipelineFramework()
pipeline.link_dependency("Extract_Logs", "Transform_Format")
pipeline.link_dependency("Transform_Format", "Load_Database")
print("-" * 40)