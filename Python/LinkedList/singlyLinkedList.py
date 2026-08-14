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

'''
Why Node takes value in __init__: 
A Node exists for one main reason: to hold a piece of data.

When you create a new node, you almost always know what value you want to put inside it right away:
Python

node_1 = Node(1)  # "Create a node that holds the number 1"

Because you pass 1 into Node(...), Python needs a parameter in __init__ to catch that input



Why SinglyList does NOT take head or tail: 
When you create a brand-new linked list, it starts completely empty. An empty list has no first item (head) and no last item (tail)

Since a new list is always empty by default, you don't need to pass any arguments when creating it:

def __init__(self):
    self.head = None  # Starts empty
    self.tail = None  # Starts empty


    
What if SinglyList DID require head and tail?
Imagine if SinglyList.__init__ was written like this:
Python

# HYPOTHETICAL (Inconvenient Design)
class SinglyList:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

To use this, you would be forced to create your nodes before you could even create the list itself:
Python

node_1 = Node(1)
node_2 = Node(2)

# You can't create an empty list first!
my_list = SinglyList(node_1, node_2)



So: 
Parameters in __init__(self, ...) are for data you must or want to provide at the moment of creation (like the value in a Node).

Attributes inside __init__ set to None or default values are for setting up the object's initial starting state (like an empty list starting with head = None and tail = None).
'''