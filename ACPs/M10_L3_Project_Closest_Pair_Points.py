# Module 10 Lesson 3: After-Class Project
# Project Name: Geometry Engine Closest Pair of Points Divide & Conquer Finder

import math

def calculate_distance_formula(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class SpaceGeometryClosestPairEngine:
    def locate_absolute_closest_distance(self, coordinates_tuple_points_list):
        # Sort values based directly upon initial horizontal grid vector coordinates
        points = sorted(coordinates_tuple_points_list, key=lambda p: p[0])
        return self.__find_closest_recursive_slice(points)

    def __find_closest_recursive_slice(self, sorted_slice):
        n = len(sorted_slice)
        if n <= 3:
            # Bruteforce fallback optimization matrix logic path for baseline boundaries
            min_dist = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    d = calculate_distance_formula(sorted_slice[i], sorted_slice[j])
                    if d < min_dist: min_dist = d
            return min_dist
            
        mid = n // 2
        mid_point = sorted_slice[mid]
        
        dl = self.__find_closest_recursive_slice(sorted_slice[:mid])
        dr = self.__find_closest_recursive_slice(sorted_slice[mid:])
        d_omega = min(dl, dr)
        
        # Build crossing stripe boundary analysis filter arrays zones layout
        stripe_zone = [p for p in sorted_slice if abs(p[0] - mid_point[0]) < d_omega]
        stripe_zone.sort(key=lambda p: p[1])
        
        min_stripe_dist = d_omega
        for i in range(len(stripe_zone)):
            for j in range(i + 1, len(stripe_zone)):
                if (stripe_zone[j][1] - stripe_zone[i][1]) >= min_stripe_dist:
                    break
                d = calculate_distance_formula(stripe_zone[i], stripe_zone[j])
                if d < min_stripe_dist: min_stripe_dist = d
                
        return min_stripe_dist

if __name__ == "__main__":
    engine = SpaceGeometryClosestPairEngine()
    radar_plots = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"Closest Euclidean Distance between radar vector plots coordinate targets: {engine.locate_absolute_closest_distance(radar_plots):.4f}")