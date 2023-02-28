"""
Week 5 Practice: Trees and Tries

Free Response Questions

Trees

    Explain what a binary tree is using a recursive definition.
        a data structure that is traversed using two recursive calls, one for each left and right child
        the traversal method, pre, post, and in order, is determined by the position of node inspection
        preorder inspects the current node first, then makes both recursive calls
        postorder recurses the left and right children, then inspects the current node
        inorder inspects the current node between the left and right recursive calls
        level order uses BFS with a queue

    What are the different traversals that we can do on a binary tree?
        pre/post/in/level order

    Your friend claims that “the time complexity of traversing a tree recursively is O(n), where n is the number of
    nodes in the tree.” Are they correct? Why/why not?
        yes.

    Your friend claims that “the worst-case space complexity of traversing a tree recursively is O(1), because we are
    not using extra space to hold a queue like a BFS would.” Are they correct? Why/why not? What if the tree is
    balanced?
        no. worst case of a tree would 1 node per level, effectively a linked list, which produces a call stack of O(n)
        balanced tree: worst case call stack is O(log(n))

    What is the difference between a binary tree and a binary search tree (BST)?
        a binary tree is an unordered graph where every node has, at most, two children; permits duplicates; O(n) runtime
        binary search tree imposes order: relative to parent node, left is < and right is >; no duplicates; O(n) runtime
        note: BSTs can handle duplicates via node lists, or comparison operator and significant algorithm modification
        balanced binary search trees exhibit O(log(n)) runtime

    What is the runtime of searching for an element in a BST? What about the space complexity?
        unbalanced: O(n) runtime; O(n) auxiliary: maximum call stack
        balanced: O(log(n)) runtime; O(log(n)) auxiliary: maximum call stack

    What’s the “worst” BST structure given the numbers [1,2,3,4,5], in terms of number of nodes visited to search for
    the existence of 6?
        unbalanced: 1 -> 2 -> 3 -> 4 -> 5
           1
         /  \
        null 2
            / \
          null 3
               ...

    What’s the “worst” BST structure given the numbers [1,2,3,4,5], in terms of number of nodes visited, to search for
    the existence of 0?
        unbalanced: 5 -> 4 -> 3 -> 2 -> 1
            5
           / \
          4  null
         / \
        3  null
        ...

    What’s the “best” BST structure, given the numbers [1,2,3,4,5,6,7], in terms of the expected number of nodes visited
    to search for the existence of an arbitrary positive or negative number?
        O(log(n)) structure (bisected)
                 4
               /   \
              2     6
            /  \   / \
           1   3  5   7

    If I want to compute the size of each subtree in a tree, which traversal(s) could I use? If some do not work,
    explain why not.
        postorder makes the process easier... but I'm not sure other methods would be impossible to implement (just
        impractical)


        def fn(node):
            if not node:
                return 0

            count = 0
            count += fn(node.left)
            count += fn(node.right)
            sub_count[node.val] = count

            return count + 1

    If I wanted to print out the tree node values level by level, which traversal(s) could I use? If some do not work,
    explain why not
        preferably level order, or BFS...

    If I wanted to sum all the node values in the tree, which traversal(s) could I use? If some do not work, explain
    why not
        pre/in/post/level/bfs
        all traversals that visit each node work; all traversals work

    If I wanted to sum all the node values in each subtree in a tree, which traversal(s) could I use? If some do not
    work, explain why not.
        postorder


Tree Traversals Orderings

    Give the preorder, postorder, inorder, and level order traversals for each of the following trees. Assume that 
    children are processed left to right.

    1. Binary Tree
    
        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7
               \
                8

    preorder:       1 2 4 3 5 6 7 8
    postorder:      4 2 6 8 7 5 3 1
    inorder:        4 2 1 3 6 5 7 8
    level order:    1 2 3 4 5 6 7 8

    2. N-Ary Tree (Nodes can have more than 2 children)
    
         1
       / | \
      2  3   4
     /  / |   \
    5  6  7    8
       |     /  \
       9    10   11
            | \   \
           12  13  14

    preorder:       1 2 5 3 6 9 7 4 8 10 12 13 11 14
    inorder:        5 2 9 6 3 7 1 4 8 12 10 13 11 14
    postorder:      5 2 9 6 7 3 12 13 10 14 11 8 4 1
    level order:    1 2 3 4 5 6 7 8 9 10 11 12 13 14

Identifying Recursive Relationships

    Notice: These exercises are new and quite challenging.
    
    Please ask us on Slack immediately if you have questions about these problems.
    
    Please identify the base case and recurrence relationship for the following relationships in binary trees. For each 
    question, please answer the following.
    
        a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
        understanding of the question.
        
        b. Base Case - When does the recursion stop?
        
        c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can describe
        this with an equation or in English - whichever is more effective at communicating your approach.
        
        d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of these
        as test cases - we will be pretty critical if your proposed solution does not work on the provided examples.
        
        e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree? Does
        the same solution work? If not, what additional changes need to be made?
    
    Here is an example of size(root) computing the size of a binary tree. Please complete the rest following this
    format.

    Example Binary Trees

        Binary Tree A
            8
           / \
          3   10
         / \    \
        1   6    14
           / \   /
          4   7 12


        Binary Tree B
            1
             \
              2
               \
                3
                 \
                  4
                   \
                    5

        Binary Tree C
                1
             /     \
            2       3
           / \     / \
          4   5    6  7
         / \ / \
        8  9 10 11


        Binary Tree D
              1
             / \
            2   2
           / \ / \
          4  5 5  4


        Binary Tree E
              1
             / \
            2   3
           / \   \
          4   5   6
         /         \
        10          8
                     \
                      9



    1. Example. size(root) finds the number of nodes in a binary tree. For case A, size(A) = 9 since there are 9 nodes
    in the tree.
        a. size(B) = 5, size(C) = 11, size(D) = 7, size(E) = 9
        b. Base Case: if root is None: return 0 in other words size(None) = 0
        c. Recurrence Relation: size(root) = size(left) + size(right) + 1
        d. Yes: Verified. size(left/3) = 5, size(right/10) = 3, size(root) = 5+3+1 = 9 You should verify all 5 of them.
        e. A similar solution works but instead. size(root) = 1 + sum(root.child) for each child node.

    2. sum(root) finds the sum of all the nodes in the binary tree. size(A) = 1+3+8+6+4+&+10+14+12= 65
        a. sum(A) = 65; sum(B) = 15; sum(C) = 66; sum(D) = 23; sum(E) = 48
        b. Base Case: if sum(input) ("root") is None: return 0
        c. Recurrence Relation: sum(root) = sum(left) + sum(right) + current
        d. Yes: Verified. sum(A; root) = 8 + (3 + 1 + 6 + 4 + 7) + (10 + 14 + 12) = 8 + 21 + 36 = 65
        e. Similar but not identical solution works; recursive calls must be made for each child (n-children).

    3. max(root) finds the maximum value among all nodes in a binary tree. max(A) = 14 since it is the largest element
    in the tree.
        a. max(A), ... max(E) = 14, 5, 11, 5, 10
        b. Base Case: if max(input) ("root") is None: return float('-inf')
        c. Recurrence Relation: max(root) = max(max(left), max(right), current)
        d. Yes: Verified. max(A; root) = max(7, ... max(12, -inf, 14), 8) -> 14
        e. Similar but not identical solution works; recursive calls must be made for each child (n-children).

    4. is_symmetric(root) returns True if the tree is symmetric and False if it is not. is_symmetric(A) = False and
    is_symmetric(D) = True. A tree is symmetric if the left and right subtrees are mirror images of each other.
        a. is_symmetric(A) ... is_symmetric(E) =
        b. Base Case: if is_symmetric(input) ("root") is None: return None
        c. Recurrence Relation: is_symmetric(root) = is_symmetric(left), is_symmetric(right)
        d.
        e.

    5. height(root) finds the height of the tree. The distance from the root to the lowest child. height(A) = 3 because
    12 is 3 levels down from the 8.

    6. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may
    or may not pass through the root of the tree. diameter(root) finds the diameter of this tree. diameter(A) = 6
    because the path from 4 or 7 to 12  has length 6.

    7. leafs(root) calculates the number of leaves in a binary tree. leafs(A)=4 because 1,4,7,12 are all leaf nodes.
    Recall leaf nodes are nodes with no children.

    8. top_ordered(root) returns True if the root of every subtree is the smallest element in its subtree.
    top_ordered(E) = True because every Node, it is smaller than the elements in its subtree. top_ordered(A) = False
    because 3 is larger than its left child of 1.

    9. find_height(root, k) determines the number of nodes that have height k. find_height(A, 2) = 3 because of 1,6,14
    are the nodes with height 2. find_height(any non empty tree, 0) = 1 because it will be just the root (assuming the
    tree is not empty)

    10. sum_only_child(root) determines the number of nodes with exactly one child. sum_only_child(A) = 36 because
    10,14,12 are the nodes with one child, and their sum if 36.

    11. level_min(root, height) determines the node of minimum value height equal to the given height.
    level_min(A, 0) = 8,level_min(A,1) = 3, level_min(A,2) = 1

    12. full(root) determines if a binary tree is full. A binary tree is said to be full if every node has 0 or 2
    children. full(D) = True, full(A) = False

    13. same(root_a, root_b) returns True if root_a and root_b represent the same binary tree and False otherwise. Your
    recurrence will require you to use both root_a, root_b as inputs. same(A, A) = True, same(A,B) = False

    14. Challenge Question. almost_same(root_a, root_b, k) returns True if root_a and root_b represent the same binary
    tree except the k of the values can be different. Suppose we're using example A. If k=1 then you can replace the
    value of the root in 0A to 20 instead of 5. We have a modified version of A call this  Z , then you would have
    almost_same(A, Z, 1) = True but almost_same(A, Z, 0) = False . The latter is False because A differs from Z in the
    root value. If the tree structure is any different, i.e. you find None in one tree at the same position as a Node in
    the other tree, then return False. If k = 0 , then the output should be equivalent to same function in the previous
    problem. Namely, almost_same(root_a, root_b,0) == same(root_a, root_b) .

Tries

    General

        What is a trie?
            a data structure used to efficiently store and find strings and certain stubstrings (e.g. prefixes)
            a trie typically has, at each node, a boolean and a hashmap of subsequent chars

        When do we use a trie?
            when you want performant string lookups, where the strings may overlap (e.g. str, string, strings)
            note: for 'overlap' to occur, string subsequences need to start with a similar sequence of at least one char

        How do we know that “dog” is an actual word in our trie and is not just a prefix of the word “doghouse”?
            the boolean, which can be either an explicit boolean attached to the given node, or implicitly via specific
            hash key

        Suppose our dictionary has n words and the longest of them is m characters long. What is the time and space
        complexity of building our trie?
            O(n*m) runtime; O(n * m) space
            note: a major advantage of tries occurs when strings 'overlap'

    Building a Trie

        Start with an empty trie and insert the words "hello", "help", "held", "helden", "helderman", "helping" into
        this trie. Draw the resulting trie in tree structure.
             'h'
              |
             'e'
              |
             'l'
          /   |   \
        'd'  'l'  'p'
         |    |
        'e'  'o'
       /  \
     'n'  'r'
           |
          'm'
           |
          'a'
           |
          'n'

        Trace through how you would search for "helping" in this trie.
            'h' -> 'e' -> 'l' -> 'p' -> 'i' -> 'n' -> 'g', bool?

        Trace how you would find all words starting with the prefix "he" in this Trie.
            'h' -> 'e', .keys(), exhaustively traverse each subsequent edge of 'e', record word when bool is True.


"""