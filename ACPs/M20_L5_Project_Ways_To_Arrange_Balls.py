# Module 20 Lesson 5: After-Class Project
# Project Name: Non-Adjacent Identity Sequence Permutations Cache Engine

class ArrangementCacheEngine:
    def __init__(self): self.cache = {}
    def calculate_ways(self, p, q, r, last_id):
        key = (p, q, r, last_id)
        if key in self.cache: return self.cache[key]
        if p == 0 and q == 0 and r == 0: return 1
        paths = 0
        if p > 0 and last_id != 1: paths += self.calculate_ways(p - 1, q, r, 1)
        if q > 0 and last_id != 2: paths += self.calculate_ways(p, q - 1, r, 2)
        if r > 0 and last_id != 3: paths += self.calculate_ways(p, q, r - 1, 3)
        self.cache[key] = paths
        return paths

if __name__ == "__main__":
    engine = ArrangementCacheEngine()
    print(f"Total mathematically secure distribution permutations paths tracking context: {engine.calculate_ways(2, 2, 2, 0)}")