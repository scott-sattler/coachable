# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = root
        self._invert(root)
        return head

    def _invert(self, node):
        if not node:
            return

        node.left, node.right = node.right, node.left
        self._invert(node.left)
        self._invert(node.right)
