"""
Delete a Node from a Circular Singly Linked List

Implement a method in the CircularLinkedList class to delete a node by value. 
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
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        current_node = self.head
        previous_node = None
        if self.length == 0: 
            return False 
        for _ in range(self.length):
            if current_node.value == value: 
                if self.length == 1: 
                    self.head = None
                    self.tail = None
                elif current_node == self.head: 
                    self.head = current_node.next
                    current_node.next = None 
                    self.tail.next = self.head         
                elif current_node == self.tail: 
                    self.tail.next = None 
                    self.tail = previous_node 
                    self.tail.next = self.head    
                else: 
                    previous_node.next = current_node.next 
                    current_node.next = None 
                self.length -= 1
                return True
            else: 
                previous_node = current_node 
                current_node = current_node.next 
        return False
            
csll = CSLinkedList() 
csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)
print(csll)
csll.delete_by_value(4)
print(csll)
print(csll.head.value, csll.tail.value, csll.length)
