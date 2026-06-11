# LESSON NAME: M17 Lesson 1 – Rat in a Maze problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic structural validator using recursive backtracking 
# that checks if a path exists from the top-left corner to the bottom-right corner of a binary maze.
# ==========================================
class BasicMazeValidator:
    def __init__(self, maze):
        self.maze = maze
        self.N = len(maze)

    def is_safe(self, x, y):
        # Check boundaries and if the block is open (1)
        return 0 <= x < self.N and 0 <= y < self.N and self.maze[x][y] == 1

    def solve_maze(self, x=0, y=0):
        if x == self.N - 1 and y == self.N - 1:
            return True
            
        if self.is_safe(x, y):
            # Move Down
            if self.solve_maze(x + 1, y): return True
            # Move Right
            if self.solve_maze(x, y + 1): return True
            
        return False

print("--- Activity 1: Simple Maze Structural Validator ---")
simple_maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
validator = BasicMazeValidator(simple_maze)
print(f"Is there a valid path through the maze? {validator.solve_maze()}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a comprehensive backtracking solver that prints out 
# the explicit path matrix showing the route the rat took (marked with 1s).
# ==========================================
class VisualMazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.N = len(maze)
        self.sol_matrix = [[0] * self.N for _ in range(self.N)]

    def _is_safe(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.maze[x][y] == 1

    def solve_util(self, x, y):
        if x == self.N - 1 and y == self.N - 1:
            self.sol_matrix[x][y] = 1
            return True

        if self._is_safe(x, y):
            self.sol_matrix[x][y] = 1
            
            # Explore Downward Move
            if self.solve_util(x + 1, y): return True
            # Explore Rightward Move
            if self.solve_util(x, y + 1): return True
            
            # Backtrack step execution tracking line
            self.sol_matrix[x][y] = 0
        return False

    def display_solution(self):
        if self.solve_util(0, 0):
            print("Calculated Path Matrix Configuration:")
            for row in self.sol_matrix: print(row)
        else:
            print("No viable paths discovered inside layout parameters.")

print("\n--- Activity 2: Visual Route Matrix Solver ---")
complex_maze = [
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
solver = VisualMazeSolver(complex_maze)
solver.display_solution()
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an ultra-flexible maze runner engine capable of exploring all 
# four directions (Up, Down, Left, Right) safely while avoiding cyclic infinite loops.
# ==========================================
class OmnidirectionalMazeRunner:
    def __init__(self, grid):
        self.grid = grid
        self.N = len(grid)
        self.visited = [[False] * self.N for _ in range(self.N)]

    def search_all_paths(self, r=0, c=0, current_path=""):
        if r == self.N - 1 and c == self.N - 1:
            print(f" -> Found complete exit trajectory sequence: {current_path}")
            return

        # Setup boundary safety and state validation guidelines
        if 0 <= r < self.N and 0 <= c < self.N and self.grid[r][c] == 1 and not self.visited[r][c]:
            self.visited[r][c] = True
            
            # Move Down (D), Left (L), Right (R), Up (U)
            self.search_all_paths(r + 1, c, current_path + "D")
            self.search_all_paths(r, c - 1, current_path + "L")
            self.search_all_paths(r, c + 1, current_path + "R")
            self.search_all_paths(r - 1, c, current_path + "U")
            
            # Backtrack clean step histories
            self.visited[r][c] = False

print("\n--- Activity 3: Omnidirectional Cycle-Safe Maze Runner ---")
open_grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
runner = OmnidirectionalMazeRunner(open_grid)
runner.search_all_paths()
print("-" * 40)