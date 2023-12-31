# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if root is None:
            return None

        # check the current node
        if root.val is p.val or root.val is q.val:
            return root

        # recurse children
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # when the current node is the LCA
        if left and right:
            return root

        # when the current node is between LCA
        # and p or q
        if left or right:
            return left if left else right

        return None
