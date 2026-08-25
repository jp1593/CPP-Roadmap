"""
Merge Two Sorted Linked List

You are given the heads of two sorted linked lists list1 and list2. 

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.   

Example 1: 

Input: list1 = [1,2,4], list2 = [1,3,4]

Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []

Output: []

Example 3: 

Input: list1 = [], list2 = [0]

Output: [0]


Constraints: 

The number of nodes in both lists is in the range [0, 50].

-100 <= Node.val <= 100

Both list1 and list2 are sorted in non-decreasing order. 
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        tail = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val: 
                tail.next = l1
                l1 = l1.next
            else: 
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next

# Build List 1: [1 -> 2 -> 4]
l1 = ListNode(1, ListNode(2, ListNode(4)))

# Build List 2: [1 -> 3 -> 4]
l2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_head = solution.mergeTwoLists(l1, l2)
current = merged_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next