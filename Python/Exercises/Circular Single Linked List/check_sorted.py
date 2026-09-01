"""
Check if a Circular Linked List is Sorted

Implement a function to check if the circular linked list is sorted in ascending order. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        if not self.head or self.head.next == self.head:
            return True
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False 
            current = current.next
        return True 




# Instantiate the circular singly linked list
csll = CircularLinkedList()

# Add nodes to the list
csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)
csll.append(5)

print(csll.is_sorted())

