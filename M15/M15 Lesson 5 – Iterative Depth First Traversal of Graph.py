# LESSON NAME: M15 Lesson 5 – Iterative Depth First Traversal of Graph

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement an Iterative DFS traversal framework from scratch 
# utilizing a manual loop control Stack structure to log asset node sequence footprints.
# ==========================================
def run_iterative_dfs_traversal(graph, root_node):
    visited = set()
    stack = [root_node]
    traversal_path = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_path.append(vertex)
            # Push non-visited neighbors onto the tracking sequence stack
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_path

print("--- Activity 1: Manual Stack-Driven Iterative DFS ---")
infrastructure_tree = {
    "Hub-Alpha": ["Switch-B", "Switch-C"],
    "Switch-B": ["Terminal-01", "Terminal-02"],
    "Switch-C": ["Terminal-03"],
    "Terminal-01": [], "Terminal-02": [], "Terminal-03": []
}
print(f"Iterative execution tracking logs: {run_iterative_dfs_traversal(infrastructure_tree, 'Hub-Alpha')}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create a corporate security audit network scanner tool that 
# processes deep system endpoints iteratively to avoid potential Call-Stack Memory overflow.
# ==========================================
class MemorySafeSecurityScanner:
    def __init__(self, network_endpoints_map):
        self.network = network_endpoints_map

    def perform_isolated_vulnerability_scan(self, startup_node):
        visited_log = set()
        execution_stack = [startup_node]
        scanned_nodes_counter = 0
        
        print(f"Initiating Iterative Memory-Isolated Node Security Scan from: {startup_node}")
        while execution_stack:
            target = execution_stack.pop()
            if target not in visited_log:
                visited_log.add(target)
                scanned_nodes_counter += 1
                print(f" -> Auditing firmware patch version definitions inside unit: {target}")
                for peer in self.network.get(target, []):
                    if peer not in visited_log:
                        execution_stack.append(peer)
                        
        return scanned_nodes_counter

print("\n--- Activity 2: Deep Heap-Allocated Infrastructure Scanner ---")
enterprise_nodes = {
    "CoreRouter": ["EdgeEnclave_1", "EdgeEnclave_2"],
    "EdgeEnclave_1": ["Workstation_A", "Workstation_B"],
    "EdgeEnclave_2": ["SecureBackupVault"],
    "Workstation_A": [], "Workstation_B": [], "SecureBackupVault": []
}
scanner = MemorySafeSecurityScanner(enterprise_nodes)
total_audited = scanner.perform_isolated_vulnerability_scan("CoreRouter")
print(f"Total isolated node assets safely checked: {total_audited}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an advanced analytics tracking router engine that traces path 
# paths back from terminal sub-component units to original source parent origins iteratively.
# ==========================================
class AncestryPathTraceEngine:
    def __init__(self, trace_graph):
        self.graph = trace_graph

    def build_parental_trace_map(self, root_node, target_node):
        parent_map = {root_node: None}
        stack = [root_node]
        
        while stack:
            current = stack.pop()
            if current == target_node:
                break
            for child in self.graph.get(current, []):
                if child not in parent_map:
                    parent_map[child] = current
                    stack.append(child)
                    
        # Reconstruct path back from target node to root node source position
        path = []
        step = target_node
        while step is not None:
            path.append(step)
            step = parent_map.get(step)
        return path[::-1] if target_node in parent_map else []

print("\n--- Activity 3: Ancestry Path-Back Trace Controller ---")
blueprint_dependencies = {
    "Engine-Assembly": ["Piston-Subassembly", "Fuel-Line-Subassembly"],
    "Piston-Subassembly": ["Valves-Component", "Rods-Component"],
    "Fuel-Line-Subassembly": [], "Valves-Component": [], "Rods-Component": []
}
tracer = AncestryPathTraceEngine(blueprint_dependencies)
route_to_part = tracer.build_parental_trace_map("Engine-Assembly", "Rods-Component")
print(f"Trace tracking path line generated: {route_to_part}")
print("-" * 40)