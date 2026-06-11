# Module 15 Lesson 4: After-Class Project
# Project Name: Directed Graph Back-Edge Track Validation Infrastructure

def detect_directed_graph_cycle(graph_map):
    visited_set, recursion_stack_set = set(), set()
    def process_node_loop_dfs(node):
        visited_set.add(node)
        recursion_stack_set.add(node)
        for neighbor in graph_map.get(node, []):
            if neighbor not in visited_set:
                if process_node_loop_dfs(neighbor): return True
            elif neighbor in recursion_stack_set: return True
        recursion_stack_set.remove(node)
        return False
        
    for node in graph_map:
        if node not in visited_set:
            if process_node_loop_dfs(node): return True
    return False

if __name__ == "__main__":
    cyclic_graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
    print(f"Deadlock cycle tracked inside structural data graph dependencies? {detect_directed_graph_cycle(cyclic_graph)}")