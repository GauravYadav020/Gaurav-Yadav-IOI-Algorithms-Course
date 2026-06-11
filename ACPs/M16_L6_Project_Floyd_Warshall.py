# Module 16 Lesson 6: After-Class Project
# Project Name: Floyd-Warshall All-Pairs Shortest Path Matrix Engine

def execute_floyd_warshall_matrix(graph_matrix_grid):
    n = len(graph_matrix_grid)
    distance_matrix = [row[:] for row in graph_matrix_grid]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    return distance_matrix

if __name__ == "__main__":
    inf = float('inf')
    matrix = [[0, 3, inf, 7], [8, 0, 2, inf], [5, inf, 0, 1], [2, inf, inf, 0]]
    print(f"All-pairs paths short calculation rows matrix output tracker: {execute_floyd_warshall_matrix(matrix)[0]}")