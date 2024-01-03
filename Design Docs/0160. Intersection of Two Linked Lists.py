from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # initialize pointers
        # initialize counters
        p1, p2 = headA, headB
        c1, c2 = 0, 0

        # find terminal nodes
        while p1.next:
            p1 = p1.next
            c1 += 1
        while p2.next:
            p2 = p2.next
            c2 += 1

        # return null in the absence
        # of an intersection
        if p1 != p2:
            return None

        # reset pointers and align at equal
        # distances to the intersecting node
        p1, p2 = headA, headB
        while c1 > c2:
            p1 = p1.next
            c1 -= 1
        while c2 > c1:
            p2 = p2.next
            c2 -= 1

        # traverse linked lists until
        # the intersecting node is found
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
