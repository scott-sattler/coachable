"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""

import math
from typing import Optional
import helper_functions as hf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # naive
    # traverse both lists, form numbers, add, create linked list
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # noqa: naming convention
        n1 = ""
        h1 = l1
        while h1.next is not None:
            n1 += str(h1.val)
            h1 = h1.next
        else:
            n1 += str(h1.val)

        n2 = ""
        h2 = l2
        while h2.next is not None:
            n2 += str(h2.val)
            h2 = h2.next
        else:
            n2 += str(h2.val)

        n1 = n1[::-1]
        n2 = n2[::-1]
        summed = int(n1) + int(n2)
        nums_to_list = list(str(summed))
        rev_nums_list = nums_to_list[::-1]

        # create linked list
        head = ListNode()
        dummy = head
        n = len(rev_nums_list)
        for i in range(n):
            head.val = rev_nums_list[i]
            if i + 1 < n:
                head.next = ListNode()
            head = head.next

        return dummy

    # second attempt (optimization attempt)
    # traverse both lists, form numbers, add, create linked list
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # noqa: naming convention
        # create return LL while traversing each LL

        head = ListNode()
        dummy = head
        l1_head = l1
        l2_head = l2
        carry = 0
        while (l1_head is not None) or (l2_head is not None) or (carry > 0):
            # control for different digit lengths
            # increment input lists
            if l1_head is None:
                l1_val = 0
            else:
                l1_val = l1_head.val
                l1_head = l1_head.next
            if l2_head is None:
                l2_val = 0
            else:
                l2_val = l2_head.val
                l2_head = l2_head.next
            val = l1_val + l2_val + carry
            carry = 0

            # control for sum > 9
            # bounds 0 - 18
            if val > 9:
                carry = 1
                val = val - 10

            head.next = ListNode()
            head = head.next
            head.val = val

        return dummy.next


num1 = [9, 9]
num2 = [9, 9]

print(99 + 99)

l1 = hf.create_linked_list(num1, reverse=True)
l2 = hf.create_linked_list(num2, reverse=True)

output = Solution().addTwoNumbers(l1, l2)
hf.print_linked_list(output, verbose=False)
