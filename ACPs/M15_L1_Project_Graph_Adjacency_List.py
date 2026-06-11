# Module 15 Lesson 1: After-Class Project
# Project Name: Network Topology Map Structural Adjacency Matrix Builder

class GraphAdjacencyCollection:
    def __init__(self): self.adjacency_map = {}
    def register_edge_node(self, source, destination, bidirectional=True):
        if source not in self.adjacency_map: self.adjacency_map[source] = []
        if destination not in self.adjacency_map: self.adjacency_map[destination] = []
        self.adjacency_map[source].append(destination)
        if bidirectional: self.adjacency_map[destination].append(source)

if __name__ == "__main__":
    graph = GraphAdjacencyCollection()
    graph.register_edge_node("Node_A", "Node_B")
    print(f"Topology maps vector link parameters context tracking values: {graph.adjacency_map}")