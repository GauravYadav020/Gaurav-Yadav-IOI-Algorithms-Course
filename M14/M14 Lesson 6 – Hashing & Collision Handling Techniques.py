# LESSON NAME: M14 Lesson 6 – Hashing & Collision Handling Techniques

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a simple username authorization hashing directory table 
# using the modulo math technique to map and find array tracking row locations.
# ==========================================
class SimpleModuloHashTable:
    def __init__(self, spaces_limit):
        self.slots_cap = spaces_limit
        self.table = [None] * spaces_limit

    def calculate_hash(self, input_string):
        character_ascii_sum = sum(ord(char) for char in input_string)
        return character_ascii_sum % self.slots_cap

    def store_user_profile(self, user_id_tag):
        target_slot = self.calculate_hash(user_id_tag)
        self.table[target_slot] = user_id_tag
        print(f"Routed username registry entry string '{user_id_tag}' to index bucket slot position: {target_slot}")

print("--- Activity 1: Direct Modulo Hash Map Directory ---")
directory = SimpleModuloHashTable(spaces_limit=10)
directory.store_user_profile("AlphaUser")
directory.store_user_profile("BetaFlyer")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Create a secure database dictionary cache using the Chaining Method 
# (Linked Lists) to resolve key collisions gracefully when data maps land on identical target slots.
# ==========================================
class ChainingCollisionHashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert_record(self, key, profile_payload):
        slot = self._hash_function(key)
        for index, element in enumerate(self.buckets[slot]):
            if element[0] == key:
                self.buckets[slot][index] = (key, profile_payload)
                return
        self.buckets[slot].append((key, profile_payload))
        print(f"Assigned Record mapping link [{key}] inside bucket frame index slot position: {slot}")

    def lookup(self, key):
        slot = self._hash_function(key)
        for k, v in self.buckets[slot]:
            if k == key: return v
        return None

print("\n--- Activity 2: Separate Chaining Collision Resolution Map ---")
cache = ChainingCollisionHashTable(size=5)
cache.insert_record("ID-101", "Alice Project Frame Details")
cache.insert_record("ID-106", "Bob Analytics Profile System") # Intentionally matches index bucket map slot targets
print(f"Retrieval evaluation match result: {cache.lookup('ID-101')}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build a high-performance database file storage map indexing architecture 
# implementing the Linear Probing technique to handle structural path collisions.
# ==========================================
class LinearProbingDatabaseTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys_list = [None] * capacity
        self.values_list = [None] * capacity

    def _hash(self, key_string):
        return sum(ord(c) for c in key_string) % self.capacity

    def write_transaction(self, key, value_string):
        home_slot = self._hash(key)
        current_slot = home_slot
        
        while self.keys_list[current_slot] is not None:
            if self.keys_list[current_slot] == key:
                self.values_list[current_slot] = value_string
                return
            current_slot = (current_slot + 1) % self.capacity
            if current_slot == home_slot:
                raise KeyError("Database system capacity limit reached. Storage table filled.")
        
        self.keys_list[current_slot] = key
        self.values_list[current_slot] = value_string
        print(f"Saved entry key '{key}' to slot {current_slot} (Hash index originally pointed to: {home_slot})")

print("\n--- Activity 3: Open Addressing Linear Probing Engine ---")
db_ledger = LinearProbingDatabaseTable(capacity=4)
db_ledger.write_transaction("Dept-Sales", "Revenue Ledger Node Frame Alpha")
db_ledger.write_transaction("Dept-Legal", "Contract File Block Binary Target")
db_ledger.write_transaction("Dept-Slack", "Communication Protocol Node Data String")
print("-" * 40)