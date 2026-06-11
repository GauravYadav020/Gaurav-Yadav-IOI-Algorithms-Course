# Module 5 Lesson 1: After-Class Project
# Project Name: Modular CAD Graphics Engine Geometric Core Computations Library

import math

def calculate_euclidean_distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_circle_area_precision(radius):
    if radius < 0: raise ValueError("Scalar error: Radius cannot be negative.")
    return math.pi * (radius ** 2)

def calculate_polygon_perimeter(coordinate_tuples_points_list):
    perimeter_accumulator = 0.0
    num_points = len(coordinate_tuples_points_list)
    for idx in range(num_points):
        p1 = coordinate_tuples_points_list[idx]
        p2 = coordinate_tuples_points_list[(idx + 1) % num_points]
        perimeter_accumulator += calculate_euclidean_distance_2d(p1[0], p1[1], p2[0], p2[1])
    return perimeter_accumulator

if __name__ == "__main__":
    triangle = [(0,0), (4,0), (4,3)]
    print(f"Computed CAD Boundary Vector Perimeter Dimension: {calculate_polygon_perimeter(triangle)}")