# Module 1 Lesson 3: After-Class Project
# Project Name: High-Fidelity Retail Inventory Control Ledger System

class InventoryLedger:
    def __init__(self):
        self.vault = {}

    def ingest_asset(self, sku, description, quantity, wholesale_cost):
        if quantity < 0 or wholesale_cost < 0: return False
        self.vault[sku] = {"desc": description, "qty": quantity, "cost": wholesale_cost}
        return True

    def run_reorder_audit(self, critical_threshold=5):
        alerts = []
        for sku, meta in self.vault.items():
            if meta["qty"] <= critical_threshold:
                alerts.append((sku, meta["desc"], meta["qty"]))
        return alerts

if __name__ == "__main__":
    warehouse = InventoryLedger()
    warehouse.ingest_asset("SKU-99", "GPU Hardware", 12, 450.00)
    warehouse.ingest_asset("SKU-104", "Solid State Drive", 2, 85.00)
    print(f"Critical Warehouse Stocks Alert Log: {warehouse.run_reorder_audit()}")