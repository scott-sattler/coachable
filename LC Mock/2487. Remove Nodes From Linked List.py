'''

5 -> 1 -> 2 -> 13 -> 3 -> 8
=>
13 -> 8

strictly decreasing linked list

stack solution:
[5, 1, 2]
[5, 2]
[13]
[13, 3]
[13, 8]
link stack nodes

1 -> 1 -> 1 -> 1 -|
=>
1 -> 1 -> 1 -> 1 -|


dhead <-> 1 <-> 2 <-> 3 <-> 4 <-|
=>
dhead <-> 4 <-|

dhead <-> 13 <-> 8 -|



dhead -> 1 -> 2 -> 3 -> 4 -|


a degenerate case for multi-pass ?

         1    2    3    4    5    6    7    8    9
dhead -> 1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 4 -> 2 -> 1 -|
largest = 4
count =

traverse once, finding largest, rightmost, value
delete lesser nodes up to it
traverse


         1    2    3    4    5    6    7    8    9
dhead -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -|


         1    2    3    4    5    6    7    8    9
dhead -> 1 -> 9 -> 1 -> 8 -> 1 -> 7 -> 1 -> 6 -> 1 -|

dhead -> 9 -> 8 -> 7 -> 6 -> 1 -|

O(n^2)

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()

        # create monotonic
        # decreasing stack
        curr = head
        while curr:
            while stack and curr.val > stack[-1].val:
                stack.pop()
            stack.append(curr)
            curr = curr.next

        # link stack nodes
        head = stack[0]  # dereference old head
        stack.append(None)  # dereference last node
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        return head
