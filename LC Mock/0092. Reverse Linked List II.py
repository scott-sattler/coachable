###############################################################################
# live practice
# time: O(n)
# space: O(1)

'''
left = 2
right = 4
             .         .
preh -> 1 -> 2 -> 3 -> 4 -> 5
        ^    ^

preh -> 1 |- 2 <- 3 <- 4    5
        ^              ^    ^

preh -> 1 -> 4 -> 3 -> 2 -> 5


1 -> 2 -> 3 -> 4 -> 5 -|
^                   ^  ^
.    .
1 -> 2

# edge cases:
    if not head.next or right == left:
        return head

    - reversing the entire list

# traverse to (left - 1)
# reverse from left to right (right - left +? 1)
# link the surrounding nodes
# return prehead.next

time: O(n)
space: O(1)

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or right == left:
            return head

        prehead = ListNode(None, head)
        pre_rev = prehead

        # traverse to (left - 1)
        for _ in range(left - 1):
            pre_rev = pre_rev.next

        # reverse from left to right
        # (right - (left - 1))
        curr = pre_rev.next
        prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # link the surrounding nodes
        pre_rev.next.next = next_node
        pre_rev.next = prev

        return prehead.next


###############################################################################
# live solution
# time: O(c*n) -> O(n), where c is (right - left)
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
