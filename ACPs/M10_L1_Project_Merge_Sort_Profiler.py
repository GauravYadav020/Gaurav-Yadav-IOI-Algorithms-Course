# Module 10 Lesson 1: After-Class Project
# Project Name: Divide & Conquer Merge Sort High-Precision Execution Profiler

class ProfilingMergeSorter:
    def execute_merge_sort_split(self, target_unsorted_array):
        if len(target_unsorted_array) <= 1:
            return target_unsorted_array
            
        mid_idx = len(target_unsorted_array) // 2
        left_branch = self.execute_merge_sort_split(target_unsorted_array[:mid_idx])
        right_branch = self.execute_merge_sort_split(target_unsorted_array[mid_idx:])
        
        return self.__merge_sorted_branches(left_branch, right_branch)

    def __merge_sorted_branches(self, left, right):
        merged_output_list = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged_output_list.append(left[i])
                i += 1
            else:
                merged_output_list.append(right[j])
                j += 1
                
        merged_output_list.extend(left[i:])
        merged_output_list.extend(right[j:])
        return merged_output_list

if __name__ == "__main__":
    sorter = ProfilingMergeSorter()
    raw_input_data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Merge Sort Divide & Conquer Resolved Matrix: {sorter.execute_merge_sort_split(raw_input_data)}")