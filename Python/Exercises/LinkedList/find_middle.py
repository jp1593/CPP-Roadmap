"""
Middle of a Singly Linked List

Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        current = self.head 
        if self.length == 0: 
            return None
        for _ in range(self.length//2): 
            current = current.next 
        return current
    
linked_list = LinkedList() 
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
print(linked_list)
print(linked_list.find_middle())