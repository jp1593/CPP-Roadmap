"""
Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        count = 0 
        current = head

        while current: 
            count += 1
            current = current.next 

        for _ in range(count // 2): 
            head = head.next 
        return head

solution = Solution()
head = ListNode(1,ListNode(2,ListNode(3, ListNode(1,ListNode(5))),),)
middle = solution.middleNode(head)
print(middle)