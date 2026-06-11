# Module 20 Lesson 2: After-Class Project
# Project Name: Greedy Unsorted Activity Interval Overlap Filters

def select_max_non_overlapping_activities(appointments_triplets_list):
    appointments_triplets_list.sort(key=lambda x: x[2]) # Sort by finish time constraints parameters profiles
    approved_selections = [appointments_triplets_list[0]]
    last_finish_marker = appointments_triplets_list[0][2]
    for idx in range(1, len(appointments_triplets_list)):
        start, finish = appointments_triplets_list[idx][1], appointments_triplets_list[idx][2]
        if start >= last_finish_marker:
            approved_selections.append(appointments_triplets_list[idx])
            last_finish_marker = finish
    return approved_selections

if __name__ == "__main__":
    raw_data = [('A', 5, 9), ('B', 1, 2), ('C', 3, 4)]
    print(f"Total compiled non-overlapping resource allocations counter: {len(select_max_non_overlapping_activities(raw_data))}")