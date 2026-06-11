# Module 9 Lesson 3: After-Class Project
# Project Name: Insertion Sort In-Memory Array State Inversion Profiler

class AnalyticsInsertionSorter:
    def sort_and_profile_inversions(self, input_unarranged_elements_list):
        arr = list(input_unarranged_elements_list)
        total_shifts = 0
        
        for i in range(1, len(arr)):
            key_element = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key_element:
                arr[j + 1] = arr[j]
                j -= 1
                total_shifts += 1
            arr[j + 1] = key_element
            
        return {"ArraySortedState": arr, "TotalStructuralArrayShifts": total_shifts}

if __name__ == "__main__":
    sorter = AnalyticsInsertionSorter()
    print(f"Insertion Sorting Output Diagnostics Summary: {sorter.sort_and_profile_inversions([22, 11, 99, 88, 44])}")