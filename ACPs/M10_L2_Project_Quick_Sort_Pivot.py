# Module 10 Lesson 2: After-Class Project
# Project Name: Quick Sort High-Speed In-Place Hoare Partitioning Framework

class HighSpeedQuickSorter:
    def sort_inplace(self, target_array, low, high):
        if low < high:
            pivot_index = self.__partition_hoare(target_array, low, high)
            self.sort_inplace(target_array, low, pivot_index - 1)
            self.sort_inplace(target_array, pivot_index + 1, high)
        return target_array

    def __partition_hoare(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

if __name__ == "__main__":
    sorter = HighSpeedQuickSorter()
    test_arr = [10, 7, 8, 9, 1, 5]
    print(f"Quick Sort Final State Realized Structural Array: {sorter.sort_inplace(test_arr, 0, len(test_arr)-1)}")