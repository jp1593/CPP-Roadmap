class Node: 
    def __init__(self, value=None): 
        self.value = value
        self.next = None

class SinglyList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            
        # Method to add node at the end fo the Linked List 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

linked_list = SinglyList() 
print(linked_list.length)
linked_list.append(107)
print(linked_list.length)
linked_list.append(70)
print(linked_list.length)
print(linked_list.head.value)
print(linked_list.tail.value)



            


