# Module 16 Lesson 5: After-Class Project
# Project Name: Kahn Dependency Resolution Framework Topological Sort

from collections import deque

def compute_topological_sort_kahns(vertices_count, adjacency_graph_map):
    in_degrees = {node: 0 for node in range(vertices_count)}
    for u in adjacency_graph_map:
        for v in adjacency_graph_map[u]: in_degrees[v] += 1
        
    zero_in_degree_queue = deque([node for node in in_degrees if in_degrees[node] == 0])
    ordered_execution_sequence = []
    
    while zero_in_degree_queue:
        curr = zero_in_degree_queue.popleft()
        ordered_execution_sequence.append(curr)
        for neighbor in adjacency_graph_map.get(curr, []):
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0: zero_in_degree_queue.append(neighbor)
            
    if len(ordered_execution_sequence) != vertices_count: return [] # Cycle dependency fault block triggered
    return ordered_execution_sequence

if __name__ == "__main__":
    adj = {0: [2], 1: [2], 2: [3], 3: []}
    print(f"Linearized build automation step sequence tracking: {compute_topological_sort_kahns(4, adj)}")