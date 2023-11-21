from __future__ import annotations
from typing import *

'''
Find the max difference in height among all leaf nodes.


1                  1
| | | | | | | | | / \
2                2   3
| | | | | | | | / \
3              4   5
| | | | | | | /
4            8

This tree would have

height() == 4 (Node 8)
lowest_leaf_height() == 2 (Node 3)
max_leaf_height_diff() == 2 (Difference between heights of 8 and 3 is 2)

'''


class TreeNode:
    def __init__(self, val: int, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

    # Returns the height of the binary tree.
    def height(self) -> int:
        return self._height(self)

    def _height(self, root) -> int:
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1

    # Returns the lowest height of any leaf in a binary tree.
    def lowest_leaf_height(self) -> int:
        return self._lowest_leaf_height(self)

    def _lowest_leaf_height(self, node) -> int:
        if node is None:
            return 0
        return min(self._lowest_leaf_height(node.left), self._lowest_leaf_height(node.right)) + 1

    # Finds the max difference in height between 2 leaf nodes.
    def max_leaf_height_diff(self) -> int:
        # height level always contains at least 1 leaf
        return self.height() - self.lowest_leaf_height()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

# height() == 4 (Node 8)
# lowest_leaf_height() == 2 (Node 3)
# max_leaf_height_diff() == 2 (Difference between heights of 8 and 3 is 2)

print(root.height())
print(root.lowest_leaf_height())
print(root.max_leaf_height_diff())
