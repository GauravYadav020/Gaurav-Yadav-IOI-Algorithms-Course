# Module 11 Lesson 4: After-Class Project
# Project Name: Deque Window Stream Processing Optimization Matrix

from collections import deque

def compute_sliding_window_max(data_stream, k_window_size):
    dq = deque()
    max_elements_output = []
    
    for idx, value in enumerate(data_stream):
        if dq and dq[0] < idx - k_window_size + 1:
            dq.popleft()
        while dq and data_stream[dq[-1]] <= value:
            dq.pop()
        dq.append(idx)
        if idx >= k_window_size - 1:
            max_elements_output.append(data_stream[dq[0]])
    return max_elements_output

if __name__ == "__main__":
    print(f"Sliding Window Maximum Out: {compute_sliding_window_max([1,3,-1,-3,5,3,6,7], 3)}")