class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value): 
        new_node = Node(value)
        if self.length == 0 : 
            self.head = new_node 
            self.tail = new_node
            new_node.next = new_node 
        else: 
            self.tail.next = new_node 
            self.tail = new_node 
            new_node.next = self.head
        self.length += 1

    def prepend(self, value): 
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
            new_node.next = new_node
        else: 
            new_node.next = self.head 
            self.head = new_node 
            self.tail.next = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node is not None:  
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head: 
                break  
            result += ' -> '
        return result
    
cslinkedlist = CSLinkedList()
cslinkedlist.append(1)
cslinkedlist.append(2)
cslinkedlist.append(3)
print(cslinkedlist)
cslinkedlist.prepend(20)
print(cslinkedlist)