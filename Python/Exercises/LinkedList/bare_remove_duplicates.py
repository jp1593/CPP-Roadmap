"""
Remove Duplicates

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

Example 1:

    Input: head = [1,1,2]
    Output: [1,2]

Example 2:

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        check_duplicate = set()
        prev_node = None
        current = head
        while current is not None: 
            if current.val not in check_duplicate: 
                check_duplicate.add(current.val)
                prev_node = current
            else: 
                prev_node.next = current.next
            current = current.next
        return head

def print_list(node):
    curr = node
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next


solution = Solution()
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
duplicates_removal = solution.deleteDuplicates(head)
print_list(duplicates_removal)
