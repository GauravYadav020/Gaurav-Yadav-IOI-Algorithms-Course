# LESSON NAME: M17 Lesson 2 – The fractional knapsack problem

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a basic greedy algorithm that calculates maximum value 
# by sorting inventory items explicitly by their total unit values alone.
# ==========================================
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def simple_fractional_knapsack(items, capacity):
    # Sort items based simply on basic raw value descending as a introductory proxy
    items.sort(key=lambda x: x.value, reverse=True)
    
    total_profit = 0.0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_profit += item.value
        else:
            fraction = capacity / item.weight
            total_profit += item.value * fraction
            break
    return total_profit

print("--- Activity 1: Value-Sorted Fractional Storage ---")
stock = [Item(60, 10), Item(100, 20), Item(120, 30)]
max_val = simple_fractional_knapsack(stock, capacity=50)
print(f"Calculated basic inventory load yield limit: ${max_val:.2f}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement the classic fractional knapsack algorithm that uses the mathematically 
# optimal Value-to-Weight density ratio ($V/W$) to optimize shipping weight container loads.
# ==========================================
class OptimalDensityCargoLoader:
    def maximize_cargo_yield(self, val_list, weight_list, max_capacity):
        # Create structured mappings containing computed value densities
        index_map = []
        for i in range(len(val_list)):
            density = val_list[i] / weight_list[i]
            index_map.append((val_list[i], weight_list[i], density, i))
            
        # Sort using the calculated weight density ratio parameter metrics
        index_map.sort(key=lambda x: x[2], reverse=True)
        
        current_weight = 0
        accrued_value = 0.0
        
        print("Processing optimal allocation distributions:")
        for v, w, dens, idx in index_map:
            if current_weight + w <= max_capacity:
                current_weight += w
                accrued_value += v
                print(f" -> Allocated 100% of Cargo Item [{idx}] (Added weight: {w}kg)")
            else:
                remaining_gap = max_capacity - current_weight
                fractional_slice = remaining_gap / w
                accrued_value += v * fractional_slice
                print(f" -> Allocated {fractional_slice*100:.1f}% of fractional slice item [{idx}]")
                break
                
        return accrued_value

print("\n--- Activity 2: Optimal Density Ratio Cargo Loader ---")
values = [500, 400, 300, 700]
weights = [10, 20, 15, 30]
loader = OptimalDensityCargoLoader()
yield_res = loader.maximize_cargo_yield(values, weights, max_capacity=45)
print(f"Total maximum shipping asset compound revenue yield: ${yield_res:.2f}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a high-performance database file logistics compiler that processes large datasets, 
# measuring instruction parsing durations and checking edge case limits where weights equal zero.
# ==========================================
import time

def production_logistics_benchmarker(data_tuples_list, container_capacity):
    if container_capacity <= 0: return 0.0
    
    t_start = time.perf_counter()
    
    # Filter anomalies out safely (e.g., handle item configurations with zero weight weights to avoid ZeroDivisionError)
    sanitized_items = [d for d in data_tuples_list if d[1] > 0]
    # Sort on high-precision floating point density metrics
    sanitized_items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    collected_payout = 0.0
    for payoff, mass in sanitized_items:
        if container_capacity >= mass:
            container_capacity -= mass
            collected_payout += payoff
        else:
            collected_payout += payoff * (container_capacity / mass)
            break
            
    duration = (time.perf_counter() - t_start) * 1000
    print(f"Algorithmic dynamic instruction duration time: {duration:.4f} ms")
    return collected_payout

print("\n--- Activity 3: High-Precision Logistics Benchmarker ---")
massive_logistics_stream = [(1200, 30), (600, 10), (900, 20), (0, 5)] # contains safety checking constraints
final_payout = production_logistics_benchmarker(massive_logistics_stream, container_capacity=35)
print(f"Compiled database high-performance calculation payout: ${final_payout:.2f}")
print("-" * 40)