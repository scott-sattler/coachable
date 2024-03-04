###############################################################################
# live loom
# time: O(n + m)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # null input edge cases
        if not list1:
            return list2
        elif not list2:
            return list1

        # make list1 (p1) primary
        if list1.val > list2.val:
            list1, list2 = list2, list1

        # merge the secondary with primary
        p1, p2 = list1, list2
        prev = p1
        while p1 and p2:
            if p1.val <= p2.val:
                prev = p1
                p1 = p1.next
            else:  # (p1.val > p2.val)
                prev.next = p2
                p2 = p2.next
                prev.next.next = p1
                prev = prev.next

        if p2:
            prev.next = p2

        # return primary
        return list1
