# LESSON NAME: M13 Lesson 3 – Searching in Binary Search Tree

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Library management quick catalog search by Book ID.
# ==========================================
class Book:
    def __init__(self, key, title):
        self.key = key
        self.title = title
        self.left = self.right = None

class LibrarySystem:
    def __init__(self): self.root = None
    def add(self, key, title):
        if not self.root: self.root = Book(key, title); return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left: curr.left = Book(key, title); break
                curr = curr.left
            else:
                if not curr.right: curr.right = Book(key, title); break
                curr = curr.right
    def search(self, target_key):
        curr = self.root
        while curr:
            if curr.key == target_key: return curr.title
            curr = curr.left if target_key < curr.key else curr.right
        return None

print("--- Activity 1: Library Quick-Search ---")
lib = LibrarySystem()
lib.add(1001, "The Odyssey")
print(f"Search 1001: {lib.search(1001)}")

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Network Route Traceroute displaying exact hop path sequence.
# ==========================================
class RouterNode:
    def __init__(self, ip_code):
        self.ip_code = ip_code
        self.left = self.right = None

class NetworkRouterBST:
    def __init__(self): self.root = None
    def insert(self, ip_code):
        def _add(node, code):
            if not node: return RouterNode(code)
            if code < node.ip_code: node.left = _add(node.left, code)
            else: node.right = _add(node.right, code)
            return node
        self.root = _add(self.root, ip_code)
    def trace_route(self, node, target_code, path_list):
        if not node: return False
        path_list.append(node.ip_code)
        if node.ip_code == target_code: return True
        if target_code < node.ip_code: return self.trace_route(node.left, target_code, path_list)
        return self.trace_route(node.right, target_code, path_list)

print("\n--- Activity 2: Network Traceroute ---")
router = NetworkRouterBST()
router.insert(50)
router.insert(25)
path = []
router.trace_route(router.root, 25, path)
print(f"Route Path: {path}")

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: E-Commerce price filtering budget range-search query engine.
# ==========================================
class ProductNode:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.left = self.right = None

class ProductCatalogBST:
    def __init__(self): self.root = None
    def insert(self, price, name):
        def _ins(node):
            if not node: return ProductNode(price, name)
            if price < node.price: node.left = _ins(node.left)
            else: node.right = _ins(node.right)
            return node
        self.root = _ins(self.root)
    def find_products_in_range(self, node, min_p, max_p, matched_list):
        if not node: return
        if node.price > min_p: self.find_products_in_range(node.left, min_p, max_p, matched_list)
        if min_p <= node.price <= max_p: matched_list.append((node.name, node.price))
        if node.price < max_p: self.find_products_in_range(node.right, min_p, max_p, matched_list)

print("\n--- Activity 3: Price Filter Query ---")
catalog = ProductCatalogBST()
catalog.insert(120, "Keyboard")
res = []
catalog.find_products_in_range(catalog.root, 40, 130, res)
print(f"Products: {res}")