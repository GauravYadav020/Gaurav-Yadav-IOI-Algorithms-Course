# LESSON NAME: M19 Lesson 3 – Minimum Coins to make a value

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Write a basic recursive coin change solver that calculates 
# the absolute fewest number of coin pieces needed to reach a target invoice amount.
# ==========================================
def basic_recursive_min_coins(coins, target):
    if target == 0: return 0
    res = float('inf')
    
    for c in coins:
        if c <= target:
            sub_res = basic_recursive_min_coins(coins, target - c)
            if sub_res != float('inf') and sub_res + 1 < res:
                res = sub_res + 1
                
    return res

print("--- Activity 1: Fewest Coins Recursive Solver ---")
denominations = [9, 6, 5, 1]
amt = 11
print(f"Minimum coins needed for total {amt}: {basic_recursive_min_coins(denominations, amt)}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a 1D Tabulation array to optimize execution speed 
# and safely compute minimum coin distributions for higher business invoice metrics.
# ==========================================
class DynamicCoinChangeEngine:
    def calculate_minimum_pieces(self, coin_pool, final_sum):
        dp = [float('inf')] * (final_sum + 1)
        dp[0] = 0 # Base Case setup
        
        print(f"Building bottom-up coin allocation grid states up to target sum: {final_sum}")
        for i in range(1, final_sum + 1):
            for coin in coin_pool:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[final_sum] if dp[final_sum] != float('inf') else -1

print("\n--- Activity 2: 1D Bottom-Up Coin Change Tabulator ---")
engine = DynamicCoinChangeEngine()
print(f"Optimal pieces count for total 30: {engine.calculate_minimum_pieces([1, 5, 10, 25], 30)}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an advanced transactional point-of-sale checkout system 
# that handles completely unresolvable change anomalies safely without breaking runtime flow.
# ==========================================
class PointOfSaleChangeSafeguard:
    def audit_transaction_feasibility(self, machine_coins, user_change_due):
        if user_change_due < 0: return "Invalid transaction amount validation bounds."
        
        dp = [float('inf')] * (user_change_due + 1)
        dp[0] = 0
        
        for current_amt in range(1, user_change_due + 1):
            for bill in machine_coins:
                if bill <= current_amt:
                    dp[current_amt] = min(dp[current_amt], dp[current_amt - bill] + 1)
                    
        if dp[user_change_due] == float('inf'):
            return f"🚨 POS EXCEPTION: Impossible payout state! No mathematical combination exists for amount: ${user_change_due}"
        return f"🎉 Transaction feasible! Exact fewest units to dispatch: {dp[user_change_due]}"

print("\n--- Activity 3: High-Performance POS Transaction Safeguard ---")
pos_vault = [5, 10]
requested_change = 7  # Impossible to create with only 5s and 10s
auditor = PointOfSaleChangeSafeguard()
print(auditor.audit_transaction_feasibility(pos_vault, requested_change))
print("-" * 40)