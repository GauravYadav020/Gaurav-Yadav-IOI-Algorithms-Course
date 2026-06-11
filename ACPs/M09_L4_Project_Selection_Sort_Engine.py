# Module 9 Lesson 4: After-Class Project
# Project Name: Selection Sort High-Performance Memory Index Exchange Optimizer

class SelectionSortOptimizer:
    def execute_optimized_selection_sort(self, collection_data_stream):
        working_list = list(collection_data_stream)
        n = len(working_list)
        
        for step_idx in range(n):
            minimum_value_found_index = step_idx
            # Scan the remaining boundary segments to locate absolute minimum targets
            for scanning_pointer in range(step_idx + 1, n):
                if working_list[scanning_pointer] < working_list[minimum_value_found_index]:
                    minimum_value_found_index = scanning_pointer
                    
            # Rotate variables pointers state mappings values instantly
            working_list[step_idx], working_list[minimum_value_found_index] = working_list[minimum_value_found_index], working_list[step_idx]
            
        return working_list

if __name__ == "__main__":
    engine = SelectionSortOptimizer()
    print(f"Selection Sort Arranged Master Output Data Vector: {engine.execute_optimized_selection_sort([64, 25, 12, 22, 11])}")