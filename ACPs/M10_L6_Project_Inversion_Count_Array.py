# Module 10 Lesson 6: After-Class Project
# Project Name: Collaborative Filtering Recommendation Inversion Counter

class RecommendationInversionCounter:
    def calculate_inversions_count(self, user_preference_ranking_array):
        working_array = list(user_preference_ranking_array)
        _, total_inversions = self.__merge_and_count_recursive(working_array)
        return total_inversions

    def __merge_and_count_recursive(self, arr):
        if len(arr) <= 1:
            return arr, 0
            
        mid = len(arr) // 2
        left, left_count = self.__merge_and_count_recursive(arr[:mid])
        right, right_count = self.__merge_and_count_recursive(arr[mid:])
        
        merged, merge_count = self.__merge_and_count_split(left, right)
        return merged, (left_count + right_count + merge_count)

    def __merge_and_count_split(self, left, right):
        merged = []
        i = j = count = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # When right element is smaller, it means it skips over all remaining elements inside left array framework slice
                count += (len(left) - i)
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

if __name__ == "__main__":
    counter = RecommendationInversionCounter()
    rankings = [1, 20, 6, 4, 5]
    print(f"Total calculated structural rank inversions profile value matching: {counter.calculate_inversions_count(rankings)}")