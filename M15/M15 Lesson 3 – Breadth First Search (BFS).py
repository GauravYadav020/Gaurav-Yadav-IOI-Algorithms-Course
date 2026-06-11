# LESSON NAME: M15 Lesson 3 – Breadth First Search (BFS)

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Implement a standard FIFO queue-driven BFS algorithm to map 
# out contact tracing lines across an unweighted social circle tracking tree.
# ==========================================
from collections import deque

def traverse_social_bfs(graph, starting_node):
    visited = set([starting_node])
    queue = deque([starting_node])
    processing_order = []
    
    while queue:
        current = queue.popleft()
        processing_order.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return processing_order

print("--- Activity 1: Social Network Contact BFS ---")
social_circle = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David", "Eve"],
    "Charlie": ["Alice", "Frank"],
    "David": ["Bob"], "Eve": ["Bob"], "Frank": ["Charlie"]
}
print(f"BFS Contact Cascade Verification: {traverse_social_bfs(social_circle, 'Alice')}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement a shortest-path checker using BFS to find the 
# minimum number of network hops required to route a packet between two servers.
# ==========================================
def find_minimum_network_hops(graph, start, destination):
    if start == destination: return 0
    visited = set([start])
    queue = deque([(start, 0)]) # Stores (current_node, hop_count)
    
    while queue:
        node, hops = queue.popleft()
        if node == destination:
            return hops
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, hops + 1))
    return -1 # Path does not exist

print("\n--- Activity 2: Minimal Network Hop Distance Engine ---")
network_grid = {
    "Switch-1": ["Switch-2", "Switch-3"],
    "Switch-2": ["Switch-1", "Mainframe"],
    "Switch-3": ["Switch-1", "Gateway-Node"],
    "Gateway-Node": ["Switch-3", "Mainframe"],
    "Mainframe": ["Switch-2", "Gateway-Node"]
}
min_path = find_minimum_network_hops(network_grid, "Switch-1", "Mainframe")
print(f"Shortest routing leap count to Mainframe: {min_path} hop(s)")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Build an AI crawler engine that monitors web page discovery loops, 
# preventing cyclic trap states through strict real-time state lookup histories.
# ==========================================
class AutomatedWebCrawlerBFS:
    def __init__(self, web_links_graph):
        self.internet = web_links_graph

    def crawl_domain_space(self, seed_url, max_pages=4):
        discovered_history = set([seed_url])
        crawler_queue = deque([seed_url])
        pages_processed_count = 0
        
        print(f"Launching AI Spider Crawl from target core seed checkpoint: {seed_url}")
        while crawler_queue and pages_processed_count < max_pages:
            url = crawler_queue.popleft()
            pages_processed_count += 1
            print(f" -> Indexing and parsing metadata details for page: {url}")
            
            for linked_page in self.internet.get(url, []):
                if linked_page not in discovered_history:
                    discovered_history.add(linked_page)
                    crawler_queue.append(linked_page)

print("\n--- Activity 3: Cycle-Safe AI Web Crawler ---")
simulated_web = {
    "home.com": ["about.com", "shop.com"],
    "about.com": ["home.com", "blog.com"], # Backlink loop trap
    "shop.com": ["checkout.net"],
    "blog.com": [], "checkout.net": []
}
spider = AutomatedWebCrawlerBFS(simulated_web)
spider.crawl_domain_space("home.com", max_pages=5)
print("-" * 40)