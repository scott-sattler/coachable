###############################################################################
# live loom solution
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prehead = ListNode(None, head)
        p1 = prehead

        # position pointer before the first
        # value greater than or equal to x
        while p1.next.val < x:
            p1 = p1.next
            # input is already partitioned
            if not p1.next:
                return head

        # find the next value less than x
        p2 = p1
        while p2.next:
            # insert lesser values after p1
            if p2.next.val < x:
                move = p2.next  # temp pointer
                p2.next = p2.next.next  # remove p2
                move.next = p1.next  # stitch p2->
                p1.next = move  # stitch ->p2
                p1 = p1.next  # stability
            else:
                p2 = p2.next

        return prehead.next
