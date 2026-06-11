# Module 15 Lesson 2: After-Class Project
# Project Name: Breadth First Search Graph Topology Level Discovery Engine

from collections import deque

def traverse_bfs_graph(graph_dictionary, starting_node_key):
    visited_nodes_set, output_sequence = set([starting_node_key]), []
    queue = deque([starting_node_key])
    while queue:
        curr = queue.popleft()
        output_sequence.append(curr)
        for neighbor in graph_dictionary.get(curr, []):
            if neighbor not in visited_nodes_set:
                visited_nodes_set.add(neighbor)
                queue.append(neighbor)
    return output_sequence

if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    print(f"BFS Path Trace Discovery Array Coordinates Map: {traverse_bfs_graph(g, 'A')}")