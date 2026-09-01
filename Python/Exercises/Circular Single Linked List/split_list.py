"""
Split a Circular Linked List into Two Equal Halves

Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, the extra node should go to the first list.  
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def split_list(self):
        current_node = self.head 
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        if self.length == 0: 
            first_list = None
            second_list = None
        else: 
            for _ in range(self.length): 
                if first_list.length != -(self.length // -2): 
                    first_list.append(current_node.value)
                else: 
                    second_list.append(current_node.value)
                current_node = current_node.next
        return first_list, second_list


# Instantiate the circular singly linked list
csll = CSLinkedList()

# Add nodes to the list
csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)
csll.append(5)

# Print the original circular linked list
print("Original List:")
print(csll)

# Call the split_list function
first_half, second_half = csll.split_list()

# Display results
print("\nFirst List:", first_half)
print("Second List:", second_half)

