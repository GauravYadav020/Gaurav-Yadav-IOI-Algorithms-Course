# Module 17 Lesson 4: After-Class Project
# Project Name: Circular Circuit Transit Matrix Fuel Station Profiler

def locate_circuit_start_point(gas_provisions_list, cost_burn_list):
    if sum(gas_provisions_list) < sum(cost_burn_list): return -1
    running_fuel_tank_balance, optimal_starting_index = 0, 0
    for idx in range(len(gas_provisions_list)):
        running_fuel_tank_balance += gas_provisions_list[idx] - cost_burn_list[idx]
        if running_fuel_tank_balance < 0:
            running_fuel_tank_balance = 0
            optimal_starting_index = idx + 1
    return optimal_starting_index

if __name__ == "__main__":
    g, c = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    print(f"Optimal coordinate loop checkpoint index start: {locate_circuit_start_point(g, c)}")