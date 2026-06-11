# LESSON NAME: M17 Lesson 4 – Huffman coding

# ==========================================
# ACTIVITY 1: Beginner Level
# Problem Statement: Build a basic binary tree node layout helper class 
# to represent structural relationships within a frequency dictionary tree map.
# ==========================================
class HuffmanBaseNode:
    def __init__(self, character, frequency):
        self.char = character
        self.freq = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Comparison logic for tracking nodes inside prioritized sequences
        return self.freq < other.freq

print("--- Activity 1: Custom Structural Node Constructor ---")
node1 = HuffmanBaseNode('A', 5)
node2 = HuffmanBaseNode('B', 12)
print(f"Is Node1 frequency value lower than Node2 parameter check? {node1 < node2}")
print("-" * 40)

# ==========================================
# ACTIVITY 2: Intermediate Level
# Problem Statement: Implement the full greedy Huffman compression algorithm using standard min-heaps 
# to build a prefix tree codebook from an input character frequency mapping.
# ==========================================
import heapq

class HuffmanCompressionEngine:
    def __init__(self):
        self.codebook = {}

    def _generate_codes_recursive(self, node, current_binary_string):
        if node is None: return
        
        # Leaf node identified containing target symbol character properties
        if node.char is not None:
            self.codebook[node.char] = current_binary_string
            return
            
        self._generate_codes_recursive(node.left, current_binary_string + "0")
        self._generate_codes_recursive(node.right, current_binary_string + "1")

    def build_prefix_encoder(self, frequency_dictionary):
        priority_heap = []
        for char, freq in frequency_dictionary.items():
            node = HuffmanBaseNode(char, freq)
            heapq.heappush(priority_heap, node)

        while len(priority_heap) > 1:
            left_child = heapq.heappop(priority_heap)
            right_child = heapq.heappop(priority_heap)
            
            merged_parent = HuffmanBaseNode(None, left_child.freq + right_child.freq)
            merged_parent.left = left_child
            merged_parent.right = right_child
            
            heapq.heappush(priority_heap, merged_parent)

        root_node = heapq.heappop(priority_heap)
        self._generate_codes_recursive(root_node, "")
        return self.codebook

print("\n--- Activity 2: Huffman Prefix Encoder Sorter ---")
frequency_map = {'e': 5, 'a': 9, 'f': 12, 'b': 13, 'c': 16, 'd': 45}
engine = HuffmanCompressionEngine()
compiled_codes = engine.build_prefix_encoder(frequency_map)
print("Generated Codebook Map Directory:")
for alphabet, binary_sequence in compiled_codes.items():
    print(f" -> Symbol Character '{alphabet}' mapped prefix stream value: {binary_sequence}")
print("-" * 40)

# ==========================================
# ACTIVITY 3: Advanced Level
# Problem Statement: Construct an advanced production-grade encoder tool that automatically calculates 
# bits savings metrics compared against standard uncompressed fixed-width 8-bit strings.
# ==========================================
def calculate_compression_efficiency_metrics(raw_text_string, codebook_directory):
    total_uncompressed_bits = len(raw_text_string) * 8
    
    total_compressed_bits = 0
    for character in raw_text_string:
        total_compressed_bits += len(codebook_directory[character])
        
    savings_percentage = ((total_uncompressed_bits - total_compressed_bits) / total_uncompressed_bits) * 100
    print(f"Compression Efficiency Profile Logs:")
    print(f" * Baseline Fixed ASCII Size Footprint: {total_uncompressed_bits} bits")
    print(f" * Huffman Variable Prefix Size Footprint: {total_compressed_bits} bits")
    print(f" * Aggregated Data Storage Space Saved: {savings_percentage:.2f}% reduction")

print("\n--- Activity 3: High-Performance Compression Analytics ---")
sample_text = "aaaaabbbbbbcccccccdddddddddddd"
text_freqs = {'a': 5, 'b': 6, 'c': 7, 'd': 12}
codes_dir = HuffmanCompressionEngine().build_prefix_encoder(text_freqs)
calculate_compression_efficiency_metrics(sample_text, codes_dir)
print("-" * 40)