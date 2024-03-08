# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return head

        prehead = ListNode(None, head)

        # find midpoint
        slow = fast = prehead
        while fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next

        # reverse second half
        curr = slow.next
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow.next = prev

        # interweave/splice
        p1 = head
        p2 = slow.next
        while p2 and p1:
            slow.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p1.next.next
            p2 = slow.next

        return head
