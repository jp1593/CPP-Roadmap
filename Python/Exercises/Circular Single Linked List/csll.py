"""
Implement a Circular Singly Linked List

Create a circular singly linked list with methods to insert a new node at the beginning, end, and print  to display the list. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        current_node = self.head 
        all_nodes = ""
        for i in range(self.length):
            if i == self.length-1: 
                all_nodes += str(current_node)
            else: 
                all_nodes += str(current_node) + " -> "
            current_node = current_node.next 
        return all_nodes

    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
            new_node.next = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 
            new_node.next = self.head 
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
            new_node.next = new_node 
        else: 
            new_node.next = self.head 
            self.head = new_node 
            self.tail.next = new_node
        self.length += 1

csll = CSLinkedList() 
csll.append(2)
csll.append(3)
csll.prepend(1)
csll.append(4)
print(csll)
