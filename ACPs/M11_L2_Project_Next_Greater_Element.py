# Module 11 Lesson 2: After-Class Project
# Project Name: Next Greater Element Monotonic Parser Pipeline

def compute_next_greater_elements(arr):
    results = [-1] * len(arr)
    stack = []
    for idx in range(len(arr)):
        while stack and arr[stack[-1]] < arr[idx]:
            position = stack.pop()
            results[position] = arr[idx]
        stack.append(idx)
    return results

if __name__ == "__main__":
    print(f"Next Greater Elements Tracked: {compute_next_greater_elements([4, 5, 2, 25])}")