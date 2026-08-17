"""
Deletion from a Singly Linked List

Write a function to delete a node from a singly linked list and return deleted_node. The function should take the index(starting from 0) of the node to be deleted as a parameter. 
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

    def delete(self, index): 
        removed_node = self.head
        if index < 0 or index >= self.length: 
            return None
        if index == 0:  
            if self.length == 1: 
                self.head = None
                self.tail = None
            self.head = removed_node.next
            removed_node.next = None
        for i in range(index):  
            prev_node = removed_node
            removed_node = removed_node.next
            if (index-1) == i:
                if removed_node.next is None: 
                    self.tail = prev_node 
                    prev_node.next = None
                prev_node.next = removed_node.next 
                removed_node.next = None      
        self.length -= 1
        return removed_node

linked_list = LinkedList() 
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
print(linked_list)
print(linked_list.delete(4))
print(linked_list)