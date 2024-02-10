from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # noinspection PyPep8Naming
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_maximum = [0]
        self.rec(root, current_maximum)
        return current_maximum[0]

    def rec(self, node, curr_max):
        # base case(s)
        if not node:
            return 0
        if not node.left and not node.right:
            return 1

        # recursive case(s)
        left = self.rec(node.left, curr_max)
        right = self.rec(node.right, curr_max)

        # if the current node max is larger
        # than previously found, update maximum
        if left + right > curr_max[0]:
            curr_max[0] = left + right

        return max(left, right) + 1
