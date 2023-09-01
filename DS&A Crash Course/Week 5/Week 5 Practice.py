'''
Week 5 Practice: Trees and Tries

Free Response Questions

Trees

    1. Explain what a binary tree is using a recursive definition.
        quote:
        The formal recursive definition is: a binary tree is either empty (represented by a null pointer), or is made of
        a single node, where the left and right pointers each point to a binary tree.

    2. What are the different traversals that we can do on a binary tree?
        pre-order
        in-order
        post-order
        level-order

    3. Your friend claims that “the time complexity of traversing a tree recursively is O(n), where n is the number of
    nodes in the tree.” Are they correct? Why/why not?
        yes; each node is only visited on the order of n times

    4. Your friend claims that “the worst-case space complexity of traversing a tree recursively is O(1), because we are
    not using extra space to hold a queue like a BFS would.” Are they correct? Why/why not? What if the tree is
    balanced?
        no; they're failing to account for the recursive call stack, which would result in O(height) space complexity
        a balanced tree would reduce the worst case O(height) space complexity from O(n) to O(log(n))

    5. What is the difference between a binary tree and a binary search tree (BST)?
        a binary tree is an undirected acyclic graph that contains a root null value or node, where each node contains
        two children as left and right pointers, with each being either null value or a node.

    6. What is the runtime of searching for an element in a BST? What about the space complexity?
        unbalanced: O(n) Θ(log n) Ω(1) time complexity; (O(n) input + O(1) auxiliary) space complexity
        balanced: O(log n) Θ(log n) Ω(1) time complexity; (O(n) input + O(1) auxiliary) space complexity

    7. What’s the “worst” BST structure given the numbers [1,2,3,4,5], in terms of number of nodes visited to search for
    the existence of 6?
        balanced:
                    2
                 1     3
                     4   5

        unbalanced:
                    1
                      2
                        3
                          4
                            5

        balanced: 3
        unbalanced: 5

    8. What’s the “worst” BST structure given the numbers [1,2,3,4,5], in terms of number of nodes visited, to search
    for the existence of 0?
        balanced:
                    4
                 3     5
              1   2

        unbalanced:
                    5
                  4
                3
              2
            1

        balanced: 3
        unbalanced: 5

    9. What’s the “best” BST structure, given the numbers [1,2,3,4,5,6,7], in terms of the expected number of nodes
    visited to search for the existence of an arbitrary positive or negative number?
        balanced:
                4
           3         5
         1   2     6   7

        always floor(log n) height (where root is height 0)

    10. If I want to compute the size of each subtree in a tree, which traversal(s) could I use? If some do not work,
    explain why not. Show how your approach works in Binary Tree A from the below section.
        post-order traversal

        left
        right
        sum

            1
           / \
          2   3
         /     \
        4       5
               / \
              6   7
                   \
                    8

        although postorder is best suited for this problem, you could inartfully use any traversal

        def subtree_sum(node) -> int:
            if node is None:
                return 0
            count += subtree_sum(node.left)
            count += subtree_sum(node.right)
            return count + 1

    11. If I wanted to print out the tree node values level by level, which traversal(s) could I use?   If some do not
    work, explain why not. Show how your approach works in Binary Tree A from the below section.
        level-order traversal

        from collections import deque

        def level_values(node) -> None:
            deq = deque([node])
            while deq:
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                print(node.val)

            1
           / \
          2   3
         /     \
        4       5
               / \
              6   7
                   \
                    8

        [1]
        [2, 3]
        print(1)
        [3, 4]
        print(2)
        [4, 5]
        print(3)
        [5]
        print(4)
        [6, 7]
        print(5)
        [7]
        print(6)
        [8]
        print(7)
        []
        print(8)

    12. If I wanted to sum all the node values in the tree, which traversal(s) could I use?  If some do not work,
    explain why not. Show how your approach works in Binary Tree A from the below section.
        any traversal that visits each node works equally well, given the stated constraints

    13. If I wanted to sum all the node values in each subtree in a tree, which traversal(s) could I use?  If some do
    not work, explain why not. Show how your approach works in Binary Tree A from the below section.
        post-order traversal

        left
        right
        sum

            1
           / \
          2   3
         /     \
        4       5
               / \
              6   7
                   \
                    8

        although postorder is best suited for this problem, you could inartfully use any traversal

        def subtree_sum(node) -> int:
            if node is None:
                return 0
            count += subtree_sum(node.left)
            count += subtree_sum(node.right)
            return count + node.val


    Tree Traversals Orderings

    Give the preorder, postorder, inorder, and level order traversals for each of the following trees. Assume that
    children are processed left to right.

    1. Binary Tree A

        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7
               \
                8

    pre-order: 1 2 4 3 5 6 7 8
    in-order: 4 2 1 3 6 5 7 8
    post-order: 4 2 6 8 7 5 3 1
    level-order: 1 2 3 4 5 6 7 8

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

    pre-order: 1 2 5 3 6 9 7 4 8 10 12 13 11 14
    in-order: UNDEFINED
    post-order: 5 2 9 6 7 3 12 13 10 14 11 8 4 1
    level-order: 1 2 3 4 5 6 7 8 9 10 11 12 13 14

Identifying Recursive Relationships

    Notice: These exercises are new and quite challenging.
    Please ask us on Slack immediately if you have questions about these problems.

    Please identify the base case and recurrence relationship for the following relationships in binary trees. For each
    question, please answer the following.

    Treat these more like math problems. Do not worry about having to implement your solutions in Python - we want to
    focus just on the approach.

    Do not use or assume global variables of any kind. If you need to pass information through recursion, please use a
    helper function with additional arguments to pass this information.

        1. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
        understanding of the question.

        2. Base Case - When does the recursion stop?

        3. Recurrence Relation - How can you solve for the parent using the solution for the children? You can describe
        this with an equation or in English - whichever is more effective at communicating your approach.

        4. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of these
        as test cases - we will be pretty critical if your proposed solution does not work on the provided examples.

        5. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree? Does
        the same solution work? If not, what additional changes need to be made?

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

    Note: The height of a binary tree is equal to the maximum number of edges from the root to the most distant leaf
    node. The height of an empty tree or tree with one node is 0. The height of an individual node is the number of
    edges from it to the root node.

    You may use previous solutions or introduce additional recursive functions to help you solve the problems.

    Here is an example of size(root) computing the size of a binary tree. Please complete the rest following this
    format.

        1. Example. size(root) finds the number of nodes in a binary tree. For case A, size(A) = 9 since there are 9
        nodes in the tree.

            a. size(B) = 5, size(C) = 11, size(D) = 7, size(E) = 9
            b. Base Case: if root is None: return 0 in other words size(None) = 0
            c. Recurrence Relation: size(root) = size(left) + size(right) + 1
            d. Yes: Verified. size(left/3) = 5, size(right/10) = 3, size(root) = 5+3+1 = 9 You should verify all 5 of
            them. Here left/3 just identifies the left child is the one with value of 3 and right/10 identifies the
            right node has the value 10
            e. A similar solution works but instead. size(root) = 1 + sum(root.child) for each child node.

        2. sum(root) finds the sum of all the nodes in the binary tree. sum(A) = 1+3+8+6+4+&+10+14+12= 65
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                sum(A) => 65
                sum(B) => 15
                sum(C) => 66
                sum(D) => 23
                sum(E) => 48

            b. Base Case - When does the recursion stop?
                if node is None:
                    return 0

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.
                sum(node) = node + sum(node.left) + sum(node.right)
                each recursive call sums the current node with children sums

            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.
                verified; the proposed relation is an application of the recursive definition of trees

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                sum(node) = node + builtins.sum([sum(child) for child in node.children])


        3. max_val(root) finds the maximum value among all nodes in a binary tree. max_val(A) = 14 since it is the
        largest element in the tree.
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                max_val(A) = 14
                max_val(B) = 5
                max_val(C) = 11
                max_val(D) = 5
                max_val(E) = 10

            b. Base Case - When does the recursion stop?
                if node is None:
                    return float('-inf')

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.
                max_val(node) = max(node.val, max_val(node.left), max_val(node.right))
                each recursive call finds the maximum value between the current node and its children

            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.
                verified

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                max_val(root) = max([node] + [max_val(child) for child in node.children])


        4. is_symmetric(root) returns True if the tree is symmetric and False if it is not. is_symmetric(A) = False and
        is_symmetric(D) = True. A tree is symmetric if the left and right subtrees are mirror images of each other.
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                is_symmetric(A) = False
                is_symmetric(B) = False
                is_symmetric(C) = False
                is_symmetric(D) = True
                is_symmetric(E) = False

            b. Base Case - When does the recursion stop?
                todo: review
                if node is None:
                    return ?

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.
                todo: incorrect
                is_symmetric(node) = all(node.left == node.right, is_symmetric(node.left), is_symmetric(node.right))

                uhh:
                is_symmetric(node) = level_order(node.left) == level_order(node.right)[::-1]
                is_symmetric(node) = level_order[:level//2] == level_order[:level//2 - 1:-1]

                is_symmetric(node) = level(nodes) == level(nodes)[::-1]

                is_symmetric(node) = is_symmetric(node.left)

                the tree is_semmetric() when each level is palindromic (has reflectional symmetry across the vertical
                axis when represented as a tree structure)



            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.
                todo

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                todo: incorrect
                is_symmetric(root) = all([node.left == node.right] + [is_symmetric(child) for child in node.children])


        5. height(root) finds the height of the tree. The distance from the root to the lowest child. height(A) = 3
        because 12 is 3 levels down from the 8.
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                height(A) = 3
                height(B) = 4
                height(C) = 3
                height(D) = 2
                height(E) = 4

            b. Base Case - When does the recursion stop?
                if node is None:
                    return 0

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.
                height(root) = max(height(node.left), height(node.right)) + 1
                each level returns the maximum depth below, plus itself (less the root)

            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.

                todo

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                height(node) = max([child for child in node.children]) + 1


        6. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path
        may or may not pass through the root of the tree. diameter(root) finds the diameter of this tree.
        diameter(A) = 6 because the path from 4 or 7 to 12  has length 6.
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                diameter(A) = 6
                diameter(B) = 4
                diameter(C) = 5
                diameter(D) = 4
                diameter(E) = 7

            b. Base Case - When does the recursion stop?
                if node is None:
                    return 0

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.

                diameter(node) = max(diameter(node.left), diameter(node.right)) + 1
                todo: vs
                diameter(node, longest) = max(diameter(node.left, longest), diameter(node.right, longest)) + 1

                each level updates the longest path (diameter) by comparing the previous best and current longest paths,
                and returns the longest left or right path plus one to the parent node.

            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.
                verified

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                diameter(node) = max([diameter(child) for child in node.children]) + 1

        7. leafs(root) calculates the number of leaves in a binary tree. leafs(A)=4 because 1,4,7,12 are all leaf nodes.
        Recall leaf nodes are nodes with no children.
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                leafs(A) = 4
                leafs(B) = 1
                leafs(C) = 6
                leafs(D) = 4
                leafs(E) = 3

            b. Base Case - When does the recursion stop?
                if node is None:
                    return 0

                if not node.left and not node.right:
                    return 1

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.
                leafs(node) = leafs(node.left) + leafs(node.right)

            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.
                verified
                todo

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                leafs(node) = sum([child for child in node.children])


        8. top_ordered(root) returns True if the root of every subtree is the smallest element in its subtree.
        top_ordered(E) = True because every Node, it is smaller than the elements in its subtree. top_ordered(A) = False
        because 3 is larger than its left child of 1.
            a. Verify Understanding - Compute the expected output for all the example trees. Do this manually to verify
            understanding of the question.
                top_ordered(A) = False
                top_ordered(B) = True
                top_ordered(C) = True
                top_ordered(D) = True
                top_ordered(E) = True

            b. Base Case - When does the recursion stop?
                if node is None:
                    return True

                left = node.left.val if node.left else node.val + 1
                right = node.right.val if node.right else node.val + 1
                return True if left > node.val and right > node.val else False

            c. Recurrence Relation - How can you solve for the parent using the solution for the children? You can
            describe this with an equation or in English - whichever is more effective at communicating your approach.
                top_ordered(node) = node.left.val > node.val and node.right.val > node.val
                                    and top_ordered(node.left) and top_ordered(node.right)

                top_ordered(node) = node.each_child.val > node.val and top_ordered(node.each_child)

                each recursive call compares the current node to its children, and checks that all children are valid

            d. Check Unit Tests. Double-check your proposed relation works for the examples trees provided. Think of
            these as test cases - we will be pretty critical if your proposed solution does not work on the provided
            examples.
                verified
                todo

            e. N-Ary Extension. How would this change if you were dealing with an n-ary tree instead of a binary tree?
            Does the same solution work? If not, what additional changes need to be made?
                top_ordered(node) = all([child.val > node.val and top_ordered(child) for child in node.children])

        9. find_height(root, height) determines the number of nodes that have height height. find_height(A, 2) = 3
        because of 1,6,14 are the nodes with height 2. find_height(any non empty tree, 0) = 1 because it will be just
        the root (assuming the tree is not empty)

        10. sum_only_child_parents(root) determines the sum of nodes with exactly one child.
        sum_only_child_parents(A) = 24because 10,14 are the nodes with one child, and their sum if 24.

        11. sum_only_child(root) determines the sum of all nodes that do not have a sibling sum_only_child(A) = 34
        because 8,14,12 are the nodes without siblings and their sum if 35. The root does not have a sibling node and is
        an "only child" node.

        12. level_min(root, height) determines the node of minimum value height equal to the given height.
        level_min(A, 0) = 8,level_min(A,1) = 3, level_min(A,2) = 1

        13. full(root) determines if a binary tree is full. A binary tree is said to be full if every node has 0 or 2
        children. full(D) = True, full(A) = False

        14. same(root_a, root_b) returns True if root_a and root_b represent the same binary tree and False otherwise.
        Your recurrence will require you to use both root_a, root_b as inputs. same(A, A) = True, same(A,B) = False

        15. Challenge Question. almost_same(root_a, root_b, k) returns True if root_a and root_b represent the same
        binary tree except the k of the values can be different. Suppose we're using example A. If k=1 then you can
        replace the value of the root in A to 20 instead of 8. We have a modified version of A call this Z, then you
        would have almost_same(A, Z, 1) = True but almost_same(A, Z, 0) = False . The latter is False because A differs
        from Z in the root value. If the tree structure is any different, i.e. you find None in one tree at the same
        position as a Node in the other tree, then return False. If k = 0 , then the output should be equivalent to same
        function in the previous problem. Namely, almost_same(root_a, root_b,0) == same(root_a, root_b) .

Tries

    General

    1. What is a trie?
        a prefix (n-ary) tree that contains a boolean (or equivalent) at each node indicating whether the preceding
        nodes are a valid prefix (e.g. a word in a dictionary)

    2. When do we use a trie?
        any time you want efficient runtime in a problem that can be reduced to, or would otherwise significantly
        benefit from, finding a prefix
        e.g.:
        implementation of the dictionary,
        pattern searching,
        longest prefix matching algorithm used for routing tables for IP addresses,
        storing/querying XML documents,
        data compression,
        computational biology,
        ...

    3. How do we know that “dog” is an actual word in our trie and is not just a prefix of the word “doghouse”?
        the 'g' node would contain a prefix indicator

    4. Suppose our dictionary has n words and the longest of them is m characters long. What is the time and space
    complexity of building our trie?




Building a Trie

    1. Start with an empty trie and insert the words "hello", "help", "held", "helden", "helderman", "helping" into this
    trie. Draw the resulting trie in tree structure.
                h
                e
                l
             d- l  p-
          e     o-    i
       r  n-          n
    m                 g-
    a
    n-

    2. Trace through how you would search for "helping" in this trie.
        h -> e -> (d- l p-) -> p- -> i -> n -> g-

    3. Trace how you would find all words starting with the prefix "he" in this Trie.
        visit all the prefix indicators ( - )
        h -> e -> l -> (d- l p-)
        h -> e -> l -> d-
        h -> e -> l -> d -> e -> (r n-)
        h -> e -> l -> d -> e -> r -> m -> a -> n-
        h -> e -> l -> d -> e -> n-
        h -> e -> l -> l -> o-
        h -> e -> l -> p-
        h -> e -> l -> p -> i -> n -> g-


'''
