############################ first solution ############################ # noqa
# hashmap + (unnecessary) array
# O(n) time/space

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # traverse linked list
        # hashing nodes and recording order

        node_index_inp = {None: 0}
        node_array_copy = [None]

        curr_copy = Node(head.val)
        copy_head = curr_copy

        i = 1
        curr_inp = head
        while curr_inp:
            if curr_inp.next:
                curr_copy.next = Node(curr_inp.next.val)

            node_index_inp[curr_inp] = i
            node_array_copy.append(curr_copy)

            curr_copy = curr_copy.next
            curr_inp = curr_inp.next
            i += 1

        curr_copy = copy_head
        curr_inp = head
        while curr_inp:
            next_i = node_index_inp[curr_inp.random]
            curr_copy.random = node_array_copy[next_i]

            curr_inp = curr_inp.next
            curr_copy = curr_copy.next

        return copy_head
