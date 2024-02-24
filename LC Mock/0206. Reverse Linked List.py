###############################################################################
# iterative solution
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
