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


    ############################# PRACTICE ############################# # noqa


    class Solution:
        # stack with O(n) space penalty
        # noinspection PyPep8Naming
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            in_order = list()
            self.hf(root, in_order)

            for i in range(1, len(in_order)):
                if in_order[i] < in_order[i - 1]:
                    return False
            return True

        def hf(self, node, stack):
            # base case
            if not node:
                return

            # in-order traversal
            self.hf(node.left, stack)
            stack.append(node.val)
            self.hf(node.right, stack)

    # noinspection PyRedeclaration
    class Solution:
        # failure transmitter with mutable parameter O(1) space
        # noinspection PyPep8Naming,PyRedeclaration
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            # visit inorder and verify current
            # element is always increasing
            prev = [float('-inf')]  # mutable argument
            return self.hf(root, prev)

        # failure transmitter
        # noinspection PyRedeclaration
        def hf(self, node, prev):
            # base case(s)
            if not node:
                return True

            # inorder traversal
            if not self.hf(node.left, prev):
                return False

            # verify order
            if not prev[0] < node.val:
                return False
            # update last visited
            prev[0] = node.val

            if not self.hf(node.right, prev):
                return False

            return True

    # noinspection PyRedeclaration
    class Solution:
        # mutable parameter w/o transmitter with O(1) space
        # noinspection PyRedeclaration,PyPep8Naming
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            last_seen = [float('-inf'), True]  # [last val, valid]
            self.hf(root, last_seen)
            return last_seen[1]

        # noinspection PyRedeclaration
        def hf(self, node, last_seen):
            # base case(s)
            if not node:
                return

            # in-order traversal
            self.hf(node.left, last_seen)
            if not last_seen[0] < node.val:
                last_seen[1] = False
            last_seen[0] = node.val
            self.hf(node.right, last_seen)
