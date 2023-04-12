from __future__ import annotations


class Node:
    def __init__(self, val: int, next_node: Node) -> None:
        self.val = val
        self.next_node = next_node


'''
Write a function to insert into the front a LinkedList and returns the head.
'''


# O(1) runtime; O(1) aux space
def insert_front(head: Node, val: int) -> Node:
    new_node = Node(val, head)
    head = new_node
    return head


'''
Write a function that returns a string representation of the list.
Format-wise, for an input Node(1, Node(2, Node(3, None))) you must return
1 -> 2 -> 3
'''


# O(n) runtime; O(n) aux space
def str_list(head: Node) -> str:
    str_rep_list = []
    while head:
        str_rep_list.append(f"{head.val}{' -> ' if head.next_node else ''}")
        head = head.next_node

    return ''.join(str_rep_list)


'''
Write a function that inserts to the end of a linked list and returns the head.
'''


# O(n) runtime; O(1) aux space
def insert_end(head: Node, val: int) -> Node:
    new_node = Node(val, None)
    pointer = head
    while pointer.next_node:
        pointer = pointer.next_node
    pointer.next_node = new_node
    return head


'''
Write a function that returns the size of the linked list
'''


# O(n) runtime; O(1) aux space
def get_size(head: Node) -> int:
    count = 0
    while head:
        count += 1
        head = head.next_node
    return count


'''
Write a function that determines if a linked list has a cycle, given the head of the list.
'''


# Floyd's Cycle Detection
# O(n) runtime; O(1) aux space
def has_cycle(head: Node) -> bool:
    slow = head
    fast = head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node

        if fast == slow:
            return True

    return False


'''
Given the head of a circular linked list, write a method to sum all elements of the list up. 
Assume all the values of the node are integers.
'''


# O(n) runtime; O(n) aux space
def get_circular_list_sum(head: Node) -> int:
    visited = {}
    total = 0

    while head and (head not in visited):
        visited[head] = 0
        total += head.val
        head = head.next_node

    return total


# ##############################
# ########## testing ###########
# ##############################


l1_head = Node(1, Node(2, Node(3, None)))

l2_head = Node(1, Node(2, Node(3, None)))
new_l2_head = insert_front(l2_head, 0)

l3_head = Node(1, Node(2, Node(3, None)))
new_l3_head = insert_end(l3_head, 4)

l4_head = Node(1, None)

last_node_of_l5 = Node(3, None)
l5_head = Node(1, Node(2, last_node_of_l5))
last_node_of_l5.next_node = l5_head


l1_head = Node(1, Node(2, Node(3, None)))

l2_head = Node(1, Node(2, Node(3, None)))
new_l2_head = insert_front(l2_head, 0)

l3_head = Node(1, Node(2, Node(3, None)))
new_l3_head = insert_end(l3_head, 4)

l4_head = Node(1, None)

last_node_of_l5 = Node(3, None)
l5_head = Node(1, Node(2, last_node_of_l5))
last_node_of_l5.next_node = l5_head

def test_str_list_1():
  assert str_list(l1_head) == "1 -> 2 -> 3"

def test_str_list_2():
  assert str_list(new_l2_head) == "0 -> 1 -> 2 -> 3"

def test_str_list_3():
  assert str_list(new_l3_head) == "1 -> 2 -> 3 -> 4"

def test_get_size_1():
  assert get_size(l4_head) == 1

def test_get_size_2():
  assert get_size(l1_head) == 3

def test_has_cycle_1():
  assert has_cycle(l1_head) == False

def test_has_cycle_2():
  assert has_cycle(l5_head) == True

def test_get_circular_list_sum_1():
  assert get_circular_list_sum(l5_head) == 6


import pytest

# do not modify this function call
retcode = pytest.main(['-v'])