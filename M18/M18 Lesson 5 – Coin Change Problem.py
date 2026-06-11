# LESSON NAME: M18 Lesson 5 – Coin Change Problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a basic recursive coin change counter that counts total 
# combinations for small target values without any caching.
# ==========================================
def recursive_change_combinations(coin_denominations, total_coins, target_amount):
    # Base Case Targets
    if target_amount == 0: return 1
    if target_amount < 0 or total_coins <= 0: return 0
    
    # Choice tree: Include current coin element vs Exclude current coin element
    return recursive_change_combinations(coin_denominations, total_coins, target_amount - coin_denominations[total_coins - 1]) + \
           recursive_change_combinations(coin_denominations, total_coins - 1, target_amount)

print("--- Activity 1: Recursive Coin Counter ---")
denoms = [1, 2, 3]
target = 4
print(f"Total separate combinations variations found: {recursive_change_combinations(denoms, len(denoms), target)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Build an optimal 1D array Tabulation engine to calculate the 
# absolute minimum number of coins needed to clear an invoice total amount.
# ==========================================
class MinimumCoinChangeTabulator:
    def calculate_min_coins(self, coin_options, final_amount):
        # Fill lookup list array with infinity representations
        dp_table = [float('inf')] * (final_amount + 1)
        dp_table[0] = 0 # Base case: 0 amount needs 0 coins
        
        for current_sum in range(1, final_amount + 1):
            for coin in coin_options:
                if current_sum - coin >= 0:
                    dp_table[current_sum] = min(dp_table[current_sum], dp_table[current_sum - coin] + 1)
                    
        return dp_table[final_amount] if dp_table[final_amount] != float('inf') else -1

print("\n--- Activity 2: Minimum Coin Change Tabulator ---")
options = [1, 5, 6, 9]
total_sum = 11
tab_engine = MinimumCoinChangeTabulator()
print(f"Absolute minimum coin units needed to clear {total_sum}: {tab_engine.calculate_min_coins(options, total_sum)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an advanced POS checkout counter simulation that logs 
# transaction allocations in real time and handles impossible-change anomalies safely.
# ==========================================
class ProductionCheckoutChangeEngine:
    def compile_change_allocation(self, bills_pool, checkout_sum):
        if checkout_sum <= 0: return []
        
        dp_table = [float('inf')] * (checkout_sum + 1)
        parent_coin_map = [-1] * (checkout_sum + 1)
        dp_table[0] = 0
        
        for amt in range(1, checkout_sum + 1):
            for coin in bills_pool:
                if amt - coin >= 0 and dp_table[amt - coin] + 1 < dp_table[amt]:
                    dp_table[amt] = dp_table[amt - coin] + 1
                    parent_coin_map[amt] = coin
                    
        if dp_table[checkout_sum] == float('inf'):
            print(f"⚠️ POS EXCEPTION ERROR: Impossible transaction amount validation bounds for total: ${checkout_sum}")
            return []
            
        # Reconstruct exactly which coins were used to build the amount
        selected_coins_list = []
        step_tracker = checkout_sum
        while step_tracker > 0:
            selected_coins_list.append(parent_coin_map[step_tracker])
            step_tracker -= parent_coin_map[step_tracker]
            
        return selected_coins_list

print("\n--- Activity 3: Real-Time POS Cashier Breakdown ---")
register_bills = [2, 5, 10]
requested_cash = 14
cashier = ProductionCheckoutChangeEngine()
print(f"Exact physical coin denominations selected for change breakdown: {cashier.compile_change_allocation(register_bills, requested_cash)}")
print("-" * 40)