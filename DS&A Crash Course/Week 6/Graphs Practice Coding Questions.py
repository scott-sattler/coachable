from __future__ import annotations

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''

'''
["n1", "n2"]
n1 -> n2
n1 is a precondition of n2

n2 is dependent on n1
n2 has n1 dependency
'''


def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
    adjacency_list = dict()
    for edge in edges:
        if edge[0] in adjacency_list:
            adjacency_list[edge[0]].append(edge[1])
        else:
            adjacency_list[edge[0]] = [edge[1]]

        if edge[1] not in adjacency_list:
            adjacency_list[edge[1]] = []

    return adjacency_list  # unordered!


'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''


def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
    # rewrite w/o reference for practice
    adjacency_list = dict()
    for edge in edges:
        if edge[0] in adjacency_list:
            adjacency_list[edge[0]].append(edge[1])
        else:
            adjacency_list[edge[0]] = [edge[1]]

        if edge[1] not in adjacency_list:
            adjacency_list[edge[1]] = []

    # addresses unordered edge input
    adjacency_list = dict(sorted(adjacency_list.items(), key=lambda xy: xy[0]))

    adjacency_matrix = list()
    # get structure from adjacency_list
    for k, v in adjacency_list.items():
        row = list()
        for ordered_k in adjacency_list:
            if ordered_k in v:
                row.append(1)
            else:
                row.append(0)
        adjacency_matrix.append(row)

    return adjacency_matrix


'''
Suppose you’re given a list of graph edges where 
each edge is of the form ["e1", "e2"], meaning that 
"e1" is connected to "e2". You’re also given a source 
node s and destination node d.
'''

'''
Write an algorithm to return the distance of one of the shortest paths, 
where each connection costs 1 to traverse. Return -1 if there is no path.
'''


def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
    visited = dict()

    for vertex in edges:
        if vertex[1] in visited:
            visited[vertex[1]].append([1, vertex[0]])
        else:
            visited[vertex[1]] = [[1, vertex[0]]]

    print(visited)
    print('x' * 111)


'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''


def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
    pass


'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''


def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
    pass


'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
    pass


'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''


def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    pass


# from stencil import *

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


def test_to_adjacency_list_1():
    assert to_adjacency_list(edges) == adj_list


def test_to_adjacency_matrix_1():
    assert to_adjacency_matrix(edges) == adj_matrix


def test_find_shortest_path_distance_1():
    assert find_shortest_path_distance("v1", "v4", edges) == 2


def test_find_shortest_path_distance_2():
    assert find_shortest_path_distance("v4", "v5", edges) == -1


def test_find_shortest_path_1():
    assert find_shortest_path("v1", "v4", edges) == ["v1", "v2", "v4"]


def test_find_shortest_path_2():
    assert find_shortest_path("v1", "v6", edges) == ["v1", "v2", "v5", "v6"]


def test_find_shortest_path_wt_1():
    assert find_shortest_path_wt("v1", "v6", edges, 5) == ["v1", "v2", "v5", "v6"]


def test_find_valid_course_ordering_if_exists_1():
    assert find_valid_course_ordering_if_exists(courses, 4) == [0, 1, 2, 3]


def test_find_valid_course_ordering_if_exists_2():
    assert find_valid_course_ordering_if_exists(courses_none, 4) == None


def test_output_mst_1():
    assert set(output_mst(graph)) == set(mst)


# from stencil import *
# from main_test import *

# order should not be assumed
edges_ooo = [["v4", "v3"], ["v5", "v6"], ["v6", "v4"], ["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"]]


def test_to_adjacency_matrix_2():
    assert to_adjacency_matrix(edges_ooo) == adj_matrix
