# Module 12 Lesson 6: After-Class Project
# Project Name: Linked List Sequence Symmetry Validation Infrastructure

def verify_linked_list_palindrome(head_node):
    data_buffer = []
    curr = head_node
    while curr:
        data_buffer.append(curr.data)
        curr = curr.next
    return data_buffer == data_buffer[::-1]

if __name__ == "__main__":
    from M12_L1_Project_Singly_Linked_List import Node
    pal = Node('A'); pal.next = Node('B'); pal.next.next = Node('A')
    print(f"Is linkage structure a mirrored palindrome configuration? {verify_linked_list_palindrome(pal)}")