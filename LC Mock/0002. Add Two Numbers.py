# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        p1 = l1
        p2 = l2
        ## find longer linked list
        # traverse to end of shorter
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
        # assign p1 longer, p2 shorter
        if p1.next:
            head = p1 = l1
            p2 = l2
        else:
            head = p1 = l2
            p2 = l1
        ## mutate longer linked list
        carry = 0
        prev = p1
        while p2:
            # mutate p1 value
            p1p2 = p1.val + p2.val
            p1.val = (p1p2 + carry) % 10
            carry =  (p1p2 + carry) // 10
            # tarverse
            prev = p1
            p1 = p1.next
            p2 = p2.next
        # when shorter list is exhausted
        while p1 and carry > 0:
            p1c = p1.val + carry
            p1.val = p1c % 10
            carry = p1c // 10

            prev = p1
            p1 = p1.next
        # edge case: carry on last node of longer
        print(carry)
        if carry > 0:
            if not p1:
                prev.next = ListNode(carry)
            else:
                p1.val += carry

        return head
