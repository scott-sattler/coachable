from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # noinspection PyPep8Naming
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        uses implicit data structure
        O(n) stack space -> O(1)
        still O(n) call stack space tho
        """
        last_seen = [float('-inf'), True]
        self._isValidBST(root, last_seen)
        return last_seen[1]

    # noinspection PyPep8Naming
    def _isValidBST(self, node, last_seen) -> None:
        if not node:
            return None

        self._isValidBST(node.left, last_seen)

        if node.val <= last_seen[0]:
            last_seen[1] = False
        last_seen[0] = node.val

        self._isValidBST(node.right, last_seen)


class OtherSolutions:
    # noinspection PyPep8Naming
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last_seen = [float('-inf')]
        return self._isValidBST(root, last_seen)

    # noinspection PyPep8Naming
    def _isValidBST(self, node, last_seen) -> bool:
        if not node:
            return True

        if not self._isValidBST(node.left, last_seen):
            return False

        if node.val <= last_seen[0]:
            return False
        last_seen[0] = node.val

        if not self._isValidBST(node.right, last_seen):
            return False

        return True

    ###########################################################################
    # stack solution

    # validate the BST property
    # root, left child, right child
    # left < root < right

    # traversed the BST in-order,
    # store in stack
    # verify correct order
    # by looking to see if i < i+1

    # O(n) time; O(n) aux. space (stack)

    # noinspection PyPep8Naming,PyRedeclaration
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = list()

        # create in-order stack
        self._isValidBST(root, stack)

        # valid stack is increasing
        i = 1
        while i < len(stack):
            if not stack[i - 1] < stack[i]:
                return False
            i += 1

        return True

    # noinspection PyPep8Naming,PyRedeclaration
    def _isValidBST(self, node: Optional[TreeNode], stack) -> None:
        # base case
        if not node:
            return None

        # traverse left child
        self._isValidBST(node.left, stack)

        # add to stack
        stack.append(node.val)

        # traverse right child
        self._isValidBST(node.right, stack)



