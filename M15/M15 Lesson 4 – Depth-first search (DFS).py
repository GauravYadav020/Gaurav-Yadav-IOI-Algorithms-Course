# LESSON NAME: M15 Lesson 4 – Depth-first search (DFS)

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a standard recursive Depth-First Search algorithm to 
# trace out the deeper branches of an active file system registry tree directory layout.
# ==========================================
def run_recursive_dfs_trace(graph, current_node, visited_set=None):
    if visited_set is None:
        visited_set = set()
        
    visited_set.add(current_node)
    print(f" -> Tracing Directory Cluster Depth Node: {current_node}")
    
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited_set:
            run_recursive_dfs_trace(graph, neighbor, visited_set)
    return visited_set

print("--- Activity 1: File Directory Depth-First Trace ---")
directory_tree = {
    "C:/Root": ["Users", "Program Files"],
    "Users": ["AliceDocs", "GuestProfile"],
    "Program Files": ["Python311"],
    "AliceDocs": [], "GuestProfile": [], "Python311": []
}
run_recursive_dfs_trace(directory_tree, "C:/Root")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Write an enterprise compiler validation tool using DFS that detects 
# cyclic import dependency lockups within project software module compilation files.
# ==========================================
class ProjectDependencyCycleDetector:
    def __init__(self, modules_graph):
        self.graph = modules_graph

    def has_cyclic_deadlock(self, node, visited, recursion_stack):
        visited.add(node)
        recursion_stack.add(node)
        
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                if self.has_cyclic_deadlock(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                print(f"❌ DEADLOCK LINE COLLISION DETECTED! Module loop point: {node} -> {neighbor}")
                return True
                
        recursion_stack.remove(node)
        return False

print("\n--- Activity 2: Code Compilation Dependency Inspector ---")
broken_source_modules = {
    "AuthModule": ["DataLayer"],
    "DataLayer": ["LoggingEngine"],
    "LoggingEngine": ["AuthModule"], # Cyclic dependencies loop injection
}
detector = ProjectDependencyCycleDetector(broken_source_modules)
is_broken = False
visited, rec_stack = set(), set()
for mod in broken_source_modules:
    if mod not in visited:
        if detector.has_cyclic_deadlock(mod, visited, rec_stack):
            is_broken = True
            break
print(f"Is compilation build tree corrupted? {is_broken}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Implement a maze pathfinding solver engine that computes the 
# exit route path coordinates from an origin gate through deep geometric validation pipelines.
# ==========================================
class MazeSolverEngineDFS:
    def __init__(self, maze_matrix):
        self.maze = maze_matrix
        self.rows = len(maze_matrix)
        self.cols = len(maze_matrix[0])

    def solve(self, curr_r, curr_c, dest_r, dest_c, path=None, visited=None):
        if path is None: path = []
        if visited is None: visited = set()
            
        if (curr_r, curr_c) == (dest_r, dest_c):
            path.append((curr_r, curr_c))
            return path
            
        visited.add((curr_r, curr_c))
        path.append((curr_r, curr_c))
        
        # Grid movement options: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.maze[nr][nc] == 1 and (nr, nc) not in visited: # 1 means valid walkable open path lane
                    final_route = self.solve(nr, nc, dest_r, dest_c, path.copy(), visited.copy())
                    if final_route: return final_route
        return None

print("\n--- Activity 3: Maze Grid Route Solver Engine ---")
# 1 = Walkable track, 0 = Concrete Wall Blockade barricade barrier
maze_grid = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]
solver = MazeSolverEngineDFS(maze_grid)
solution_route = solver.solve(0, 0, 2, 3)
print(f"Calculated exit path coordinates chain: {solution_route}")
print("-" * 40)