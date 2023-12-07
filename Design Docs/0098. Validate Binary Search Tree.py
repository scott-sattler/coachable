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
        """
        last_seen = [float('-inf'), True]
        self._isValidBST(root, last_seen)
        return last_seen[1]

    # noinspection PyPep8Naming
    def _isValidBST(self, node, last_seen) -> bool:
        if not node:
            return True

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

    # # noinspection PyPep8Naming
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     # todo: write stack implementation
