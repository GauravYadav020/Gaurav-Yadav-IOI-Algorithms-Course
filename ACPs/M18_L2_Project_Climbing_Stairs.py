# Module 18 Lesson 2: After-Class Project
# Project Name: Linear Iterative Step Configurations Tabulator Engine

def compute_staircase_combinations(total_steps_n):
    if total_steps_n <= 2: return total_steps_n
    step_minus_two, step_minus_one = 1, 2
    for _ in range(3, total_steps_n + 1):
        step_minus_two, step_minus_one = step_minus_one, step_minus_two + step_minus_one
    return step_minus_one

if __name__ == "__main__":
    print(f"Total mathematically verified arrangement configuration trajectories: {compute_staircase_combinations(5)}")