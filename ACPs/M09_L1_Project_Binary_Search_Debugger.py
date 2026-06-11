# Module 9 Lesson 1: After-Class Project
# Project Name: High-Speed Array Binary Search Matrix Element Lookup Engine

class AnalyticsBinarySearchEngine:
    def search_sorted_inventory_id(self, ordered_id_array, target_id_key):
        low_pointer = 0
        high_pointer = len(ordered_id_array) - 1
        
        while low_pointer <= high_pointer:
            midpoint_index = (low_pointer + high_pointer) // 2
            midpoint_value = ordered_id_array[midpoint_index]
            
            if midpoint_value == target_id_key:
                return midpoint_index # Target matched lookup location returned
            elif midpoint_value < target_id_key:
                low_pointer = midpoint_index + 1
            else:
                high_pointer = midpoint_index - 1
                
        return -1 # Key element not located inside target collection array bounding frames

if __name__ == "__main__":
    engine = AnalyticsBinarySearchEngine()
    sorted_uids = [1002, 2004, 3500, 4120, 5060, 9999]
    print(f"Target key located at sorted index matching layout location: {engine.search_sorted_inventory_id(sorted_uids, 4120)}")