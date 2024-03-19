'''
count size
calculate target: size // 2
reset count
count size 0-indexed - 1
remove
return head

1 node: 1 // 2 -> 0
2 node: 2 // 2 -> 1
3 node: 3 // 2 -> 1
4 node: 4 // 2 -> 2
5 node: 5 // 2 -> 2


0    1    2    3    4    5    6    7    8
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -|

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -|
               ^ (x - 1)
1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -|

9 // 2 -> 4


0    1    2    3    4
1 -> 2 -> 3 -> 4 -> 5 -|


solutions:
traverse to get count OR
fast/slow pointers


0    1    2    3    4
1 -> 2 -> 3 -> 4 -> 5 -|
          ^
                    ^

0    1    2    3
1 -> 2 -> 3 -> 4 -|
          ^
                  ^


1 2 3 4

0    1    2    3    4
1 -> 2 -> 3 -> 4 -> 5 -|
^
^

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        prev = dhead = ListNode(None, head)

        while True:
            if not fast or not fast.next:
                break
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return dhead.next
