# Module 3 Lesson 4: After-Class Project
# Project Name: Warehouse Bulk Freight Weight Distribution Splitter

class BulkLogisticsDistributor:
    def split_weight_loads(self, incoming_freight_weights_list, threshold_limit_kg):
        lightweight_shuttles = []
        heavyweight_containers = []
        
        for weight in incoming_freight_weights_list:
            if weight > threshold_limit_kg:
                heavyweight_containers.append(weight)
            else:
                lightweight_shuttles.append(weight)
                
        return {"ShuttleFleet": lightweight_shuttles, "HeavyContainers": heavyweight_containers}

if __name__ == "__main__":
    logistics = BulkLogisticsDistributor()
    cargo_manifest = [45, 120, 340, 88, 12, 500, 210]
    print(f"Logistics Manifest Structural Distribution Split: {logistics.split_weight_loads(cargo_manifest, 150)}")