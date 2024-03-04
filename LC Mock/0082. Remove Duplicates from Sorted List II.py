###############################################################################
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prehead = ListNode(None, head)
        p1 = prehead
        p2 = head.next

        while p2:
            # node values differ
            if p1.next.val != p2.val:
                p1 = p1.next
                p2 = p2.next
                continue

            # nodes require removal
            while p2 and p1.next.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p2 = p2.next if p2 else None

        return prehead.next
