# LESSON NAME: M16 Lesson 6 – Problems with backtracking

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a localized target-sum compiler using backtracking 
# to find exact numeric matches inside an array database package.
# ==========================================
def find_target_sum_subsets(numbers_list, target_value, index=0, current_combination=None, solutions_archive=None):
    if current_combination is None: current_combination = []
    if solutions_archive is None: solutions_archive = []

    if target_value == 0:
        solutions_archive.append(list(current_combination))
        return solutions_archive
    if target_value < 0 or index >= len(numbers_list):
        return solutions_archive

    # Option 1: Include current element in potential tracking combination row
    current_combination.append(numbers_list[index])
    find_target_sum_subsets(numbers_list, target_value - numbers_list[index], index + 1, current_combination, solutions_archive)
    
    # Option 2: Exclude current element and backtrack step parameters execution
    current_combination.pop()
    find_target_sum_subsets(numbers_list, target_value, index + 1, current_combination, solutions_archive)
    
    return solutions_archive

print("--- Activity 1: Target-Sum Subset Matcher ---")
dataset = [10, 7, 5, 18, 12, 20]
req_sum = 35
print(f"Valid subsets adding up exactly to {req_sum}: {find_target_sum_subsets(dataset, req_sum)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement an $M$-Coloring graph verification utility that uses backtracking 
# to ensure adjacent interconnected map boundary segments do not share matching colors.
# ==========================================
class MapColoringBacktracker:
    def __init__(self, nodes_count, colors_limit):
        self.V = nodes_count
        self.m = colors_limit
        self.graph = [[0] * nodes_count for _ in range(nodes_count)]
        self.assigned_colors = [0] * nodes_count

    def _is_safe_color(self, v, c, color_assignment):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color_assignment[i] == c: return False
        return True

    def solve_map_coloring(self, v_index=0):
        if v_index == self.V: return True

        for c_choice in range(1, self.m + 1):
            if self._is_safe_color(v_index, c_choice, self.assigned_colors):
                self.assigned_colors[v_index] = c_choice
                if self.solve_map_coloring(v_index + 1): return True
                self.assigned_colors[v_index] = 0 # Backtrack tracking state cleanup
        return False

print("\n--- Activity 2: M-Coloring Graph Map Optimizer ---")
mapper = MapColoringBacktracker(nodes_count=4, colors_limit=3)
mapper.graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
print(f"Can map boundaries resolve colors successfully? {mapper.solve_map_coloring()}")
print(f"Assigned color routing maps distribution sequence index list: {mapper.assigned_colors}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a production-grade Hamiltonian Path compiler tool designed 
# to trace a continuous linear journey that touches every node in the graph exactly once.
# ==========================================
class HamiltonianPathCompiler:
    def __init__(self, matrix_map):
        self.graph = matrix_map
        self.V = len(matrix_map)

    def _is_valid_move(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0: return False
        if v in path: return False
        return True

    def find_hamiltonian_cycle(self):
        path = [-1] * self.V
        path[0] = 0 # Set starting pivot master position context
        if not self._backtrack_path_seek(path, 1):
            print("No complete continuous Hamiltonian path trajectory sequence exists.")
            return []
        return path

    def _backtrack_path_seek(self, path, pos):
        if pos == self.V:
            # Confirm path connects back to origin to form a complete structural loop cycle
            return self.graph[path[pos - 1]][path[0]] == 1

        for v_choice in range(1, self.V):
            if self._is_valid_move(v_choice, pos, path):
                path[pos] = v_choice
                if self._backtrack_path_seek(path, pos + 1): return True
                path[pos] = -1
        return False

print("\n--- Activity 3: Hamiltonian Path Sequence Compiler ---")
network_grid_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
compiler = HamiltonianPathCompiler(network_grid_matrix)
print(f"Calculated complete linear sequence cycle index route path: {compiler.find_hamiltonian_cycle()}")
print("-" * 40)