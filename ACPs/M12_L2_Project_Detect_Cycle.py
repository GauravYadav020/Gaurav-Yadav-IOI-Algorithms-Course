# Module 12 Lesson 2: After-Class Project
# Project Name: Floyds Tortoise and Hare Cycle Identification Matrix

def identify_linked_list_loop(head_node):
    slow_ptr = fast_ptr = head_node
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr: return True
    return False

if __name__ == "__main__":
    from M12_L1_Project_Singly_Linked_List import Node
    root = Node(10); root.next = Node(20); root.next.next = root  # Form cycle loops structure
    print(f"Cycle anomaly tracked in link structure graph? {identify_linked_list_loop(root)}")