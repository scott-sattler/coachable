# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_nodes = ListNode(None, None)
        p2 = odd_nodes

        p1 = head
        odd = True
        while p1.next:
            if odd:
                p2.next = p1.next  # move odd to odd list
                p2 = p2.next  # increment odd list
                p1.next = p1.next.next  # restructure evens list
                odd = False  # flip
            else:
                p1 = p1.next
                odd = True

        p1.next = odd_nodes.next  # link two lists
        p2.next = None  # remove potential loops

        return head
