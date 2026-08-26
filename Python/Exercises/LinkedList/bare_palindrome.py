"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def copy_list(self, head):
        if not head:
            return None
        return ListNode(head.val, self.copy_list(head.next))
    
    def reversed(self, head): 
        prev_node = None 
        current_node = head 
        while current_node: 
            next_node = current_node.next 
            current_node.next = prev_node 
            prev_node = current_node 
            current_node = next_node
        return prev_node

    def isPalindrome(self, head):
        reversed_list = self.reversed(self.copy_list(head))
        while reversed_list and head: 
            if reversed_list.val == head.val: 
                reversed_list = reversed_list.next 
                head = head.next 
            else: 
                return False
        return True

solution = Solution()
head = ListNode(1,ListNode(2,ListNode(3, ListNode(1,)),),)
is_palindrome = solution.isPalindrome(head)
print(is_palindrome)