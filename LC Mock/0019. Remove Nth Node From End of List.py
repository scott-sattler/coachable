# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(None, head)

        # position leading pointer
        while n > 0:
            right = right.next
            n -= 1

        # position delete pointer
        while right.next:
            right = right.next
            left = left.next

        # remove nth node
        left.next = left.next.next

        return dummy.next
