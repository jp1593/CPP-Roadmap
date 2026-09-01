"""
Count the Number of Nodes

Add a method to count the number of nodes in the circular singly linked list. 
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
    
    def count_nodes(self): 
        current_node = self.head 
        count = 0
        while True: 
            if self.head == None and self.tail == None: 
                return 0
            count += 1
            current_node = current_node.next
            if current_node == self.head: 
                break 
        return count

csll = CSLinkedList() 
csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)
print(csll)
print(csll.count_nodes())


