# Module 16 Lesson 4: After-Class Project
# Project Name: Kruskals Path Disjoint Set Forest Union-Find Engine

class DisjointSetForestStructure:
    def __init__(self, size): self.parent = list(range(size))
    def find_root(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find_root(self.parent[i]) # Path compression mechanism alignment rules active
        return self.parent[i]
    def union_nodes(self, i, j):
        root_i, root_j = self.find_root(i), self.find_root(j)
        if root_i != root_j: self.parent[root_i] = root_j; return True
        return False

def compute_kruskals_mst_cost(total_nodes, edge_list_tuples):
    edge_list_tuples.sort(key=lambda edge: edge[2])
    dsf = DisjointSetForestStructure(total_nodes)
    mst_accumulated_weight, tracking_count = 0, 0
    for u, v, weight in edge_list_tuples:
        if dsf.union_nodes(u, v):
            mst_accumulated_weight += weight
            tracking_count += 1
            if tracking_count == total_nodes - 1: break
    return mst_accumulated_weight

if __name__ == "__main__":
    edges_pool = [(0, 1, 10), (0, 2, 6), (1, 2, 5)]
    print(f"Kruskals structural graph processing results optimization value: {compute_kruskals_mst_cost(3, edges_pool)}")