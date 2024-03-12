'''

time: O(n)
space: O(n) stack

can we O(1) space?

iterative:
    while not child:
        increment

    if we have a child
    push next_node to stack

    insert/reassign pointers of children node

    when no next, pop from stack if exists
    point next_node in stack to current
    traverse to


recrusive:
    record next node from current
    # recursive case
    if child:
        link current and traverse to it
        prev = recurse(...) assign fn call to prev
    if prev: ?
        link prev to next
    traverse to next node

    # base case
    if not next:
        return curr_node

    return current node


head -> 1 <-> 2 <-> 3 -|
                    |
                    4 <-> 5

head -> 1 <-> 2 <-> 3 -None
                    |
                    4 <-> 6
                    |
                    5

head -> 1 <-> 2 <-> 3 -None
        |
        2
        |
        3

head -> 1 <-> 2 -None
        |
        3 <-> 4
        |
        5 <-> 6
        |
        7 <-> 8

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # head <-> nodes <-> tail
        head = Node(None, None, head, None)
        curr = head.next

        stack = list()

        while curr:
            # if current node has child
            # push next node to the stack
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None

            # if no next node, process stack
            # pop and link pop with current
            if not curr.next and stack:
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr

            curr = curr.next

        return head.next
