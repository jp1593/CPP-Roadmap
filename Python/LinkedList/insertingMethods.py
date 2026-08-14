class Node: 
    def __init__(self, value=None): 
        self.value = value
        self.next = None

class SinglyList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node

        # Method to add node at the beggining fo the Linked List 
        else: 
            previous_head = self.head
            self.head = new_node
            self.head.next = previous_head
        self.length += 1

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

    # String representation of an Instance
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None: 
            result += str(temp_node.value)
            if temp_node.next is not None: 
               result += '-->'
            # self.head.next = temp_node
            temp_node = temp_node.next
        return result

linked_list = SinglyList() 
linked_list.append(107)
linked_list.append(70)
linked_list.append(88)
linked_list.append(63)
linked_list.prepend(1)
print(linked_list) 




            


