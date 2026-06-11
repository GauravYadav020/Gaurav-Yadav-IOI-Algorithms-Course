# LESSON NAME: M15 Lesson 6 – Problems related to graphs

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write an algorithmic graph engine that counts the exact total 
# number of isolated cluster subnet islands inside an enterprise hosting topology map.
# ==========================================
class IsolatedSubnetIslandCounter:
    def count_islands(self, adjacency_grid):
        visited = set()
        island_count = 0
        
        def run_cluster_drain_dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                for peer in adjacency_grid.get(curr, []):
                    if peer not in visited:
                        visited.add(peer)
                        stack.append(peer)

        for center in adjacency_grid:
            if center not in visited:
                island_count += 1
                visited.add(center)
                run_cluster_drain_dfs(center)
                
        return island_count

print("--- Activity 1: Isolated Subnet Cluster Island Counter ---")
hosting_topology = {
    "Server-A": ["Server-B"], "Server-B": ["Server-A"], # Island Unit 1
    "Server-C": ["Server-D"], "Server-D": ["Server-C"], # Island Unit 2
    "LegacyTerminal": []                                # Island Unit 3
}
counter = IsolatedSubnetIslandCounter()
print(f"Total isolated cloud network subnets discovered: {counter.count_islands(hosting_topology)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a bipartite infrastructure check utility to determine 
# if database storage engines can be cleanly divided into a functional master-replica topology.
# ==========================================
from collections import deque

def check_valid_bipartite_split(graph):
    color_map = {} # Maps node to group flags (0 or 1)
    
    for vertex in graph:
        if vertex not in color_map:
            queue = deque([vertex])
            color_map[vertex] = 0
            
            while queue:
                curr = queue.popleft()
                for peer in graph.get(curr, []):
                    if peer not in color_map:
                        color_map[peer] = 1 - color_map[curr]
                        queue.append(peer)
                    elif color_map[peer] == color_map[curr]:
                        print(f" -> Structural conflict mismatch found between: {curr} and {peer}")
                        return False
    return True

print("\n--- Activity 2: Master-Replica Split Validator ---")
valid_split_cluster = {
    "DB-Node-1": ["Replica-A", "Replica-B"],
    "Replica-A": ["DB-Node-1"], "Replica-B": ["DB-Node-1"]
}
invalid_split_cluster = {
    "DB-Node-1": ["DB-Node-2", "Replica-A"],
    "DB-Node-2": ["DB-Node-1", "Replica-A"], # Internal link violates bipartite rules
    "Replica-A": ["DB-Node-1", "DB-Node-2"]
}
print(f"Can cluster split into independent rows safely? {check_valid_bipartite_split(valid_split_cluster)}")
print(f"Can complex cluster split safely? {check_valid_bipartite_split(invalid_split_cluster)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a high-performance network routing analytical framework 
# that computes topological sort layout lines for complex task execution sequencing.
# ==========================================
class SchedulingSequenceEngine:
    def __init__(self, tasks_dependencies_graph):
        self.graph = tasks_dependencies_graph

    def compute_linear_schedule(self):
        visited = set()
        permanent_stack_frame = []
        
        def dfs_topological_sort(node):
            visited.add(node)
            for structural_peer in self.graph.get(node, []):
                if structural_peer not in visited:
                    dfs_topological_sort(structural_peer)
            permanent_stack_frame.append(node)

        for job in list(self.graph.keys()):
            if job not in visited:
                dfs_topological_sort(job)
                
        return permanent_stack_frame[::-1]

print("\n--- Activity 3: Topological Compilation Ordering Engine ---")
build_execution_pipeline = {
    "Compile_Kernel": ["Link_Drivers", "Load_Core_Modules"],
    "Link_Drivers": ["Initialize_System_UI"],
    "Load_Core_Modules": ["Initialize_System_UI"],
    "Initialize_System_UI": []
}
scheduler = SchedulingSequenceEngine(build_execution_pipeline)
ordered_flow = scheduler.compute_linear_schedule()
print("Optimized Linear Task Deployment Ordering Blueprint Sequence:")
for order_idx, job_id in enumerate(ordered_flow, start=1):
    print(f" Phase Steps [{order_idx}] ---> Executing Job Component Task Reference: {job_id}")
print("-" * 40)