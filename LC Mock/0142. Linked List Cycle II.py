########################## more clear variant ########################## # noqa

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Floyd's Cycle Detection
        slow = head
        fast = head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # find cycle entry node
        probe = head
        while probe != slow:
            probe = probe.next
            slow = slow.next

        return probe


############################ first solution ############################ # noqa

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Floyd's Cycle Detection
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # acyclic test
        if not fast or not fast.next:
            return None

        # find cycle entry node
        probe = head
        while probe != slow:
            probe = probe.next
            slow = slow.next

        return probe
