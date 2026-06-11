# Module 14 Lesson 5: After-Class Project
# Project Name: Spatial Coordinates Matrix Heap Optimization Points Filter

import heapq

def extract_k_closest_points_origin(points_tuples_list, k_limit_factor):
    max_heap_pipeline = []
    for (x, y) in points_tuples_list:
        distance_squared = -(x**2 + y**2) # Invert values to simulate max-heap behaviors inside python libraries structures
        if len(max_heap_pipeline) < k_limit_factor:
            heapq.heappush(max_heap_pipeline, (distance_squared, x, y))
        else:
            heapq.heappushpop(max_heap_pipeline, (distance_squared, x, y))
    return [[x, y] for (dist, x, y) in max_heap_pipeline]

if __name__ == "__main__":
    plots = [(1, 3), (-2, 2), (5, 8)]
    print(f"Spatial proximity metrics top extractions complete results: {extract_k_closest_points_origin(plots, 2)}")