"""
Remove Duplicates from a Singly Linked List

Given a singly linked list, write a function that removes all the duplicates. use this linked list .

Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

Result Linked List - "1 -> 2 -> 4 -> 3
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
    
    def remove_duplicates(self):
        values_set = set()
        previous_node = None
        current = self.head
        for _ in range(self.length): 
            next_node = current.next 
            if current.value in values_set: 
                previous_node.next = next_node
                current.next = None
            else: 
                values_set.add(current.value) 
                previous_node = current
            current = next_node
        self.tail = previous_node






linked_list = LinkedList() 
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
print(linked_list)
linked_list.remove_duplicates()
print(linked_list)
print(linked_list.head.value, linked_list.tail.value)