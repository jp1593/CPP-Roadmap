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

    def prepend(self, value): 
        new_node = Node(value)
        if not self.head: 
            new_node.previous = new_node 
            new_node.next = new_node 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.head.previous = new_node 
            self.tail.next = new_node 
            new_node.next = self.head 
            new_node.previous = self.tail 
            self.head = new_node
        self.length += 1

    def traverse(self): 
        if not self.head: 
            return
        current_node = self.head 
        while True: 
            print(current_node.value)
            current_node = current_node.next 
            if current_node == self.head: 
                break

    def __str__(self):
        if self.length == 0: 
            return ""
        current_node = self.head 
        values = []
        while current_node.next is not self.head: 
            values.append(str(current_node.value))
            current_node =  current_node.next 
        values.append(str(current_node.value))
        return " <-> ".join(values) 

cdll = CircularDoubleLinkedList()
cdll.append(10)
cdll.append(20)
cdll.prepend(51)
cdll.append(30)
print(cdll)
cdll.traverse()