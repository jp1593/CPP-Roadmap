class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0

# Method to add new node at the end of the dll
    def append(self, value): 
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node 
        else: 
            new_node.previous = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1

# Method to add a new node at the beginning of the dll
    def prepend(self, value): 
        new_node = Node(value)
        if not self.head: 
            self.head = new_node 
            self.tail = new_node
        else: 
            new_node.next = self.head 
            self.head.previous = new_node 
            self.head = new_node
        self.length += 1

# Method to print the node values of the hole list
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next 
            if temp_node == None: 
                break
            result += ' <-> '
        return result
            

dll = DoubleLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(100)
print(dll)