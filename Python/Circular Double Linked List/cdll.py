class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.previous = None

class CircularDoubleLinkedList: 
    def __init__(self):
        self.head = None 
        self.tail =  None 
        self.length = 0

    def append(self, value): 
        new_node = Node(value)
        if not self.head: 
            new_node.previous = new_node 
            new_node.next = new_node 
            self.head = new_node 
            self.tail = new_node 
        else: 
            new_node.previous = self.tail 
            new_node.next = self.head 
            self.head.previous = new_node
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1