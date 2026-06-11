# LESSON NAME: M16 Lesson 5 – Sudoku Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic 9x9 Sudoku validation engine that checks row, 
# column, and local 3x3 subgrid safety constraints before placing a number.
# ==========================================
class SudokuBasicValidator:
    def __init__(self, puzzle_board):
        self.board = puzzle_board

    def is_placement_safe(self, row, col, num):
        # Validate horizontal constraint guidelines
        if num in self.board[row]: return False
        # Validate vertical layout line constraints
        if num in [self.board[i][col] for i in range(9)]: return False
        
        # Validate targeted localized quadrant box block bounds
        box_r, box_c = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_r + i][box_c + j] == num: return False
        return True

print("--- Activity 1: Core Constraint Validation Logic ---")
mock_puzzle = [[0]*9 for _ in range(9)]
mock_puzzle[0][0] = 5
validator = SudokuBasicValidator(mock_puzzle)
print(f"Is slot target safe for insertion parameter value (5) at row 0, col 1? {validator.is_placement_safe(0, 1, 5)}")
print(f"Is slot target safe for insertion parameter value (9) at row 0, col 1? {validator.is_placement_safe(0, 1, 9)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build a fully functional 9x9 Sudoku solver using recursive 
# backtracking that solves puzzle instances and outputs the completed board array.
# ==========================================
class ClassicSudokuSolver:
    def __init__(self, matrix_board):
        self.board = matrix_board

    def _find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0: return i, j
        return None

    def _safe(self, r, c, val):
        if val in self.board[r]: return False
        if val in [self.board[i][c] for i in range(9)]: return False
        br, bc = (r // 3) * 3, (c // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[br+i][bc+j] == val: return False
        return True

    def execute_solving_sequence(self):
        empty_slot = self._find_empty()
        if not empty_slot: return True # Solved completely
        row, col = empty_slot

        for choice in range(1, 10):
            if self._safe(row, col, choice):
                self.board[row][col] = choice
                if self.execute_solving_sequence(): return True
                self.board[row][col] = 0 # Undo choice and backtrack
        return False

print("\n--- Activity 2: Backtracking Grid Solution Sorter ---")
raw_sudoku = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]
engine = ClassicSudokuSolver(raw_sudoku)
if engine.execute_solving_sequence():
    print("Successfully compiled sudoku grid results:")
    print(engine.board[0])
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Create an advanced, high-performance Sudoku matrix solver that uses 
# the Minimum Remaining Values (MRV) heuristic to prioritize grids with fewer remaining choices.
# ==========================================
class HeuristicSudokuSolver:
    def __init__(self, board):
        self.board = board

    def get_mrv_cell(self):
        # Heuristic optimization analyzer tool choice tracker logic
        min_choices = 10
        best_cell = None
        
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    valid_options_count = sum(1 for val in range(1, 10) if self._is_valid(r, c, val))
                    if valid_options_count < min_choices:
                        min_choices = valid_options_count
                        best_cell = (r, c)
        return best_cell

    def _is_valid(self, r, c, val):
        if val in self.board[r]: return False
        if val in [self.board[i][c] for i in range(9)]: return False
        br, bc = (r // 3) * 3, (c // 3) * 3
        return not any(self.board[br+i][bc+j] == val for i in range(3) for j in range(3))

    def solve_with_mrv(self):
        cell = self.get_mrv_cell()
        if not cell: return True
        r, c = cell

        for val in range(1, 10):
            if self._is_valid(r, c, val):
                self.board[r][c] = val
                if self.solve_with_mrv(): return True
                self.board[r][c] = 0
        return False

print("\n--- Activity 3: High-Performance Heuristic MRV Sudoku Solver ---")
mrv_puzzle = [list(row) for row in raw_sudoku] # Copy puzzle data layout
mrv_engine = HeuristicSudokuSolver(mrv_puzzle)
print(f"Heuristic pipeline status execution solver resolution state: {mrv_engine.solve_with_mrv()}")
print("-" * 40)