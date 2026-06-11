# Module 15 Lesson 3: After-Class Project
# Project Name: Depth First Search Stack Graph Recursive Deep Traversal Engine

def traverse_dfs_graph(graph_dictionary, starting_node_key):
    visited, output_sequence = set(), []
    def recursive_dfs_step(node):
        visited.add(node)
        output_sequence.append(node)
        for neighbor in graph_dictionary.get(node, []):
            if neighbor not in visited: recursive_dfs_step(neighbor)
    recursive_dfs_step(starting_node_key)
    return output_sequence

if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    print(f"DFS Recursive Trace Coordinates Linear Sequence Layout: {traverse_dfs_graph(g, 'A')}")