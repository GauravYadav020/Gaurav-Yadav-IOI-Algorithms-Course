# Module 14 Lesson 6: After-Class Project
# Project Name: Multi-Channel Data Stream Min-Heap Synthesis Pipeline

import heapq

def merge_k_sorted_arrays(jagged_arrays_stream_list):
    heap, compiled_output = [], []
    for array_idx, target_array in enumerate(jagged_arrays_stream_list):
        if target_array: heapq.heappush(heap, (target_array[0], array_idx, 0))
        
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        compiled_output.append(val)
        if elem_idx + 1 < len(jagged_arrays_stream_list[arr_idx]):
            heapq.heappush(heap, (jagged_arrays_stream_list[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    return compiled_output

if __name__ == "__main__":
    streams = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(f"Synthesized linear matrix output pipeline: {merge_k_sorted_arrays(streams)}")