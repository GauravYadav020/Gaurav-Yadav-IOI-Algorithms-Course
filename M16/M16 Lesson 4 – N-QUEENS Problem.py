# LESSON NAME: M16 Lesson 4 – N-QUEENS Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic 4-Queens board solver using recursive backtracking 
# and a safe placement validation method to isolate queen items without collisions.
# ==========================================
class NQueensMiniSolver:
    def __init__(self, size=4):
        self.n = size
        self.board = [[0] * size for _ in range(size)]

    def _is_safe(self, row, col):
        # Check horizontal axis lane row
        for i in range(col):
            if self.board[row][i] == 1: return False
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1: return False
        # Check lower left diagonal
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1: return False
        return True

    def solve_board_step(self, col=0):
        if col >= self.n: return True
        for i in range(self.n):
            if self._is_safe(i, col):
                self.board[i][col] = 1
                if self.solve_board_step(col + 1): return True
                self.board[i][col] = 0 # Backtrack step execution tracking line
        return False

print("--- Activity 1: Core 4-Queens Backtracking Board ---")
solver = NQueensMiniSolver(4)
if solver.solve_board_step():
    for row_line in solver.board: print(row_line)
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create a comprehensive chess placement validator engine that returns 
# all valid board solution layouts for custom dimensions, counting overall steps.
# ==========================================
class AnalyticalNQueensEngine:
    def __init__(self, dimensions):
        self.n = dimensions
        self.solutions_count = 0
        self.evaluation_steps = 0

    def find_all_board_options(self):
        board = [[0] * self.n for _ in range(self.n)]
        self._backtrack_search(board, 0)
        return self.solutions_count

    def _is_valid(self, board, r, c):
        self.evaluation_steps += 1
        for i in range(c):
            if board[r][i] == 1: return False
        for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
            if board[i][j] == 1: return False
        for i, j in zip(range(r, self.n), range(c, -1, -1)):
            if board[i][j] == 1: return False
        return True

    def _backtrack_search(self, board, col):
        if col == self.n:
            self.solutions_count += 1
            return
        for i in range(self.n):
            if self._is_valid(board, i, col):
                board[i][col] = 1
                self._backtrack_search(board, col + 1)
                board[i][col] = 0

print("\n--- Activity 2: Structural All-Solutions Counter Engine ---")
engine = AnalyticalNQueensEngine(5)
total_ans = engine.find_all_board_options()
print(f"Total separate valid placement variations found for grid sizing 5: {total_ans}")
print(f"Total algorithmic search steps verified: {engine.evaluation_steps}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Write an ultra-fast N-Queens system that uses optimized bitwise operations 
# (Bitmasking) to track column and diagonal conflicts at production-grade speeds.
# ==========================================
class BitmaskedNQueensOptimizer:
    def __init__(self, grid_size):
        self.n = grid_size
        self.count = 0

    def calculate_fast_solutions(self):
        # bitmask boundaries rule sets mapping configuration
        done_mask = (1 << self.n) - 1
        self._bit_backtrack(0, 0, 0, done_mask)
        return self.count

    def _bit_backtrack(self, col_mask, ld_mask, rd_mask, done_mask):
        if col_mask == done_mask:
            self.count += 1
            return
        
        # Get all valid open spaces in the current row using bitwise operations
        open_slots = ~(col_mask | ld_mask | rd_mask) & done_mask
        while open_slots:
            lowest_bit = open_slots & -open_slots
            open_slots -= lowest_bit
            self._bit_backtrack(
                col_mask | lowest_bit,
                (ld_mask | lowest_bit) << 1,
                (rd_mask | lowest_bit) >> 1,
                done_mask
            )

print("\n--- Activity 3: Bitmasked High-Performance Placement Sorter ---")
bit_optimizer = BitmaskedNQueensOptimizer(8)
print(f"Total calculated placement combinations for standard 8x8 chessboard: {bit_optimizer.calculate_fast_solutions()}")
print("-" * 40)