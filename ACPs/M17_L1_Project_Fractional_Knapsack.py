# Module 17 Lesson 1: After-Class Project
# Project Name: Fractional Knapsack Continuous Value Optimizer

class CargoItem:
    def __init__(self, value, weight):
        self.val = value
        self.wt = weight
        self.density = value / weight

def compute_fractional_knapsack_max(items_pool_objects, max_payload_capacity):
    items_pool_objects.sort(key=lambda item: item.density, reverse=True)
    accumulated_net_worth = 0.0
    for item in items_pool_objects:
        if max_payload_capacity >= item.wt:
            max_payload_capacity -= item.wt
            accumulated_net_worth += item.val
        else:
            accumulated_net_worth += item.density * max_payload_capacity
            break
    return round(accumulated_net_worth, 2)

if __name__ == "__main__":
    pool = [CargoItem(60, 10), CargoItem(100, 20), CargoItem(120, 30)]
    print(f"Greedy resource configuration total optimal score calculated: ${compute_fractional_knapsack_max(pool, 50)}")