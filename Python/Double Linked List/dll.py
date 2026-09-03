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

# Method to access each node in the dll 
    def traverse(self): 
        current_node = self.head 
        while current_node: 
            print(current_node.value)
            current_node = current_node.next 

# Method to traverse the dll from the end to the beggining
    def reverse_traverse(self): 
        current_node = self.tail 
        while current_node: 
            print(current_node.value)
            current_node = current_node.previous

# Method to reverse the dll references
    def reverse(self): 
        current_node = self.tail 
        origin_head = self.head 
        origin_tail = self.tail
        while current_node: 
            next = current_node.next 
            prev = current_node.previous 
            current_node.next = prev 
            current_node.previous = next 
            current_node = current_node.next 
        self.tail = origin_head
        self.head = origin_tail 

# Method that searches if there is a node with the given value inside the dll (or returns the index instead of the boolean)
    def search(self, value):
        current_node = self.head  
        index = 0
        while current_node: 
            if current_node.value == value: 
                return index
                # return True (optional if it will be implemented with the boolean)
            current_node = current_node.next 
            index += 1
        return -1
        # return False (optional if it will be implemented with the boolean) 

#  Method to get the value of the node given and index 
    def get(self, index): 
        if index >= self.length or index < 0: 
            return None
        if index < self.length // 2: 
            current_node = self.head 
            for _ in range(index): 
                current_node = current_node.next
        else: 
            current_node = self.tail 
            for _ in range(self.length-1, index, -1): 
                current_node = current_node.previous
        return current_node

# Method to set a new value to a specific node based on it's position
    def set(self, index, value): 
        target_node = self.get(index)
        if target_node: 
            target_node.value = value
            return True
        return False


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
dll.append(20)
dll.append(3)
dll.prepend(100)
print(dll)
# dll.traverse()
# dll.reverse_traverse() 
print("Search:", dll.search(20))
print("Get:", dll.get(2).value)
dll.set(1, 50)
print(dll)
dll.reverse()
print(dll)

