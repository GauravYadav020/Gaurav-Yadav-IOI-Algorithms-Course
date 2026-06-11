# Module 9 Lesson 2: After-Class Project
# Project Name: Interactive Bubble Sort Metric Telemetry Logging Matrix

class MetricBubbleSorter:
    def execute_monitored_bubble_sort(self, raw_unarranged_list):
        working_array = list(raw_unarranged_list)
        n = len(working_array)
        total_swaps_counter = 0
        
        print(f"Beginning bubble sort tracking passes sequence logic on input framework of length: {n}")
        for pass_idx in range(n):
            is_swapped_flag = False
            for element_idx in range(0, n - pass_idx - 1):
                if working_array[element_idx] > working_array[element_idx + 1]:
                    # Switch element pointer mapping layouts positions
                    working_array[element_idx], working_array[element_idx + 1] = working_array[element_idx + 1], working_array[element_idx]
                    total_swaps_counter += 1
                    is_swapped_flag = True
                    
            if not is_swapped_flag:
                break # Sequence array execution optimization exit path
                
        return {"SortedResult": working_array, "TotalSwapsIncurred": total_swaps_counter}

if __name__ == "__main__":
    sorter = MetricBubbleSorter()
    dataset = [45, 12, 89, 5, 23]
    print(f"Bubble Sort Framework Profile Analysis Metrics: {sorter.execute_monitored_bubble_sort(dataset)}")