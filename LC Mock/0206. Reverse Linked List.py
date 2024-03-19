###############################################################################
# live iterative solution
# time: O(n)
# space: O(1)

'''

1 -> 2 -> 3 -> 4 -|
=>
4 -> 3 -> 2 -> 1 -|

# iterative solution:
initialize prev as last.next (None)
while on a node
    record next
    reassign next to previous
    record previous
    reassign current to next
return current


# recursive solution:
parameters:
    previous (current)
    node recursed into

base case(s):
    if next is null
    return current
recursive case(s):
    fn(next)


<-   <-   <-   <-
1 -> 2 -> 3 -> 4 -|
               ^

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


###############################################################################
# recursive solution
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
        return self._hf(head, None)

    def _hf(self, node, previous):
        if not node:
            return previous

        next_node = node.next
        node.next = previous

        return self._hf(next_node, node)


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
