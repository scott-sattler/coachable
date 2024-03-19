###############################################################################
# live solution
# time: O(n)
# space: O(1)

'''

reverse sublists
    prev <-
    while
    next_node = curr.next
    curr.next = prev
    curr = next_node

count
group_size


                             |-----------------|
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -|
  |         |              |
                              ^


find if group exists
    probe group distance
    if count not equal to group size:
        assign group size the count

if group is even
    reverse

traverse

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _reverse(self, pre_head, post_tail):
        tail = pre_head.next
        prev = post_tail
        curr = pre_head.next
        while curr != post_tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        pre_head.next = prev
        return tail

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        count = 1
        group_size = 2

        left = right = None
        probe = head
        while probe.next:
            # determin if full group exists
            left = probe
            probe = left.next
            while probe.next and count < group_size:
                count += 1
                probe = probe.next
            if count < group_size:
                group_size = count
            right = probe.next

            # reverse or traverse to next
            if group_size % 2 == 0:
                probe = self._reverse(left, right)

            count = 1
            group_size += 1

        return head
