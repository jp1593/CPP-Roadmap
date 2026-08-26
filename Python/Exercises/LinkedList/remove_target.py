"""
Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy
        current_node = head 
        while current_node:
            if current_node.val == val: 
                prev_node.next = current_node.next 
            else: 
                prev_node = current_node 
            current_node = current_node.next 
        return dummy.next


def print_list(node):
    curr = node
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

solution = Solution()
head = ListNode(1,ListNode(2,ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))),),)
# head = ListNode(7, ListNode(7, ListNode(7, ListNode(7, ))))
remove_elements = solution.removeElements(head, 6)
print_list(remove_elements)


