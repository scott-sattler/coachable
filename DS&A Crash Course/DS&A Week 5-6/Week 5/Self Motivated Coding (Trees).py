

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


"""
                3
        40               2
    7       5       6       10

   45
52   18
"""

# tree_7 = TreeNode(7, None, None)
# tree_5 = TreeNode(5, None, None)
# tree_6 = TreeNode(6, None, None)
# tree_10 = TreeNode(10, None, None)
#
# tree_40 = TreeNode(40, tree_7, tree_5)
# tree_2 = TreeNode(2, tree_6, tree_10)
#
# tree_root = TreeNode(3, tree_40, tree_2)

tree_root = TreeNode(3, None, None)
tree_root.left = TreeNode(40, None, None)
tree_root.left.left = TreeNode(7, None, None)
tree_root.left.right = TreeNode(5, None, None)
tree_root.right = TreeNode(2, None, None)
tree_root.right.left = TreeNode(6, None, None)
tree_root.right.right = TreeNode(10, None, None)


output = []


def traverse(node):
    if not node:
        return None

    output.append(node.val)
    traverse(node.left)
    traverse(node.right)


traverse(tree_root)
print(output)

