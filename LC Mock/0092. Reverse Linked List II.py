###############################################################################
# live solution
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or right - left < 1:
            return head

        prehead = ListNode(None, head)
        right = right - left + 2

        # position left bound (exclusive)
        l_bound = prehead
        while left > 1:
            l_bound = l_bound.next
            left -= 1

        # position right bound (exclusive)
        r_bound = l_bound
        while right > 0:
            r_bound = r_bound.next
            right -= 1

        # reverse between bounds
        curr = l_bound.next
        prev = r_bound
        while curr != r_bound:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        l_bound.next = prev

        return prehead.next
