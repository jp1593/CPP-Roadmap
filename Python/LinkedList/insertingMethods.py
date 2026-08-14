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
            new_node.next = self.head
            self.head = new_node
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

    def insert(self, index, value): 
        new_node = Node(value)
        if index < 0 or index > self.length: 
            return False
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
            return
        elif index == 0: 
            new_node.next = self.head
            self.head = new_node
        else: 
            temp_node = self.head
            for _ in range(index-1): 
                temp_node = temp_node.next
            new_node.next = temp_node.next 
            temp_node.next = new_node 

            if index == self.length:
                self.tail = new_node 

        self.length += 1
        return True
    # String representation of an Instance
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None: 
            result += str(temp_node.value)
            if temp_node.next is not None: 
               result += '-->'
            temp_node = temp_node.next
        return result

linked_list = SinglyList() 
linked_list.insert(6, 50)
linked_list.append(107)
linked_list.append(70)
linked_list.append(88)
linked_list.append(63)
linked_list.append(575)
linked_list.prepend(1)
linked_list.insert(6, 50)
print(linked_list.head.value, linked_list.tail.value)
print(linked_list) 




            


