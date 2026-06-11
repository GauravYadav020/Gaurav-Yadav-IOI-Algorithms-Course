# Module 16 Lesson 3: After-Class Project
# Project Name: Prims Greedy Minimum Spanning Tree Infrastructure Engine

import heapq

def compute_prims_mst_cost(graph_network_map, starting_node_key):
    visited_set, heap_pipeline = set(), [(0, starting_node_key)]
    accumulated_mst_weight = 0
    while heap_pipeline:
        cost, curr = heapq.heappop(heap_pipeline)
        if curr in visited_set: continue
        visited_set.add(curr)
        accumulated_mst_weight += cost
        for neighbor, weight in graph_network_map.get(curr, []):
            if neighbor not in visited_set: heapq.heappush(heap_pipeline, (weight, neighbor))
    return accumulated_mst_weight

if __name__ == "__main__":
    g = {"A": [("B", 2), ("C", 3)], "B": [("A", 2), ("C", 1)], "C": [("A", 3), ("B", 1)]}
    print(f"Optimized backbone infrastructure grid implementation weight value: {compute_prims_mst_cost(g, 'A')}")