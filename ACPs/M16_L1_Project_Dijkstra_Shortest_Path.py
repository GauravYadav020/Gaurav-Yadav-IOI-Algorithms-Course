# Module 16 Lesson 1: After-Class Project
# Project Name: Shortest Route Matrix Path Optimization Engine Using Dijkstra

import heapq

class DijkstraRouteOptimizer:
    def locate_shortest_payouts(self, network_adjacency_map, origin_node_key):
        priority_heap = [(0, origin_node_key)]
        shortest_path_costs_map = {node: float('inf') for node in network_adjacency_map}
        shortest_path_costs_map[origin_node_key] = 0
        
        while priority_heap:
            current_cost, current_node = heapq.heappop(priority_heap)
            if current_cost > shortest_path_costs_map[current_node]: continue
            for neighbor_node, travel_weight in network_adjacency_map.get(current_node, []):
                calculated_cost = current_cost + travel_weight
                if calculated_cost < shortest_path_costs_map[neighbor_node]:
                    shortest_path_costs_map[neighbor_node] = calculated_cost
                    heapq.heappush(priority_heap, (calculated_cost, neighbor_node))
        return shortest_path_costs_map

if __name__ == "__main__":
    optimizer = DijkstraRouteOptimizer()
    net = {"A": [("B", 4), ("C", 2)], "B": [("C", 3), ("D", 23)], "C": [("B", 1), ("D", 5)], "D": []}
    print(f"Calculated shortest paths intervals profiles values mapping: {optimizer.locate_shortest_payouts(net, 'A')}")