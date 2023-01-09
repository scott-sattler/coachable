from __future__ import annotations
# from treenode import TreeNode
# from narytreenode import NaryTreeNode

from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class NaryTreeNode:
  def __init__(self, val, children):
    self.val = val
    self.children = children

'''
Questions 1-4 use the TreeNode class in treenode.py.
The test tree looks like the following
                   1
                 /   \
                2     3
               / \   / \
              4  5  6   7
'''

'''
Question 1. Write a function to traverse the tree in an inorder fashion,
returning a list of node values in the order the nodes were traversed.
Traverse the left side then the right side. 
'''


def question1(node: TreeNode) -> list[int]:
    return _question1(node, list())


def _question1(node: TreeNode, nodes: list[int]) -> None | list[int]:
    if node is None:
        return None

    _question1(node.left, nodes)
    nodes.append(node.val)
    _question1(node.right, nodes)

    return nodes


'''
Question 2. Write a function to traverse the tree in an preorder fashion,
returning a list of node values in the order the nodes were traversed.
Traverse the left side then the right side. 
'''


def question2(node: TreeNode) -> list[int]:
    return _question2(node, list())


def _question2(node, nodes):
    if node is None:
        return None

    nodes.append(node.val)
    _question2(node.left, nodes)
    _question2(node.right, nodes)

    return nodes


'''
Question 3. Write a function to traverse the tree in an postorder fashion,
returning a list of node values in the order the nodes were traversed.
Traverse the left side then the right side. 
'''


def question3(node: TreeNode) -> list[int]:
    return _question3(node, list())


def _question3(node, nodes):
    if node is None:
        return None

    _question3(node.left, nodes)
    _question3(node.right, nodes)
    nodes.append(node.val)

    return nodes


'''
Question 4. Write a function to traverse the tree in an breadth first search fashion,
returning a list of node values in the order the nodes were traversed.
In each level, traverse from left to right.
'''


def question4(node: TreeNode) -> list[int]:
    # ... is binary tree ... ?

    output = []
    agenda = deque()
    agenda.append(node)

    while agenda:
        current_node = agenda.popleft()
        output.append(current_node.val)
        if current_node.left is not None:
            agenda.append(current_node.left)
        if current_node.right is not None:
            agenda.append(current_node.right)

    return output


'''
Question 5. Write a function that returns the size of each subtree
in an n-ary tree. Return the answer as a normal dictionary, not defaultdict.

See the NaryTreeNode class in narytreenode.py for the definition.
The test tree looks like the following
                 A
               / | \
              B  C  D
                   / \
                  E   F
'''


def question5(nary_node: NaryTreeNode) -> dict[str, int]:
    # postorder running sum ?
    print(_question5(nary_node, dict()))
    return _question5(nary_node, dict())


def _question5(nary_node, subtree_sums):
    if nary_node is None:
        return 1

    level_sum = 0
    for each_child in nary_node.children:
        _question5(each_child, subtree_sums)
        if each_child.val in subtree_sums:
            level_sum += subtree_sums[each_child.val]

    subtree_sums[nary_node.val] = level_sum + 1

    return subtree_sums






root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

def test_question1_case1():
  assert question1(root) == [4,2,5,1,6,3,7]

def test_question1_case2():
  assert question1(root) == [4,2,5,1,6,3,7]

def test_question2_case1():
  assert question2(root) == [1,2,4,5,3,6,7]

def test_question2_case2():
  assert question2(root) == [1,2,4,5,3,6,7]

def test_question3_case1():
  assert question3(root) == [4,5,2,6,7,3,1]

def test_question3_case2():
  assert question3(root) == [4,5,2,6,7,3,1]

def test_question4_case1():
  assert question4(root) == [1,2,3,4,5,6,7]

def test_question4_case2():
  assert question4(root) == [1,2,3,4,5,6,7]

nary_root = NaryTreeNode("A", [NaryTreeNode("B", []), NaryTreeNode("C", []), NaryTreeNode("D", [NaryTreeNode("E", []), NaryTreeNode("F", [])])])

def test_question5_case1():
  assert question5(nary_root) == {"A": 6, "B": 1, "C": 1, "D": 3, "E": 1, "F": 1}

def test_question5_case2():
  assert question5(nary_root) == {"A": 6, "B": 1, "C": 1, "D": 3, "E": 1, "F": 1}







test_question1_case1()
assert question1(root) == [4,2,5,1,6,3,7]

test_question1_case2()
assert question1(root) == [4,2,5,1,6,3,7]

test_question2_case1()
assert question2(root) == [1,2,4,5,3,6,7]

test_question2_case2()
assert question2(root) == [1,2,4,5,3,6,7]

test_question3_case1()
assert question3(root) == [4,5,2,6,7,3,1]

test_question3_case2()
assert question3(root) == [4,5,2,6,7,3,1]

test_question4_case1()
assert question4(root) == [1,2,3,4,5,6,7]

test_question4_case2()
assert question4(root) == [1,2,3,4,5,6,7]

nary_root = NaryTreeNode("A", [NaryTreeNode("B", []), NaryTreeNode("C", []), NaryTreeNode("D", [NaryTreeNode("E", []), NaryTreeNode("F", [])])])

test_question5_case1()
assert question5(nary_root) == {"A": 6, "B": 1, "C": 1, "D": 3, "E": 1, "F": 1}

test_question5_case2()
assert question5(nary_root) == {"A": 6, "B": 1, "C": 1, "D": 3, "E": 1, "F": 1}