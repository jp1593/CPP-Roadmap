"""
Insert into a Sorted Circular Linked List

Write a function to insert a new node into a sorted circular linked list. 
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
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def insert_into_sorted(self, data):
        new_node = Node(data)
        current_node = self.head 
        if self.head == None or self.head.data >= new_node.data: 
            self.prepend(data)
            return
        else: 
            while current_node.next != self.head:  
                if new_node.data >= current_node.data and new_node.data <= current_node.next.data: 
                    new_node.next = current_node.next 
                    current_node.next = new_node 
                    break 
                else: 
                    current_node = current_node.next 
            if current_node.next == self.head: 
                self.append(data)
                return

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))



# Instantiate the circular singly linked list
csll = CircularLinkedList()

# Add nodes to the list

# Add nodes to the list
csll.append(1)
csll.append(3)
csll.append(3)

csll.insert_into_sorted(3)
csll.print_list()