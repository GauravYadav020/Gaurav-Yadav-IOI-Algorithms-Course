# Module 19 Lesson 6: After-Class Project
# Project Name: Unbounded Knapsack Commercial Segment Revenue Maximizer

def maximize_rod_cutting_revenue(market_prices_list, total_rod_length):
    dp = [0] * (total_rod_length + 1)
    for length_step in range(1, total_rod_length + 1):
        max_val = float('-inf')
        for pieces_cut_idx in range(length_step):
            max_val = max(max_val, market_prices_list[pieces_cut_idx] + dp[length_step - pieces_cut_idx - 1])
        dp[length_step] = max_val
    return dp[total_rod_length]

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print(f"Maximum calculated production partition net yields values payouts: ${maximize_rod_cutting_revenue(prices, 8)}")