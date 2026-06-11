# Module 4 Lesson 4: After-Class Project
# Project Name: Multi-Store Retail Product Merging and Catalog Sync Engine

class DistributedCatalogSynchronizer:
    def merge_retail_catalogs(self, outlet_catalog_a, outlet_catalog_b):
        # Master sync process using automated union mechanics
        master_synced_catalog = outlet_catalog_a.copy()
        
        for key, value in outlet_catalog_b.items():
            if key in master_synced_catalog:
                # Retain the lowest retail market value price as competitive proxy
                master_synced_catalog[key] = min(master_synced_catalog[key], value)
            else:
                master_synced_catalog[key] = value
                
        return master_synced_catalog

if __name__ == "__main__":
    sync = DistributedCatalogSynchronizer()
    store1 = {"Laptop": 1200, "Keyboard": 45}
    store2 = {"Keyboard": 38, "Mouse": 25}
    print(f"Synchronized Master Network Store Price Catalog: {sync.merge_retail_catalogs(store1, store2)}")