# Module 11 Lesson 5: After-Class Project
# Project Name: Operational FIFO Queue Inversion Pipeline Utility

from collections import deque

def reverse_first_k_elements(queue_instance, k_steps):
    if not queue_instance or k_steps > len(queue_instance) or k_steps <= 0: return queue_instance
    stack = []
    for _ in range(k_steps):
        stack.append(queue_instance.popleft())
    while stack:
        queue_instance.append(stack.pop())
    for _ in range(len(queue_instance) - k_steps):
        queue_instance.append(queue_instance.popleft())
    return queue_instance

if __name__ == "__main__":
    q = deque([10, 20, 30, 40, 50])
    print(f"Queue context transformation inverted framework: {list(reverse_first_k_elements(q, 3))}")