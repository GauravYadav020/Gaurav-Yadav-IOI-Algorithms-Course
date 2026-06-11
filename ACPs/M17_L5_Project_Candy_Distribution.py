# Module 17 Lesson 5: After-Class Project
# Project Name: Minimum Resource Allocation Performance Rank Optimizer

def calculate_minimum_candy_distribution(ratings_scores_list):
    n = len(ratings_scores_list)
    allocations_vector = [1] * n
    for i in range(1, n):
        if ratings_scores_list[i] > ratings_scores_list[i - 1]:
            allocations_vector[i] = allocations_vector[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings_scores_list[i] > ratings_scores_list[i + 1]:
            allocations_vector[i] = max(allocations_vector[i], allocations_vector[i + 1] + 1)
    return sum(allocations_vector)

if __name__ == "__main__":
    print(f"Minimum resource units required to satisfy constraints: {calculate_minimum_candy_distribution([1, 0, 2])}")