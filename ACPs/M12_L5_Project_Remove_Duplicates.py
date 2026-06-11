# Module 12 Lesson 5: After-Class Project
# Project Name: Linked List Deduplication Matrix Optimization Framework

def purge_duplicate_nodes(head_node):
    curr = head_node
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr.curr = curr.next
    return head_node

if __name__ == "__main__":
    from M12_L1_Project_Singly_Linked_List import Node
    root = Node(5); root.next = Node(5); root.next.next = Node(10)
    purge_duplicate_nodes(root)
    print(f"Deduplicated linkage configuration state: {root.next.data}")