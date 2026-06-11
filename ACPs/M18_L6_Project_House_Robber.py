# Module 18 Lesson 6: After-Class Project
# Project Name: Non-Adjacent Vector Elements Allocation Value Maximizer

def maximize_non_adjacent_payouts(values_yield_pool):
    if not values_yield_pool: return 0
    if len(values_yield_pool) <= 2: return max(values_yield_pool)
    prev_max_back_two, prev_max_back_one = values_yield_pool[0], max(values_yield_pool[0], values_yield_pool[1])
    for current_value in values_yield_pool[2:]:
        calculated_current_peak = max(prev_max_back_one, prev_max_back_two + current_value)
        prev_max_back_two = prev_max_back_one
        prev_max_back_one = calculated_current_peak
    return prev_max_back_one

if __name__ == "__main__":
    print(f"Maximum isolated independent parameter values synthesis totals yield: {maximize_non_adjacent_payouts([2, 7, 9, 3, 1])}")