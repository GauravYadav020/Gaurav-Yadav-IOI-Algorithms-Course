# Module 9 Lesson 5: After-Class Project
# Project Name: Multi-Occurrence Transaction Linear Searching Stream Indexer

class StreamLinearSearchIndexer:
    def locate_all_matching_indices(self, telemetry_data_stream, target_lookup_value):
        index_occurrences_matched_list = []
        
        for current_pointer_idx, current_element_val in enumerate(telemetry_data_stream):
            if current_element_val == target_lookup_value:
                index_occurrences_matched_list.append(current_pointer_idx)
                
        return {
            "MatchesFoundCount": len(index_occurrences_matched_list),
            "TargetIndexCoordinates": index_occurrences_matched_list
        }

if __name__ == "__main__":
    searcher = StreamLinearSearchIndexer()
    logs_stream = [101, 404, 200, 404, 301, 404, 500]
    print(f"Linear Scanning Multi-Match Tracker Profile Results: {searcher.locate_all_matching_indices(logs_stream, 404)}")