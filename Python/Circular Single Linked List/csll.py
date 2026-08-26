class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList: 
# Constructor for only one element in the CSLL 
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node 
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

cslinkedlist = CSLinkedList()
print(cslinkedlist.head, cslinkedlist.tail)