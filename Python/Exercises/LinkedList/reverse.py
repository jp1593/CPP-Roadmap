"""
Reverse a Singly Linked List

Write a function to reverse a singly linked list. The function should reverse the original linked list.

Example:

Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5

Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1
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
        
    def reverse(self):
        prev_node = None
        current_node = self.head
        for _ in range(self.length):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node 
            current_node = next_node
        self.tail = self.head
        self.head = prev_node


linked_list = LinkedList() 
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
print(linked_list)
linked_list.reverse()
print(linked_list)
print(linked_list.head.value, linked_list.tail.value)