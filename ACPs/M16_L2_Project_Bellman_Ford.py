# Module 16 Lesson 2: After-Class Project
# Project Name: Bellman-Ford Negative Cycle Routing Protection Engine

def execute_bellman_ford_protection(vertices_count, edges_triplets_list, origin_node):
    distances = [float('inf')] * vertices_count
    distances[origin_node] = 0
    
    for _ in range(vertices_count - 1):
        for u, v, w in edges_triplets_list:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                
    for u, v, w in edges_triplets_list:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return "CRITICAL_EXCEPTION: Negative arbitrage threat vector signature tracking loop confirmed."
    return distances

if __name__ == "__main__":
    edges = [(0, 1, -1), (1, 2, -2), (2, 0, -3)] # Cyclic negative arbitrage generation rules active
    print(execute_bellman_ford_protection(3, edges, 0))