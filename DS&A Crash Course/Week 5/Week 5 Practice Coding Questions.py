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


def create_BST() -> TreeNode:
    pass


'''
Write a function to perform a preorder traversal on the BT and return the preorder as a list.
'''


def preorder_traversal(root: TreeNode) -> list[int]:
    pass


'''
Write a function to perform an inorder traversal on the BT and return the inorder as a list. 
'''


def inorder_traversal(root: TreeNode) -> list[int]:
    pass


'''
Write a function to perform a postorder traversal on the BT and return the postorder as a list.
'''


def postorder_traversal(root: TreeNode) -> list[int]:
    pass


'''
Write a function to perform a level by level order traversal on the BT.
'''


def level_order_traversal(root: TreeNode) -> list[list[int]]:
    pass


'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''


def get_k_smallest_elements(root: TreeNode, k: int) -> list[int]:
    pass


'''
Write a function to perform a traversal where we return the k largest elements in descending order in this BST.
'''


def get_k_largest_elements(root: TreeNode, k: int) -> list[int]:
    pass


'''
Complete the following Trie class.  
insert(word: str) -> None
word_exists(word: str) -> bool i.e. if our dictionary contains “doghouse”, the word “doghouse” exists but the word “dog” does not.
prefix_exists(prefix: str) -> bool i.e. if our dictionary contains “doghouse”, “dog” and “doghouse” would both be prefixes of some word(s) in our dictionary (and thus return True).
'''


class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        pass

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pass

    def word_exists(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pass

    def prefix_exists(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pass


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
