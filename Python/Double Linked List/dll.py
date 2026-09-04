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

# Method to insert a new node in any position in the dll
    def insert(self, index, value):
        if index < 0 or index > self.length: 
            return None
        if index == 0 or not self.head: 
            self.prepend(value)
        elif index == self.length: 
            self.append(value)
        else: 
            new_node = Node(value)
            previous_node = self.get(index-1)
            next_node = previous_node.next 
            new_node.previous = previous_node
            new_node.next = next_node
            next_node.previous = new_node 
            previous_node.next = new_node
        self.length += 1
        return True

# Method to remove the fist node of the dll
    def pop_first(self): 
        if not self.head: 
            return None
        removed_node = self.head 
        if self.head == self.tail: 
            self.head = None
            self.tail = None
        else: 
            self.head = removed_node.next 
            removed_node.next.previous = None
            removed_node.next = None
        self.length -= 1
        return removed_node

# Method to remove the last element of the dll
    def pop(self): 
        if not self.head: 
            return None
        removed_node = self.tail
        if self.head == self.tail: 
            self.head = None
            self.tail = None
        else: 
            self.tail = removed_node.previous 
            self.tail.next = None 
            removed_node.previous = None 
        self.length -= 1
        return removed_node

 # Method to remove any node from the dll           
    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return None

        if index == 0: 
            return self.pop_first()

        if index == self.length -1: 
            return self.pop()

        removed_node = self.get(index)
        removed_node.previous.next = removed_node.next 
        removed_node.next.previous = removed_node.previous 
        removed_node.next = None
        removed_node.previous = None
        self.length -= 1
        return removed_node


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
dll.append(43)
dll.append(89)
print(dll)
# dll.traverse()
# dll.reverse_traverse() 
print("Search:", dll.search(20))
print("Get:", dll.get(2).value)
dll.set(1, 50)
print(dll)
dll.insert(4, 222)
print(dll)
dll.pop_first()
print("Pop_First:", dll)
dll.pop()
print("Pop: ", dll)
dll.remove(4)
print("Remove:", dll)
dll.reverse()
print(dll)

