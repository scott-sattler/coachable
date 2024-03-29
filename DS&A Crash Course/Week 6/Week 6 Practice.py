"""
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
        trees are an acyclic subset of graphs that have exactly one edge between any two vertices

    2. For the graph (Figure 1), write the Adjacency Matrix and Adjacency List representations.
        adjacency matrix:
           1  2  3  4  5  6
        1  1  1  1  1  1  0
        2  1  0  0  0  0  1
        3  1  0  0  0  0  0
        4  1  0  0  0  0  0
        5  1  0  0  0  0  1
        6  0  1  0  0  1  0

        adjacency list:
        [
            [2, 3, 4, 5],
            [1, 6],
            [1],
            [1],
            [1, 6],
            [2, 5]
        ]
        {
            1: [2, 3, 4, 5],
            2: [1, 6],
            3: [1],
            4: [1],
            5: [1, 6],
            6: [2, 5]
        }
        LLNode[1] -> LLNode[2] -> LLNode[3] -> LLNode[4] -> LLNode[5]
        LLNode[2] -> LLNode[1] -> LLNode[6]
        LLNode[3] -> LLNode[1]
        LLNode[4] -> LLNode[1]
        LLNode[5] -> LLNode[1] -> LLNode[6]
        LLNode[6] -> LLNode[2] -> LLNode[5]


    3. What does it mean for a graph to be directed?
        for vertex connections (edges) to be unidirectional
        predecessors (tail nodes) can access their successors (head nodes)
        a --> b : a implies b; b does not imply a
        a <-- b : b implies a; a does not imply b
        a <-> b : a implies b, b implies a

    4. What does it mean for a graph to have a cycle?
        for a path (trail) to lead back to the originating vertex

    5. How can you detect a cycle in a graph?
        1. keep track of visited nodes
        2. Floyd's cycle detection algorithm (two pointers)
        3. todo other

    6. If you have a graph with N vertices, what is the maximum number of edges it could have?
        n(n-1) directed graph without self loops
        n(n-1)/2 undirected graph (each path is bidirectional)
        n^2 directed graph with self loops

    7. Recall that a binary tree is an example of a graph. If a binary tree has N nodes, what is the maximum number of
    edges it can have?
        the first node has 0 connections, with every additional node will having a maximum of 1 connection
        -> (N - 1)

Graph Traversals

    Assume the adjacency lists are in sorted order. For example, follow the edge O → B before O → E. Similarly, follow
    3 → 2 before 3 → 7.

    < FIGURE 2 >

    1. Give the postorder of the graph when visited by DFS. Start from O.
        M W Y I P S E B O

    2. Give the preorder of the graph when visited by DFS. Start from O.
        O B E S I W M Y P

    3. Give the BFS traversal of the graph. Start from O.
        O B E Y S W I M P

    4. Is there a topological order starting from O? If there is not, why not? If there is one, write the topological
    order.
        no. topological order requires a directed acyclic graph because the sort orders the vertices of directed edges
        such that parents precede children; cycles have no parent (cycles contain neither predecessor nor successor).

    < FIGURE 3 >

    1. Give the postorder of the graph when visited by DFS. Start from node 10.
        1 6 8 7 2 5 4 3 9 10

    2. Give the preorder of the graph when visited by DFS. Start from 1O.
        10 9 3 2 1 7 6 8 4 5

    3. Give the level order of the graph. Start from 10.
        10 9 3 5 8 2 4 7 1 6

    4. Is there a topological order starting from 10? If there is not, why not? If there is one, write the topological
    order.
        no. 4 -> 9 -> 3 -> 4
        but, if we removed edge 3 -> 4:
        10 4 9 5 3 2 7 8 6 1

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
            B E I M P S W O Y

            dfs(O)
                dfs(B)
                dfs(E)
                process(O)
                dfs(Y)

            dfs(B)
                process(B)

            dfs(E)
                process(E)
                dfs(S)
                dfs(W)

            dfs(S)
                dfs(I)
                dfs(M)
                dfs(P)
                process(S)

            dfs(I)
                process(I)

            dfs(M)
                process(M)

            dfs(P)
                process(P)

            dfs(W)
                process(W)

            dfs(Y)
                process(Y)

        The graph in figure 3 starting from 10
            1 2 3 4 6 7 5 8 9 10

            dfs(10)
                dfs(9)
                process(10)

            dfs(9)
                dfs(3)
                dfs(5)
                dfs(8)
                process(9)

            dfs(3)
                dfs(2)
                process(3)
                dfs(4)
                dfs(7)

            dfs(2)
                dfs(1)
                process(2)

            dfs(1)
                process(1)

            dfs(4)
                process(4)

            dfs(7)
                dfs(6)
                process(7)

            dfs(6)
                process(6)

            dfs(5)
                process(5)

            dfs(8)
                process(8)

Shortest Path

    1. Supposes we have a graph G with vertices s,t. How can you find the length of the shortest path from s→t in each
    of the following scenarios?

        a. Every edge in G has weight 1.
            1. dijkstra's
            2. shortest path faster algorithm (SPFA)
            3. bellman-ford
            4. dfs, return length at first encounter of t
            5. dfs, exhaustive

        b. Every edge in G has uniform edge weight e where e > 0?
            1. dijkstra's
            2. shortest path faster algorithm (SPFA)
            3. bellman-ford
            4. bfs, return length at first encounter of t
            5. dfs, exhaustive

        c. Edges in G have nonuniform but strictly positive edge weights?
            1. dijkstra's
            2. shortest path faster algorithm (SPFA)
            3. bellman-ford
            4. bfs, exhaustive
            5. dfs, exhaustive

        d. Edges in G have nonuniform negative/positive edge weights?
            1. bellman-ford
            2. SPFA
            3. bfs, exhaustive
            4. dfs, exhaustive

    2. How do any of these change if we want to return the path itself instead of the shortest path length?
        dijkstra's distance map can also contain the previous node
        bellman-ford's distance map can also contain the previous node
        SPFA's distance map can also contain the previous node
        bfs/dfs can store paths, rather than distances


Valid Orderings

    1. If I have a directed acyclic graph (DAG) where c1 -> c2 means that I need to take course c1 before c2

        a. What algorithm can I use to sequence my coursework without skipping courses?
            topological sort

        b. How is this algorithm different from a standard BFS/DFS?
            todo:
            topological sort is an ordering where for every directed edge (u, v), u is ordered before v in the ordering
            neither BFS nor DFS specifically intend to maintain this property, and given certain graphs, will
            predictably violate it (tho BFS often provides similar orderings when visiting nodes)

        c. What would happen if the directed graph was cyclic, and I tried using the same algorithm?
            the algorithm would fail: a cycle has neither a predecessor, nor successor, therefore, cannot be
            topologically ordered

Intermediate Processing BFS/DFS

    Assume you have a digraph G with vertices represented with lowercase letters e.g. s,v,w. A counter-example here is a
    specific graph where the statement is false.

    Hint: Once you have established any of the statements as true or false, you may use them to prove further ones.
    I.e. if you think (2) is true, you can use it to help you prove (1).

    DFS. For each of the following statements, indicate whether it is true or false in the context of a depth-first
    search on a digraph starting from vertex s starting with dfs(G,s). If it is false, provide a counterexample. If it
    is true, explain why.

    1. At the moment when dfs(G, v) is called, there must be a directed path from s to v in G.
        true; dfs being called on v indicates v is a (direct or indirect) successor to s

    2. At the moment when dfs(G, v) is called, there must be a directed path from s to v in the function-call stack.
        true; dfs ordinarily does not operate on disjointed graphs, and in such cases, there must exist a directed path
        from s to v, given lemma (1)

    3. At the moment when dfs(G, v) is called, if G includes an edge v → w for which w has been previously marked, then
    G must contain a directed cycle containing v.
        false; this could be true if G were an undirected graph, or if w otherwise had a path to a direct or indirect
        successor of s, which also had a directed path to any vertex on the path from s to v.
        examples: [(s, v), (v, w) (w, s)], [(s, v), (s, t), (v, w), (w, t), (t, v)]

    4. At the moment when dfs(G, v) is called, if G includes an edge v → w for which w is currently a vertex on the
    function-call stack, then G must contain a directed cycle containing v.
        true; in dfs, vertices on the function-call stack indicate those vertices are part of a path from s to v.
        therefore, any edge which leads to a vertex on the function-call stack has formed a cycle

    BFS. For each of the following statements, indicate whether it is true or false in the context of a breadth-first
    search on a digraph starting from vertex s. If it is false, provide a counterexample. If it is true, explain why.

    1. At the moment when v is removed from the queue during BFS, there must be a directed path from s to v in G.
        true; the queue is populated with successors to all previously visited vertices, and just as each successor was
        visited from the queue, a path can be found through those successors from s to v

    2. At the moment when v is removed from the queue during BFS, there must be a directed path from s to v in the
    queue.
        false; the queue is populated with successors to all previously visited vertices, and does not necessarily
        contain a path from s to v. example: given the graph [(s, v), (s, w), (v, w)], our queue would look like
        [(s, v), (s, w)], we then .popleft() and obtain [(s, w)]. further, exploring v would get us no closer to
        establishing the truth of that statement: [(s, w), (v, w)]

    3. At the moment when v is removed from the queue during BFS, if G includes an edge v → w for which w has been
    previously marked, then G must contain a directed cycle containing v.
        false; w could also have been an acyclic successor of a previously visited node

    4. At the moment when v is removed from the queue during BFS, if G includes an edge v → w for which w is currently
    a vertex in the queue, then G must contain a directed cycle containing v.
        false; given the graph [(s, v), (s, w), (v, w)], with v visited first, the queue for v would be [(s, w)]


(Optional Section) MSTs

    1. What is a minimum spanning tree?
        weighted edges that connect all vertices at minimum cost, without loops

    2. How do I generate an MST for a graph with edge weights? Explain the algorithm in a few sentences instead of
    giving just the algorithm name.
        1. pick any vertex
        2. find lowest edge weight
            ignore visited vertices
        3. move to that vertex
        4. repeat 2 and 3 until  all vertices are visited

    3. If the graph is not connected, can I still create an MST? Why or why not? What about a Minimum Spanning Forest
        no. a tree requires all vertices be connected. however, a collection of MSTs, or disconnected MSTs are called
        Minimum Spanning Forests (MSFs). of the algorithms mentioned within this section, we can find MSFs with
        Kruskal's algorithm, or Prim's algorithm on each disconnected graph.


Heaps

Free Response Questions

    1. What underlying data structure(s) can a heap use?
        list (array) or binary tree

    2. What is the difference between a min and a max heap?
        min heap: every parent is less than either child
        max heap: every parent is greater than either child

    3. What is the runtime of pushing an element into a heap?
        O(log n), where n is the size of the heap

    4. What is the runtime of popping an element out of a heap?
        O(log n), where n is the size of the heap

    5. We can store integers in a heap. What about an arbitrary object? Which ones can we keep, and which ones can’t we?
        any object that is orderable  (i.e. has some value that can be compared, such as 97 < 98, a < b) can be used in
        a heap. objects without this property cannot - unless they're assigned such a value

    6. If we wanted to store some of those objects we can’t keep, what concept do we need to add to those objects?
        the object needs to be assigned a value that will be used for comparison

    7. If I wanted to find the K smallest elements in a stream, would I use a min or a max heap of size K? Why?
        max heap; you would add elements from the stream, popping the max value whenever the heap exceeded size K

    8. What if I wanted to find the K most significant (frequently occurring) elements in a stream? Why?
        create a key-value pair for each new element: key is the element ID that will be observed in the stream, and
        value is the frequency (or a two element list also containing the current index if not using a binary tree).

        for each time a key-value pair is created or updated:
            (1) if the element is newly created, append it to the min-heap and
                (1a) if capacity is not yet filled, sift_up for O(log K), or
                (1b) when over max capacity,
                    (1b.i) if the new element is less than the root, do not add it to the heap,
                    (1b.ii) if it is greater than the root, replace the root and sift_down for O(log K);
            (2) if the element is updated, and NOT within the heap, treat it as if it were a new element;
            (3) if the element is updated within in the heap, sift_down that element for O(log K).

        O(n * log K) time complexity, where n is the number of stream elements, and K is the size of the heap
        O(n + K) space complexity, where n is the total stream count, and K is size of the heap

    9. If I have a collection of N elements, and I insert each of them into a min heap, and then pop + print each
    element from the heap. What did I just do?
        sort ascending

    10. What if I inserted each of them into a max heap and did the same thing?
        sort descending

    11. Suppose I insert the following sequence of numbers into a min heap: 5, 7, 9, 2, 4.

        a. What does the min heap look like?
            2 4 9 7 5

        b. Now suppose I pop twice. What does the heap look like now?
            4 5 9 7
            5 7 9

        c. Now suppose I insert 3, 9, 12. What does the heap look like now?
            3 5 9 7 9 12

True or False

    Determine if the statements are true or false. If false, provide a counter-example. If true, explain why.

    1. Let a[] be a max-oriented binary heap that contains the N distinct integers 1, 2, . . . , N in a[1] through a[N].
    Then, key N must be in a[1]; key N − 1 must be in either a[2] or a[3]; and key N − 2 must be in either a[2] or a[3].
        true. max heaps have the property of each node being greater than all children/descendant nodes.

        Given that N > N - 1 > N - 2,

               N
             /   \
           /      \
        N - 1    N - 2

               N
             /   \
           /      \
        N - 2    N - 1

        both satisfy the max-heap property

    2. The order of growth of the total number of compares to insert N distinct keys in descending order into an
    initially empty max-oriented binary heap is N.
        false. insertion time complexity is O(log k), where k is the heap size. what we mean by this is that for each
        insertion, we're going to be doing up to 2*log_2(k) compares - not N. so, the order of growth of the number of
        compares for this problem is N*log(k). we can, however, heapify an already existing array in O(N) time by
        starting at the rightmost (in an array/list) parent, iterating to the topmost node, and sifting the ith node
        down on each iteration...

        disregarding the bottommost level (they have no children, hence, satisfy the heap property), we have O(1)
        operations on the level above. this results in ~(n/4) nodes remaining...
        we have n/4 nodes at level 1, n/8 nodes at level 2, n/16 nodes at level 3... and 1 node at log(n) level...
        which can be rewritten as: n/4(1c) + n/8(2c) + n/16(3c) + ... 1(log(n)c)...
        and if n/4 = 2^k, the above becomes: c2^k(1/2^0 + 2/2^1 + 3/2^2 + ... (k + 1)/2^k)...
        notice that (1/2^0 + 2/2^1 + 3/2^2 + ... (k + 1)/2^k) converges to less than 3...
        so we can rewrite the statement as, c2^kc -> c2^k -> c(n)/4 -> c(n) -> O(n)

    3. A 3-heap is an array representation (using 1-based indexing) of a complete 3-way tree, where the key in each node
    is greater than (or equal to) its children’s keys. In the worst case, the number of compares to insert a key in a
    3-heap containing N keys is ∼ 1 log3 N.
        true. insertions append the key, then sift-up. in binary trees, sift-up operations compare the child to the
        parent at most, log_2(N) times, where N is the height of the tree. when we say log_2(N) times, what we're saying
        is how many times some number has doubled (or been multiplied by our base 2) - because we're using binary trees.
        however, if we were to use ternary, or 3-way trees, each level triples (not doubles), hence ~ log_3(N).


Number of Comparisons

    < FIGURE A >

    1. If we insert a new element y into the heap. How many positions could it end up in?
        5; root, root.right, root.right.right, root.right.right.right, root.right.right.right.left

    2. See the binary heap in Figure A. Supposed the last operation was insert(x). How many values could it possibly
    have been? Hint: Try to identify which values specifically would be possible.
        5; 19, 26, 32, 35, 38

    3. Suppose you delete the maximum key from the binary heap in figure A. How many keys are involved in one or more
    comparisons?
        7: 37 35, 19 37; 34 36, 19 36; 14 17, 19 17
        19 37 35 34 36 14 17

"""
