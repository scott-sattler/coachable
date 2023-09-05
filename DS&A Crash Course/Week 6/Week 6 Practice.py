'''
Graphs

Free Response Questions

General

    Figure 1:
    6 - 2
     |   |
     5 - 1 - 4
         |
         3

    1. What are the differences between graphs and trees?

    2. For the graph (Figure 1), write the Adjacency Matrix and Adjacency List representations.

    3. What does it mean for a graph to be directed?

    4. What does it mean for a graph to have a cycle?

    5. How can you detect a cycle in a graph?

    6. If you have a graph with N vertices, what is the maximum number of edges it could have?

    7. Recall that a binary tree is an example of a graph. If a binary tree has N nodes, what is the maximum number of
    edges it can have?

Graph Traversals

    Assume the adjacency lists are in sorted order. For example, follow the edge O → B before O → E. Similarly, follow
    3 → 2 before 3 → 7.

    < FIGURE 2 >

    1. Give the postorder of the graph when visited by DFS. Start from O.

    2. Give the preorder of the graph when visited by DFS. Start from O.

    3. Give the BFS traversal of the graph. Start from O.

    4. Is there a topological order starting from O? If there is not, why not? If there is one, write the topological
    order.

    < FIGURE 3 >

    1. Give the postorder of the graph when visited by DFS. Start from node 10.

    2. Give the preorder of the graph when visited by DFS. Start from 1O.

    3. Give the level order of the graph. Start from 10.

    4. Is there a topological order starting from 10? If there is not, why not? If there is one, write the topological
    order.

Inorder for Graphs

    We have a preorder, inorder, and postorder for binary trees. However, an inorder traversal doesn't really make sense
    for graphs because it's unclear where you would process the node among multiple child nodes. For example, if you had
    a parent node X with children A,B,C, it's ambiguous which child you would process X after.

    For this reason, graph DFS is usually postorder or preorder.

    For this exercise, we'll use alphabetical ordering to create our in-order traversal - the parent and children will
    be processed in alphabetical order. In the above DFS call on X would look like

    dfs(X)
        dfs(A)
        dfs(B)
        dfs(C)
        process(x)

    If B were the parent and A,C,X were the children, then the call would look like this.

    dfs(B)
        dfs(A)
        process(B)
        dfs(C)
        dfs(X)

    Determine the alphabetical in-order traversal for

        The graph in figure 2 starting from O.

        The graph in figure 3 starting from 10

Shortest Path

    1. Supposes we have a graph G with vertices s,t. How can you find the length of the shortest path from s→t in each
    of the following scenarios?

        a. Every edge in G has weight 1.

        b. Every edge in G has uniform edge weight e where e > 0?

        c. Edges in G have nonuniform but strictly positive edge weights?

        d. Edges in G have nonuniform negative/positive edge weights?

    2. How do any of these change if we want to return the path itself instead of the shortest path length?

Valid Orderings

    1. If I have a directed acyclic graph (DAG) where c1 -> c2 means that I need to take course c1 before c2

        a. What algorithm can I use to sequence my coursework without skipping courses?

        b. How is this algorithm different from a standard BFS/DFS?

        c. What would happen if the directed graph was cyclic, and I tried using the same algorithm?

Intermediate Processing BFS/DFS

    Assume you have a digraph G with vertices represented with lowercase letters e.g. s,v,w. A counter-example here is a
    specific graph where the statement is false.

    Hint: Once you have established any of the statements as true or false, you may use them to prove further ones.
    I.e. if you think (2) is true, you can use it to help you prove (1).

    DFS. For each of the following statements, indicate whether it is true or false in the context of a depth-first
    search on a digraph starting from vertex s starting with dfs(G,s) If it is false, provide a counterexample. If it is
    true, explain why.

    1. At the moment when dfs(G, v) is called, there must be a directed path from s to v in G.

    2. At the moment when dfs(G, v) is called, there must be a directed path from s to v in the function-call stack.

    3. At the moment when dfs(G, v) is called, if G includes an edge v → w for which w has been previously marked, then
    G must contain a directed cycle containing v.

    4. At the moment when dfs(G, v) is called, if G includes an edge v → w for which w is currently a vertex on the
    function-call stack, then G must contain a directed cycle containing v.

    BFS. For each of the following statements, indicate whether it is true or false in the context of a breadth-first
    search on a digraph starting from vertex s.  If it is false, provide a counterexample. If it is true, explain why.

    1. At the moment when v is removed from the queue during BFS, there must be a directed path from s to v in G.

    2. At the moment when v is removed from the queue during BFS, there must be a directed path from s to v in the
    queue.

    3. At the moment when v is removed from the queue during BFS, if G includes an edge v → w for which w has been
    previously marked, then G must contain a directed cycle containing v.

    4. At the moment when v is removed from the queue during BFS, if G includes an edge v → w for which w is currently
    a vertex in the queue, then G must contain a directed cycle containing v.

(Optional Section) MSTs

    1. What is a minimum spanning tree?

    2. How do I generate an MST for a graph with edge weights? Explain the algorithm in a few sentences instead of
    giving just the algorithm name.

    3. If the graph is not connected, can I still create an MST? Why or why not? What about a Minimum Spanning Forest

Heaps

Free Response Questions

    1. What underlying data structure(s) can a heap use?

    2. What is the difference between a min and a max heap?

    3. What is the runtime of pushing an element into a heap?

    4. What is the runtime of popping an element out of a heap?

    5. We can store integers in a heap. What about an arbitrary object? Which ones can we keep, and which ones can’t we?

    6. If we wanted to store some of those objects we can’t keep, what concept do we need to add to those objects?

    7. If I wanted to find the K smallest elements in a stream, would I use a min or a max heap of size K? Why?

    8. What if I wanted to find the K most significant elements in a stream? Why?

    9. If I have a collection of N elements, and I insert each of them into a min heap, and then pop + print each element
    from the heap. What did I just do?

    10. What if I inserted each of them into a max heap and did the same thing?

    11. Suppose I insert the following sequence of numbers into a min heap: 5, 7, 9, 2, 4.

        a. What does the min heap look like?

        b. Now suppose I pop twice. What does the heap look like now?

        c. Now suppose I insert 3, 9, 12. What does the heap look like now?

True or False

Determine if the statements are true or false. If false, provide a counter-example. If true, explain why.

    1. Let a[] be a max-oriented binary heap that contains the N distinct integers 1, 2, . . . , N in a[1] through a[N].
    Then, key N must be in a[1]; key N − 1 must be in either a[2] or a[3]; and key N − 2 must be in either a[2] or a[3].

    2. The order of growth of the total number of compares to insert N distinct keys in descending order into an
    initially empty max-oriented binary heap is N.

    3. A 3-heap is an array representation (using 1-based indexing) of a complete 3-way tree, where the key in each node
    is greater than (or equal to) its children’s keys. In the worst case, the number of compares to insert a key in a
    3-heap containing N keys is ∼ 1 log3 N.

Number of Comparisons

    < FIGURE A >

    1. If we insert a new element y into the heap. How many positions could it end up in?

    2. See the binary heap in Figure A. Supposed the last operation was insert(x). How many values could it possibly
    have been? Hint: Try to identify which values specifically would be possible.

    3. Suppose you delete the maximum key from the binary heap in figure A. How many keys are involved in one or more
    comparisons?

'''