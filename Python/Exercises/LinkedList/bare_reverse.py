""" 
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev_node = None
        current_node = head 
        while current_node: 
            next_node = current_node.next 
            current_node.next = prev_node 
            prev_node = current_node
            current_node = next_node
        return prev_node

def print_list(node):
    curr = node
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

solution = Solution()
head = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5,))),),)
reversed = solution.reverseList(head)
print_list(reversed)