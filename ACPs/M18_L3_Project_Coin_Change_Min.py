# Module 18 Lesson 3: After-Class Project
# Project Name: Coin Change Minimum Node Matrix Combination Tabulator

def calculate_min_coins_required(denominations_pool, target_amount):
    dp_matrix = [float('inf')] * (target_amount + 1)
    dp_matrix[0] = 0
    for value_step in range(1, target_amount + 1):
        for coin in denominations_pool:
            if value_step - coin >= 0:
                dp_matrix[value_step] = min(dp_matrix[value_step], dp_matrix[value_step - coin] + 1)
    return dp_matrix[target_amount] if dp_matrix[target_amount] != float('inf') else -1

if __name__ == "__main__":
    print(f"Optimal allocation count target combination metrics match: {calculate_min_coins_required([1, 2, 5], 11)}")