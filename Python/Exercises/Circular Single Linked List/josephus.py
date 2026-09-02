"""
Josephus Circle using Circular Linked List

Solve the Josephus problem using a circular linked list. Implement a function that takes the number of people n and the step rate k and returns the position of the last person standing.

Output: Last person left standing: 3  
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        current_node = self.head
        previous_node = self.head 

        while previous_node.next != self.head: 
            previous_node = previous_node.next 
                
        while True: 
            if current_node.next == current_node: 
                return f"Last person left standing: {current_node.data}"
            for _ in range(step-1): 
                previous_node = current_node
                current_node = current_node.next 
            previous_node.next = current_node.next 
            current_node = current_node.next 
            


    def __str__(self):
            temp_node = self.head 
            result = ''
            while temp_node is not None:  
                result += str(temp_node.data)
                temp_node = temp_node.next
                if temp_node == self.head: 
                    break  
                result += ' -> '
            return result

# --- EXECUTION ---
# Test 1: Standard case (n=5, k=2) -> Output: 3
clist1 = CircularLinkedList()
for i in range(1, 6): clist1.append(i)
print(clist1.josephus_circle(2)) 

# Test 2: Edge case (n=5, k=1) -> Output: 5
clist2 = CircularLinkedList()
for i in range(1, 6): clist2.append(i)
print(clist2.josephus_circle(1)) 

# Test 3: Larger group (n=7, k=3) -> Output: 4
clist3 = CircularLinkedList()
for i in range(1, 8): clist3.append(i)
print(clist3.josephus_circle(3))