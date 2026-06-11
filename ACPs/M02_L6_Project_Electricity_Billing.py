# Module 2 Lesson 6: After-Class Project
# Project Name: Progressive Tier Commercial Grid Electricity Invoicer

class PowerGridInvoicer:
    def calculate_utility_bill(self, total_kilowatt_hours):
        accumulated_cost = 0.0
        if total_kilowatt_hours <= 100:
            accumulated_cost = total_kilowatt_hours * 3.50
        elif total_kilowatt_hours <= 300:
            accumulated_cost = (100 * 3.50) + ((total_kilowatt_hours - 100) * 4.75)
        else:
            accumulated_cost = (100 * 3.50) + (200 * 4.75) + ((total_kilowatt_hours - 300) * 6.20)
        return round(accumulated_cost, 2)

if __name__ == "__main__":
    billing = PowerGridInvoicer()
    print(f"Calculated Smart Grid Monthly Invoice Total: ${billing.calculate_utility_bill(450)}")