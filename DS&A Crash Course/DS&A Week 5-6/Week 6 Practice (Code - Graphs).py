from __future__ import annotations
from collections import deque

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''


def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
  adjacency_dict: dict[str, list[str]] = dict()
  seen_nodes: set[str] = set()
  for edge in edges:
    if edge[0] in adjacency_dict:
      adjacency_dict[edge[0]] += [edge[1]]
      seen_nodes.add(edge[1])
    else:
      adjacency_dict[edge[0]] = [edge[1]]
    # if a seen child is never a parent
    if edge[1] not in adjacency_dict:
      adjacency_dict[edge[1]] = []

  return adjacency_dict


'''
Create an adjacency matrix for it where each respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''


def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
  adjacency_matrix: list[list[int]] = list()
  adjacency_list = to_adjacency_list(edges)
  for key, value in adjacency_list.items():  # rows
    matrix_row = []
    for each_vertex in adjacency_list.keys():  # columns
      if each_vertex in value:
        matrix_row.append(1)
      else:
        matrix_row.append(0)
    adjacency_matrix.append(matrix_row)
  return adjacency_matrix


'''
Suppose you’re given a list of graph edges where each edge is of the form ["e1", "e2"], meaning that "e1" is connected to "e2". You’re also given a source node s and destination node d.
'''

'''
Write an algorithm to return the distance of one of the shortest paths, where each connection costs 1 to traverse. Return -1 if there is no path.
'''


def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
  # on positive, uniform weight, graphs first BFS solution is optimal
  adjacency_list = to_adjacency_list(edges)
  agenda: deque[list[str]] = deque()  # can reduce space complexity via deque[tuple[str, int]] (last node, length)
  # visited: set[str] = set()  # detects/avoids loops when not recording paths
  agenda.append([s])
  while agenda:
    current_path = agenda.popleft()
    for neighbor in adjacency_list[current_path[-1]]:
      # if neighbor not in current_path:  # can be used to exclude loops
      extended_path = current_path + [neighbor]
      agenda.append(extended_path)
      if neighbor is d:
        return len(extended_path) - 1
  return -1


'''
Modify the above algorithm to return the path itself. For the test inputs, the path will always exist.
'''


def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
  # uniform weights, acyclic, graphs solved via first BFS solution
  adjacency_list = to_adjacency_list(edges)
  agenda: deque[list[str]] = deque([[s], ])
  while agenda:
    current_path = agenda.popleft()
    current_node = current_path[-1]
    for neighbor in adjacency_list[current_node]:
      # loop test
      if neighbor not in current_path:
        extended_path = current_path + [neighbor]
        agenda.append(extended_path)
        if neighbor is d:
          return extended_path


'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''


def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
  # same
  # where nonuniform, Dijkstras
  pass


'''
Given a list of course prerequisites each in the form [0, 1] where 0 is a prerequisite of 1 and n, the total number of courses, write a function to output a valid course ordering, or None if not possible. Courses are numbered from 0 to n-1.
'''


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
    # reverse postorder; topological sort
    # find nodes with no dependencies
    # remove these nodes as dependencies of other nodes
    # update in-degrees
    adjacency_list = to_adjacency_list(prerequisites)
    topologically_ordered: list = list()

    in_degrees = {k: 0 for k in adjacency_list}
    no_incoming = []

    # node in-degrees
    for key, value in adjacency_list.items():
        for neighbor in adjacency_list[key]:
            in_degrees[neighbor] += 1

    # find nodes without incoming
    for key, value in in_degrees.items():
        if value == 0:
            no_incoming.append(key)

    # construct topological list
    while no_incoming:
        node = no_incoming.pop()
        topologically_ordered.append(node)
        # decrement neighbors' in-degree
        for neighbor in adjacency_list[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                no_incoming.append(neighbor)

    return topologically_ordered if len(topologically_ordered) == len(adjacency_list) else None


'''
Suppose you’re given a list of graph edges where each edge is of the form ("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an edge weight of 3. The graph is connected. Write an algorithm to print out the an MST of the graph.
'''


def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
  pass







################################################################################  # noqa
################################################################################  # noqa
################################################################################  # noqa


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
courses = [[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]]
courses_none = [[0, 1], [1, 2], [2, 0]]

graph = []
graph.append(("e1", "e2" , 6))
graph.append(("e2", "e3", 2))
graph.append(("e1", "e3" , 4))
graph.append(("e4", "e5" , 3))
graph.append(("e1", "e4" , 5))

mst = [("e2", "e3", 2), ("e4", "e5" , 3), ("e1", "e3" , 4), ("e1", "e4" , 5)]

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


# test_to_adjacency_list_1()
# test_to_adjacency_matrix_1()
# test_find_shortest_path_distance_1()
# test_find_shortest_path_distance_2()
# test_find_shortest_path_1()
# test_find_shortest_path_2()

# test_find_shortest_path_wt_1()

# test_find_valid_course_ordering_if_exists_1()
test_find_valid_course_ordering_if_exists_2()
# test_output_mst_1()
