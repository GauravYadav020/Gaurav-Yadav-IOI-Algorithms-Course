# Module 18 Lesson 4: After-Class Project
# Project Name: LIS Structural Pattern Sequence Tabulation Optimizer

def compute_lis_length(data_vector_array):
    if not data_vector_array: return 0
    dp_tracker = [1] * len(data_vector_array)
    for i in range(1, len(data_vector_array)):
        for j in range(0, i):
            if data_vector_array[i] > data_vector_array[j]:
                dp_tracker[i] = max(dp_tracker[i], dp_tracker[j] + 1)
    return max(dp_tracker)

if __name__ == "__main__":
    print(f"Longest continuous target subsystem alignment metrics layout length: {compute_lis_length([10, 9, 2, 5, 3, 7, 101, 18])}")