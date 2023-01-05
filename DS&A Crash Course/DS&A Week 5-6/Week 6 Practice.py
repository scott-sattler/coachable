""" Week 6 Practice """

"""
### Graphs ###

Free Response Questions

General
    Figure 1:
        6 - 2
        |   |
        5 - 1 - 4
            |
            3

    What are the differences between graphs and trees?
        trees are a subset of graphs
        trees are exclusively digraphs
        trees always have 1 parent and >0 neighbor
            bst: r > p > l
        trees can provide structural time complexity advantages
          bisects data: many operations in log(n)

    For the graph (Figure 1), write the Adjacency Matrix and Adjacency List representations.
            1   2   3   4   5   6
        1   0   1   1   1   1   0
        2   1   0   0   0   0   1
        3   1   0   0   0   0   0
        4   1   0   0   0   0   0
        5   1   0   0   0   0   1
        6   0   1   0   0   1   0

        [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 6], \
        [3, 1], [4, 1], [5, 1], [5, 6], [6, 2], [6, 5]]

        {1: [2, 3, 4, 5], 2: [1, 6], 3: [1], 4: [1], 5: [1, 6], 6: [2, 5]}

        LLNode[1] -> LLNode[2] -> LLNode[3] -> LLNode[4] -> LLNode[5]
        LLNode[2] -> LLNode[1] -> LLNode[6]
        LLNode[3] -> LLNode[1]
        LLNode[4] -> LLNode[1]
        LLNode[5] -> LLNode[1] -> LLNode[6]
        LLNode[6] -> LLNode[2] -> LLNode[5]

    What does it mean for a graph to be directed?
        for > 0 vertex connections (edges) to be unidirectional

    What does it mean for a graph to have a cycle?
        for > 0 vertices have > 0 paths (edge + vertices) to themselves

    How can you detect a cycle in a graph?
        DFS while inspecting for previously visited vertices
        
    If you have a graph with N vertices, what is the maximum number of edges it could have?
        n(n-1) directed graph; n(n-1)/2 undirected graph; n^2 directed graph with self loops

    Recall that a binary tree is an example of a graph. If a binary tree has N nodes, what is the maximum number of 
    edges it can have?
        n - 1: n-n-n... always n - 1

        height (full/complete): ~ 2^n or 2^(n-1)

Graph Traversals

Assume the adjacency lists are in sorted order. For example, follow the edge O → B before O → E. Similarly, follow 3 → 2 
before 3 → 7

    Figure 2

        Give the postorder of the graph when visited by DFS. Start from O.
            M W Y I M P E B O
        
        Give the preorder of the graph when visited by DFS. Start from O.
            O B E S I W M Y P
            
        Give the BFS traversal of the graph. Start from O.
            O B E Y S W I M P
        
        Is there a topological order starting from O? If there is not, why not? If there is one, write the topological 
        order.
            no: loops - topological order can only be applied to DAGs
            topological sort orders the vertices of directed edges from a parent vertex to neighbor
                parents are undefined in cycles

  why BFS vs DFS:

        c          
        d   e g  t   d
      a        
        b  f  x  n  z  y  l


    Figure 3

        Give the postorder of the graph when visited by DFS. Start from node 10.
            !FIX: 5 4 8 6 7 1 2 3 9 10
            1 6 8 7 2 5 4 3 9 10
            
        Give the preorder of the graph when visited by DFS. Start from 1O.
            10 9 3 2 1 7 6 8 4 5
        
        Give the level order of the graph. Start from 10.
            review: 10 9 3 5 8->?4 2 7 1 6 8
        
        Is there a topological order starting from 10? If there is not, why not? If there is one, write the topological 
        order.
            no: loops - topological order can only be applied to DAGs
            topological sort orders the vertices of directed edges from a parent vertex to neighbor
                parents are undefined in cycles

Shortest Path

    Supposes we have a graph G where every edge has weight 1.
        How can I find the length of the shortest path from s to t?
            BFS, count nodes in path

        What if a graph has uniform edge weights e where e > 0?
            BFS, count nodes in path
        
        What if a graph has nonuniform but strictly positive edge weights?
            A* w/o heuristic; Dijkstra's Algorithm
        
        What if a graph has nonuniform negative/positive edge weights?
            eg Bellman–Ford Algorithm

        What if, instead of the length of the shortest path, I wanted to return the path itself?
            keep list of paths in agenda

Valid Orderings

    If I have a directed acyclic graph (DAG) where c1 -> c2 means that I need to take course c1 before c2.
    
    What algorithm can I use to sequence my coursework without skipping courses?
        topological sort
    
    How is this algorithm different from a standard BFS/DFS?
        it requires a DAG
    
    What would happen if the directed graph was cyclic and I tried using the same algorithm?
        it would fail: topological sort orders adjacent vertices by outgoing and incoming - a cycle is ambiguous

Intermediate Processing BFS/DFS

    For each statement, determine if it is true or false in both scenarios. Provide a counterexample if it is false or 
    explain your solution if it is true.
    
    Scenario 1 DFS. Consider the execution of depth-first search on a digraph G from vertex s, beginning with the 
    function call dfs(G, s). Suppose that dfs(G, v) is called during the depth-first search. Which of the following 
    statements can you infer at the moment when dfs(G, v) is called?
    
    Scenario 2 BFS. Consider the execution of breadth-first search on a digraph G, starting from vertex s. Suppose that 
    vertex v is removed from the queue during the breadth-first search. Which of the following statements can you infer 
    at the moment when v is removed from the queue?

    Statements
    
    G contains a directed path from s → v
    T T
    
    The function-call stack contains a directed path from s → v
        
    
    If G includes an edge v → w for which w has been previously marked, then G has a directed cycle containing v
        
    
    If G includes an edge v → w for which w is currently a vertex on the function-call stack, then G has a directed 
    cycle containing v
        

(Optional Section) MSTs

    What is a minimum spanning tree?
        acyclic minimum edge weight connecting all vertices
    
    How do I generate an MST for a graph with edge weights? Explain the algorithm in a few sentences instead of giving 
    just the algorithm name.
        Kruskal's Algorithm: sort by edge weight ascending, add smallest edges which do not form cycles
    
    If the graph is not connected, can I still create an MST? Why or why not? What about a Minimum Spanning Forest
        with Kruskal's Algorithm, yes; but not with Prim’s algorithm.


### Heaps ###

from queue import PriorityQueue
from queue import Queue

pq = PriorityQueue()
pq.put(-5)
pq.put(-7)

Free Response Questions

    What underlying data structure(s) can a heap use?
        tree; list
    
    What is the difference between a min and a max heap?
        node less/greater than or equal to children; recursively true
        
    What is the runtime of pushing an element into a heap?
        O(log N)
    
    What is the runtime of popping an element out of a heap?
        O(log N)
    
    We can store integers in a heap. What about an arbitrary object? Which ones can we keep, and which ones can’t we?
        see below.
    
    If we wanted to store some of those objects we can’t keep, what concept do we need to add to those objects?
        an orderable property; eg [red, blue, green] cannot be ordered without an orderable property - assigning these 
        words their respective wavelength [(red, 700), ... ]can then be ordered by ascending/descending wavelength
    
    If I wanted to find the K most minor elements in a stream, would I use a min or a max heap of size K? Why?
        min heap of K size contains K most minor elements
    
    What if I wanted to find the K most significant elements in a stream? Why?
        max heap of K size contains K largest elements
    
    If I have a collection of N elements, and I insert each of them into a min heap, and then pop + print each element 
    from the heap. What did I just do?
        sort by ascending
    
    What if I inserted each of them into a max heap and did the same thing?
        sort by descending
    
    Suppose I insert the following sequence of numbers into a min heap: 5, 7, 9, 2, 4. 
    
        What does the min heap look like?
            2 4 9 7 5
        
        Now suppose I pop twice. What does the heap look like now?
            5 7 9
        
        Now suppose I insert 3, 9, 12. What does the heap look like now?
            3 5 9 7 9 12
        

True or False

    Determine if the statements are true or false. If false, provide a counter-example. If true, explain why.
    
        Let a[] be a max-oriented binary heap that contains the N distinct integers 1, 2, . . . , N in a[1] through 
        a[N]. Then, key N must be in a[1]; key N − 1 must be in either a[2] or a[3]; and key N − 2 must be in either 
        a[2] or a[3]. 
        
        The order of growth of the total number of compares to insert N distinct keys in descending order into an 
        initially empty max-oriented binary heap is N.
            order of growth of total number of compares 
            is proportional to maximum height, where (n - 1) elements have a maximum height of log_2(n)
        
        A 3-heap is an array representation (using 1-based indexing) of a complete 3-way tree, where the key in each 
        node is greater than (or equal to) its children’s keys. In the worst case, the number of compares to insert a 
        key in a 3-heap containing N keys is ∼ 1 log3 N.
        
Number of Comparisons
        
    See the binary heap in Figure A. Supposed the last operation was insert(x). How many values could it possibly have 
    been? Hint: Try to identify which values specifically would be possible.
        22 ... unclear
        
    Suppose you delete the maximum key from the binary heap in figure A. How many keys are involved in one (or more) 
    comparisons?
        8: 37 35 34 36 30 28 29 19
        


"""

# ====================== CODING QUESTIONS ==========================

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 
(visually, n1 -> n2),
Create an adjacency list for it. def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
Create an adjacency matrix for it def to_adjacency_matrix(edges: list[list[str]]) -> list[list[str]:
'''


def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:  # noqa: shadowed name
    adjacency_list: dict[str, list[str]] = dict()
    for node_pair in edges:
        if node_pair[0] in adjacency_list:
            adjacency_list[node_pair[0]] += [node_pair[1]]
        else:
            adjacency_list[node_pair[0]] = [node_pair[1]]
        if node_pair[1] not in adjacency_list:
            adjacency_list[node_pair[1]] = []
    return adjacency_list


def to_adjacency_matrix(edges: list[list[str]]) -> list[list[str]]:  # noqa: shadowed name
    adjacency_list = to_adjacency_list(edges)
    matrix: list[list[str]] = list(list())
    # iterating over the edge pairs
    for row in adjacency_list.items():
        matrix_row = []  # create a new row for each key/vertex
        # if the values of this item (connected vertices) are present, append 1, else 0
        for column in adjacency_list.keys():
            if column in row[1]:
                matrix_row.append(1)
            else:
                matrix_row.append(0)
        matrix.append(matrix_row)
    return matrix


'''
Suppose you’re given a list of graph edges where each edge is of the form ["e1", "e2"], meaning that "e1" is connected to "e2". You’re also given a source node s and destination node d.
Write an algorithm to return the distance of one of the shortest paths, where each connection costs 1 to traverse. Return -1 if there is no path. def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
Modify the above algorithm to return the path itself. def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
Modify the above algorithm to work if each connection costs k where k > 0. def find_shortest_path(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
'''

from collections import deque  # noqa


def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
    # homogeneous weights & bidirectional -> BFS first solution is optimal

    # construct adjacency list; O(n), where n is number of edges
    associative_dict: dict[str, list[str]] = dict()
    for edge in edges:
        if edge[0] in associative_dict:
            associative_dict[edge[0]] += [edge[1]]
        else:
            associative_dict[edge[0]] = [edge[1]]
        if edge[1] not in associative_dict:
            associative_dict[edge[1]] = []

    # BFS traversal; O(V+E), where V total vertices and E total edges
    agenda = deque([[s], ])
    while agenda:
        current_path = agenda.popleft()
        # iterate over edges
        for node in associative_dict[current_path[-1]]:
            if node not in current_path:  # avoid cycles
                extended_path = current_path[:]
                extended_path.append(node)
                agenda.append(extended_path)
            if node == d:
                return len(agenda[-1]) - 1
    return -1


# Modify the above algorithm to return the path itself.
def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
    # homogeneous weights & bidirectional -> BFS first solution is optimal

    # construct adjacency list
    adjacency_dict: dict[str, list[str]] = dict()
    for edge in edges:
        if edge[0] in adjacency_dict:
            adjacency_dict[edge[0]] += [edge[1]]
        else:
            adjacency_dict[edge[0]] = [edge[1]]
        if edge[1] not in adjacency_dict:
            adjacency_dict[edge[1]] = []

    # traverse graph BFS
    agenda: deque = deque([[s], ])
    while agenda:
        print(agenda)
        current_path = agenda.popleft()
        for node in adjacency_dict[current_path[-1]]:
            if node not in current_path:
                extended_path = current_path[:]
                extended_path.append(node)
                agenda.append(extended_path)
            if node == d:
                return agenda[-1]

    return []


# Modify the above algorithm to work if each connection costs k where k > 0.
def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
    # A* without heuristic; Dijkstra's Algorithm
    # D EYE KA STRAs

    # best first?

    # construct adjacency list
    adjacency_dict: dict[str, list[str]] = dict()
    for edge in edges:
        if edge[0] in adjacency_dict:
            adjacency_dict[edge[0]] += [edge[1]]
        else:
            adjacency_dict[edge[0]] = [edge[1]]
        if edge[1] not in adjacency_dict:
            adjacency_dict[edge[1]] = []

    # traverse graph Dijkstra's
    node_dict: dict[str, list[int, str]] = dict(s=[0, ''])

    agenda: list[list[str, int, str]] = [[s, 0, ''], ]  # stack for DFS
    visited: set = {s}
    while agenda:
        current_node = agenda.pop(0)
        prev = current_node[0]
        dist = current_node[1]
        for node in adjacency_dict[current_node[0]]:
            if node not in visited:
                updated_node = [node, dist + k, prev]
                agenda.append(updated_node)
                visited.add(node)
            if node == d:
                return "traverse back"
        else:
            updated_node = current_node
        agenda.append(updated_node)
        agenda.sort(key=lambda x: x[1])

    return []


'''
Given a list of course prerequisites each in the form [0, 1] where 0 is a prerequisite of 1 and n, the total number of 
courses, write a function to output a valid course ordering, or None if not possible. Courses are numbered from 0 to 
n-1.
'''


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
    pass


'''
Optional Question. Comment in the testcase in the test engine code if you want to test this. 
Suppose you’re given a list of graph edges where each edge is of the form ("e1", "e2", 3), meaning that "e1" is 
connected to "e2" and has an edge weight of 3. The graph is connected. Write an algorithm to print out the an MST of the 
graph.
'''


def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    pass


# ===== BEGIN DO NOT MODIFY =====

class TestCase:
    def __init__(self, id, method, inputs, output):
        self.id = id
        self.method = method
        self.inputs = inputs
        self.output = output

    def execute(self):
        actual = self.method(*self.inputs)
        if actual == self.output:
            print("Test case " + str(self.id) + " passed")
        else:
            print("Test case " + str(self.id) + " failed, Expected Output: " + str(
                self.output) + ", Actual Output: " + str(actual))


adj_list = {}
adj_list["v1"] = ["v2", "v3"]
adj_list["v2"] = ["v4", "v5"]
adj_list["v3"] = []
adj_list["v4"] = ["v3"]
adj_list["v5"] = ["v6"]
adj_list["v6"] = ["v4"]

adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0]
]

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
courses = [[0, 1], [1, 2], [0, 2], [1, 3], [2, 3]]
courses_none = [[0, 1], [1, 2], [2, 0]]

graph = []
graph.append(("e1", "e2", 6))
graph.append(("e2", "e3", 2))
graph.append(("e1", "e3", 4))
graph.append(("e4", "e5", 3))
graph.append(("e1", "e4", 5))

mst = [("e2", "e3", 2), ("e4", "e5", 3), ("e1", "e3", 4), ("e1", "e4", 5)]

# TODO
testcases = [
    TestCase(1, to_adjacency_list, [edges], adj_list),
    TestCase(2, to_adjacency_matrix, [edges], adj_matrix),
    TestCase(3, find_shortest_path_distance, ["v1", "v4", edges], 2),
    TestCase(4, find_shortest_path_distance, ["v4", "v5", edges], -1),
    TestCase(5, find_shortest_path, ["v1", "v4", edges], ["v1", "v2", "v4"]),
    TestCase(6, find_shortest_path, ["v1", "v6", edges], ["v1", "v2", "v5", "v6"]),
    TestCase(7, find_shortest_path_wt, ["v1", "v6", edges, 5], ["v1", "v2", "v5", "v6"]),
    TestCase(8, find_valid_course_ordering_if_exists, [courses, 4], [0, 1, 2, 3]),
    TestCase(9, find_valid_course_ordering_if_exists, [courses_none, 4], None),
    TestCase(10, output_mst, [graph], mst)
]

for testcase in testcases:
    testcase.execute()

# ===== END DO NOT MODIFY =====