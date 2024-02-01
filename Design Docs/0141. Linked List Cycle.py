# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Floyd's Cycle Detection Algorithm
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # node-inequality loop invariant
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

        # # no-tail loop invariant
        # slow = head
        # fast = head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False
