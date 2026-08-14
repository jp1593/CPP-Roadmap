class Node: 
    def __init__(self, value=None): 
        self.value = value
        self.next = None

class SinglyList: 
    def __init__(self):
        self.head = None
        self.tail = None

singlyLinkedList = SinglyList() 
node_1 = Node(1)
node_2 = Node(2)

singlyLinkedList.head = node_1
singlyLinkedList.head.next = node_2
singlyLinkedList.tail = node_2

