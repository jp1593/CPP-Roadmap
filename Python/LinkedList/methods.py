class Node: 
    def __init__(self, value=None): 
        self.value = value
        self.next = None

class SinglyList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# Method to get all the nodes values in the linked list
    def traverse(self): 
        current = self.head
        while current: 
            print(current.value, end=" ")
            current = current.next

# Method to get the index of a node given it's value
    def search(self, target): 
        current = self.head
        index = 0
        while current:
            if current.value == target: 
                return index
            current = current.next
            index += 1 
        return -1

# Method to get the value of the node given it's index
    def get(self, index): 
        if index == -1: 
            return self.tail
        if index < 0 or index > self.length: 
            return None
        current  = self.head
        for _ in range(index): 
            current = current.next
        return current

# Method that given and index and a value it will change the value of the node in that index
    def set(self, index, new_value): 
        temp = self.get(index)
        if temp: 
            temp.value = new_value
            return True
        return False
            
# Method to add a node at the beginning of the list
    def prepend(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node

        # Method to add node at the beggining fo the Linked List 
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node

        # Method to add node at the end fo the Linked List 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, value): 
        new_node = Node(value)
        if index < 0 or index > self.length: 
            return False
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
            return
        elif index == 0: 
            new_node.next = self.head
            self.head = new_node
        else: 
            temp_node = self.head
            for _ in range(index-1): 
                temp_node = temp_node.next
            new_node.next = temp_node.next 
            temp_node.next = new_node 

            if index == self.length:
                self.tail = new_node 

        self.length += 1
        return True

    # Method that eliminates the first node of the linked list and return that node. 
    def pop_first(self): 
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            removed_node = self.head 
            self.head = self.head.next
            removed_node.next = None
        self.length -= 1
        return  removed_node

    # Method that eliminates the last node and returns it
    def pop(self): 
        if self.length == 0: 
            return None
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            removed_node= self.tail
            temp = self.head
            while temp.next is not self.tail: 
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return removed_node
    
    # String representation of an Instance
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None: 
            result += str(temp_node.value)
            if temp_node.next is not None: 
               result += '-->'
            temp_node = temp_node.next
        return result

# Linked list creation
linked_list = SinglyList() 

# Insertion and append of nodes
linked_list.insert(6, 50)
linked_list.append(107)
linked_list.append(70)
linked_list.append(88)
linked_list.append(63)
linked_list.append(575)
linked_list.prepend(1)
linked_list.insert(6, 50)
# Information to be printed
linked_list.traverse()
print("\nHead:", linked_list.head.value,"Tail:",  linked_list.tail.value)
print(linked_list) 
print("Search:", linked_list.search(63))
print("Get:", linked_list.get(-1))
print(linked_list.set(-1, 22))
print(linked_list)
print(linked_list.pop_first())
print(linked_list)
print(linked_list.pop())
print(linked_list)


