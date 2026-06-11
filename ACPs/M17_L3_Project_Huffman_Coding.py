# Module 17 Lesson 3: After-Class Project
# Project Name: Huffman Text Compression Framework Encoder Engine

import heapq

class HuffmanEncodingNode:
    def __init__(self, symbol, frequency):
        self.char, self.freq = symbol, frequency
        self.left = self.right = None
    def __lt__(self, comparative_node): return self.freq < comparative_node.freq

def build_huffman_lookup_dictionary(text_symbols_frequency_map):
    heap = [HuffmanEncodingNode(char, freq) for char, freq in text_symbols_frequency_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap); n2 = heapq.heappop(heap)
        merged_node = HuffmanEncodingNode(None, n1.freq + n2.freq)
        merged_node.left, merged_node.right = n1, n2
        heapq.heappush(heap, merged_node)
        
    codes_lookup_table = {}
    def recursive_compile_bits(node, active_bitstring):
        if not node: return
        if node.char: codes_lookup_table[node.char] = active_bitstring
        recursive_compile_bits(node.left, active_bitstring + "0")
        recursive_compile_bits(node.right, active_bitstring + "1")
        
    if heap: recursive_compile_bits(heap[0], "")
    return codes_lookup_table

if __name__ == "__main__":
    freqs = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
    print(f"Compiled Huffman Bit Allocation Maps Profiles: {build_huffman_lookup_dictionary(freqs)}")