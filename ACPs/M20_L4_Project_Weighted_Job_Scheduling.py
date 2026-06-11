# Module 20 Lesson 4: After-Class Project
# Project Name: Binary Interval Search High-Yield Dynamic Work Planner

import bisect

def compute_max_weighted_revenue(tasks_triplets_list):
    tasks_triplets_list.sort(key=lambda x: x[1])
    finish_times = [task[1] for task in tasks_triplets_list]
    n = len(tasks_triplets_list)
    dp = [0] * n
    dp[0] = tasks_triplets_list[0][2]
    
    for i in range(1, n):
        start, _, payout = tasks_triplets_list[i]
        include_payout = payout
        idx = bisect.bisect_right(finish_times, start) - 1
        if idx >= 0: include_payout += dp[idx]
        dp[i] = max(include_payout, dp[i - 1])
    return dp[-1]

if __name__ == "__main__":
    pipeline = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 41)]
    print(f"Maximum calculated optimal compound net value tracking target yields: ${compute_max_weighted_revenue(pipeline)}")