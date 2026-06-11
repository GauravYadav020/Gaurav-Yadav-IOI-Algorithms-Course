# LESSON NAME: M19 Lesson 5 – Matrix Chain Multiplication

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic recursive partition finder that computes 
# the minimal computational operations cost to multiply a sequence of dimensional matrices.
# ==========================================
def recursive_matrix_chain_cost(dimensions, i, j):
    if i == j: return 0
    
    min_computations = float('inf')
    
    # Partition loop separating sequence bounds chunks
    for k in range(i, j):
        current_ops_cost = (recursive_matrix_chain_cost(dimensions, i, k) +
                            recursive_matrix_chain_cost(dimensions, k + 1, j) +
                            dimensions[i - 1] * dimensions[k] * dimensions[j])
        
        if current_ops_cost < min_computations:
            min_computations = current_ops_cost
            
    return min_computations

print("--- Activity 1: Recursive Matrix Partition Cost ---")
matrix_dims = [10, 20, 30, 40]
print(f"Minimum operations needed: {recursive_matrix_chain_cost(matrix_dims, 1, len(matrix_dims) - 1)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a 2D Tabulation array framework to solve the Matrix Chain Multiplication 
# problem, optimizing calculation performance and checking step constraints.
# ==========================================
class MatrixChainTabulationCompiler:
    def compile_optimal_multiplication_table(self, dims_arr):
        n = len(dims_arr) - 1
        dp_matrix = [[0] * (n + 1) for _ in range(n + 1)]
        
        # L represents the dynamic sliding length of the matrix chain scale window
        for L in range(2, n + 1):
            for i in range(1, n - L + 2):
                j = i + L - 1
                dp_matrix[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp_matrix[i][k] + dp_matrix[k + 1][j] + dims_arr[i - 1] * dims_arr[k] * dims_arr[j]
                    if cost < dp_matrix[i][j]:
                        dp_matrix[i][j] = cost
                        
        return dp_matrix[1][n]

print("\n--- Activity 2: 2D Matrix Chain Tabulation Grid ---")
compiler = MatrixChainTabulationCompiler()
test_dims = [40, 20, 30, 10, 30]
print(f"Optimal dynamic computation expense result: {compiler.compile_optimal_multiplication_table(test_dims)} operations")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an advanced matrix compiler system that records structural footprints 
# and tracks data processing duration metrics across complex matrix sequences.
# ==========================================
import time
import sys

def profile_matrix_pipeline_footprint():
    synthetic_dims = [10, 20, 30, 40, 50, 60, 70]
    
    t_start = time.perf_counter()
    res_cost = MatrixChainTabulationCompiler().compile_optimal_multiplication_table(synthetic_dims)
    duration = (time.perf_counter() - t_start) * 1000
    
    print("Matrix Processing Framework Profiler Evaluation:")
    print(f" * Computed Operations Cost Result: {res_cost}")
    print(f" * Array Element Data Struct Footprint Allocation: {sys.getsizeof(synthetic_dims)} bytes")
    print(f" * Total Compiler Parsing Evaluation Time: {duration:.4f} ms")

print("\n--- Activity 3: High-Performance Matrix Pipeline Profiler ---")
profile_matrix_pipeline_footprint()
print("-" * 40)