###############################################################################
# second attempt live
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if not head or not head.next:
            return head

        # inspect middle value
        # between prev and post
        prehead = ListNode(None, head)
        prev = prehead
        post = head.next

        while post:
            # no duplicates
            if prev.next.val != post.val:
                prev = prev.next
                post = post.next
                continue

            # remove duplicates
            while post and prev.next.val == post.val:
                post = post.next
            prev.next = post
            post = post.next if post else None

        return prehead.next


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

        # inspect middle value
        # between prev and post
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
