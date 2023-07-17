# import pytest
#
# # do not modify this function call
# retcode = pytest.main(['-v'])


from __future__ import annotations


# from treenode import TreeNode
# from __future__ import annotations

class TreeNode:
    def __init__(self, value: int, left: TreeNode = None, right: TreeNode = None) -> None:
        self.value = value
        self.left = left
        self.right = right


'''
Create a BT that looks like this and return the root.
         3         
       /   \        
      2     6     
    /     /   \    
   1     5     7 

For example, you your code should do the following.

root = create_BST() 
print(x.value) # Prints 3.
print(x.left.value) # Prints 2

You only need to construct the above tree and return the root of that tree.
'''


# value: int, left: TreeNode= None, right: TreeNode= None)
def create_BST() -> TreeNode:
    node1 = TreeNode(1)
    node5 = TreeNode(5)
    node7 = TreeNode(7)

    node2 = TreeNode(2, node1)
    node6 = TreeNode(6, node5, node7)

    head = TreeNode(3, node2, node6)

    return head


'''
Write a function to perform a preorder traversal on the BT and return the preorder as a list.
'''


def preorder_traversal(root: TreeNode) -> list[int]:
    preorder_return = list()
    _preorder_traversal(root, preorder_return)
    return preorder_return


def _preorder_traversal(node, preord_list) -> None:
    if not node:
        return

    preord_list.append(node.value)
    if node.left:
        _preorder_traversal(node.left, preord_list)
    if node.right:
        _preorder_traversal(node.right, preord_list)


'''
Write a function to perform an inorder traversal on the BT and return the inorder as a list. 
'''


def inorder_traversal(root: TreeNode) -> list[int]:
    inorder_return = list()
    _inorder_traversal(root, inorder_return)
    return inorder_return


def _inorder_traversal(node, inord_list) -> None:
    if not node:
        return

    if node.left:
        _inorder_traversal(node.left, inord_list)
    inord_list.append(node.value)
    if node.right:
        _inorder_traversal(node.right, inord_list)


'''
Write a function to perform a postorder traversal on the BT and return the postorder as a list.
'''


def postorder_traversal(root: TreeNode) -> list[int]:
    postorder_return = list()
    _postorder_traversal(root, postorder_return)
    return postorder_return


def _postorder_traversal(node, postord_list) -> None:
    if not node:
        return

    if node.left:
        _postorder_traversal(node.left, postord_list)
    if node.right:
        _postorder_traversal(node.right, postord_list)
    postord_list.append(node.value)


'''
Write a function to perform a level by level order traversal on the BT.
'''


# def level_order_traversal(root: TreeNode) -> list[list[int]]:
#   from collections import deque
#   levelorder_return = list()
#   agenda = deque([root])

#   while agenda:
#     node = agenda.popleft()
#     levelorder_return.append(node.value)
#     if node.left:
#       agenda.append(node.left)
#     if node.right:
#       agenda.append(node.right)

#   return levelorder_return


def level_order_traversal(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    seed = [root]
    level_order_return = list()
    _level_order_traversal(seed, level_order_return)
    return level_order_return


def _level_order_traversal(node_list, final_return: list[list]) -> None:
    if len(node_list) < 1:
        return

    level_list = list()
    for level_node in node_list:
        level_list.append(level_node.value)

    final_return.append(level_list)

    found_children = list()
    for child in node_list:
        if child.left:
            found_children.append(child.left)
        if child.right:
            found_children.append(child.right)
    _level_order_traversal(found_children, final_return)


'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''


def get_k_smallest_elements(root: TreeNode, k: int) -> list[int]:
    # inorder
    k_smallest = list()
    _inorder(root, k_smallest, k)
    return k_smallest


def _inorder(node, k_small, k):
    if len(k_small) >= k:
        return

    if node.left:
        _inorder(node.left, k_small, k)

    if len(k_small) < k:
        k_small.append(node.value)
    else:
        return

    if node.right:
        _inorder(node.right, k_small, k)


'''
Write a function to perform a traversal where we return the k largest elements in descending order in this BST.
'''


def get_k_largest_elements(root: TreeNode, k: int) -> list[int]:
    # previous solution modified to traverse right first
    k_largest = list()
    _k_largest_hf(root, k_largest, k)
    return k_largest


def _k_largest_hf(node, k_large, k):
    if len(k_large) >= k:
        return

    if node.right:
        _k_largest_hf(node.right, k_large, k)

    if len(k_large) < k:
        k_large.append(node.value)

    if node.left:
        _k_largest_hf(node.left, k_large, k)


'''
Complete the following Trie class.  
  insert(word: str) -> None

  word_exists(word: str) -> bool
  i.e. if our dictionary contains “doghouse”, the word “doghouse” exists but the word “dog” does not.

  prefix_exists(prefix: str) -> bool
  i.e. if our dictionary contains “doghouse”, “dog” and “doghouse” would both be prefixes of some word(s) in our 
  dictionary (and thus return True).
'''


class Trie:
    '''
        c            a            t
    dict node -> dict node -> dict node -> dict node (is_prefix t in cat)
    '''
    is_prefix = 'is_prefix'

    def __init__(self) -> None:
        # implicit data structure
        # prefix: {str: bool}
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pointer = self.root
        for char in word:
            if char in pointer:
                pointer = pointer[char]
                continue
            else:  # todo
                pointer[char] = {self.is_prefix: False}
                pointer = pointer[char]
        else:
            pointer[self.is_prefix] = True

    def word_exists(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pointer = self.root
        i = 0
        while i < len(word) and word[i] in pointer:
            pointer = pointer[word[i]]
            i += 1
        return pointer[self.is_prefix]

    def prefix_exists(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.root
        for char in prefix:
            if char in pointer:
                pointer = pointer[char]
            else:
                return False

        return True


'''file: main_test.py'''

# from stencil import *
# from treenode import TreeNode

root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(6, TreeNode(5), TreeNode(7)))

inorder = [1, 2, 3, 5, 6, 7]
preorder = [3, 2, 1, 6, 5, 7]
postorder = [1, 2, 5, 7, 6, 3]
level_order = [[3], [2, 6], [1, 5, 7]]


def test_create_bst():
    new_bst = create_BST()
    assert new_bst.value == 3
    assert new_bst.left.value == 2
    assert new_bst.left.left.value == 1
    assert new_bst.left.left.left is None
    assert new_bst.right.value == 6
    assert new_bst.right.right.value == 7
    assert new_bst.right.left.value == 5


def test_preorder_traversal_1():
    assert preorder_traversal(root) == preorder


def test_inorder_traversal_1():
    assert inorder_traversal(root) == inorder


def test_postorder_traversal_1():
    assert postorder_traversal(root) == postorder


def test_level_order_traversal_1():
    assert level_order_traversal(root) == level_order


def test_level_order_traversal_2():
    assert level_order_traversal(None) == []


def test_get_k_smallest_elements_1():
    assert get_k_smallest_elements(root, 4) == [1, 2, 3, 5]


def test_get_k_largest_elements_1():
    assert get_k_largest_elements(root, 4) == [7, 6, 5, 3]


trie = Trie()
trie.insert("doghouse")


def test_trie_word_exists_1():
    assert trie.word_exists("doghouse") == True


def test_trie_word_exists_2():
    assert trie.word_exists("dog") == False


def test_trie_word_exists_3():
    assert trie.word_exists("dogs") == False


def test_trie_prefix_exists_1():
    assert trie.prefix_exists("dog") == True


def test_trie_prefix_exists_2():
    assert trie.prefix_exists("dogs") == False


'''file: secondary_test.py'''

# from stencil import *
# from main_test import *


def test_get_k_smallest_elements_3():
  assert get_k_smallest_elements(root, 0) == []

def test_get_k_smallest_elements_4():
  assert get_k_smallest_elements(root, 1) == [1]

def test_get_k_smallest_elements_5():
  assert get_k_smallest_elements(root, 2) == [1, 2]

def test_get_k_smallest_elements_6():
  assert get_k_smallest_elements(root, 6) == [1, 2, 3, 5, 6, 7]

def test_get_k_smallest_elements_7():
  assert get_k_smallest_elements(root, 7) == [1, 2, 3, 5, 6, 7]

def test_get_k_smallest_elements_8():
  assert get_k_smallest_elements(root, 999) == [1, 2, 3, 5, 6, 7]