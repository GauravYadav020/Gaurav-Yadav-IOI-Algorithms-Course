# Module 11 Lesson 6: After-Class Project
# Project Name: LRU Cache Memory Management Simulation Pipeline

class LRUCacheNode:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class ProductionLRUCacheManager:
    def __init__(self, storage_capacity_limit):
        self.cap = storage_capacity_limit
        self.lookup_map = {}
        self.head, self.tail = LRUCacheNode(0, 0), LRUCacheNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def __isolate_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def __inject_at_head(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node

    def fetch_cached_value(self, key):
        if key in self.lookup_map:
            node = self.lookup_map[key]
            self.__isolate_node(node)
            self.__inject_at_head(node)
            return node.val
        return -1

    def commit_cache_payload(self, key, value):
        if key in self.lookup_map:
            self.__isolate_node(self.lookup_map[key])
        node = LRUCacheNode(key, value)
        self.__inject_at_head(node)
        self.lookup_map[key] = node
        if len(self.lookup_map) > self.cap:
            lru_tail = self.tail.prev
            self.__isolate_node(lru_tail)
            del self.lookup_map[lru_tail.key]

if __name__ == "__main__":
    cache = ProductionLRUCacheManager(2)
    cache.commit_cache_payload(1, 100)
    cache.commit_cache_payload(2, 200)
    print(f"Fetched register data value: {cache.fetch_cached_value(1)}")