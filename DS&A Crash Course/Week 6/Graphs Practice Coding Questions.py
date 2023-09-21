# from __future__ import annotations
import unittest


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


# Dijkstra's Algorithm
# todo just rewrite using minheap ffs
def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
    import max_heap  # maxheap

    p_que = max_heap.MaxHeap(track_index=True)
    visited = set()
    adj_list = to_adjacency_list(edges)

    distance = dict()
    for vertex in adj_list.keys():
        distance[vertex] = _v(float('inf'))
        p_que.push((_v(float('inf')), vertex))
    distance[s] = 0
    p_que.update_element(s, 0)

    while p_que:
        next_item = p_que.pop()
        vertex = next_item[1]
        visited.add(vertex)
        for neighbor in adj_list[vertex]:
            if neighbor in visited:
                continue

            new_dist = distance[vertex] + _v(1)  # all weights are 1
            if _v(new_dist) < _v(distance[neighbor]):  # reversed comparison using maxheap
                distance[neighbor] = new_dist

                p_que.update_element(neighbor, new_dist)

    return _v(distance[d]) if distance[d] != _v(float('inf')) else -1


def _v(val):
    return -val


def find_shortest_path_distance_bfs(s: str, d: str, edges: list[list[str]]) -> int:
    from collections import deque

    adj_list = to_adjacency_list(edges)
    seed = [[1, node] for node in adj_list[s]]
    queue = deque(seed)
    while queue:
        current = queue.popleft()
        neighbors = adj_list[current[-1]]
        for neighbor in neighbors:
            path = [current[0] + 1, neighbor]

            if path[1] == d:
                return path[0]

    return -1

'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''


# Dijkstra's: second attempt (min heap)
def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
    import heapq

    dist = dict()
    prev = dict()
    min_heap = list()
    adj_list = to_adjacency_list(edges)

    for v in adj_list.keys():
        if v != s:
            dist[v] = float('inf')
            prev[v] = None
            heapq.heappush(min_heap, (float('inf'), v))

    dist[s] = 0
    prev[s] = None
    min_heap = [(0, s, None)] + min_heap  # todo sift_up/decrease_key

    while min_heap:
        next_element = heapq.heappop(min_heap)
        next_vertex = next_element[1]
        neighbors = adj_list[next_vertex]
        for neighbor in neighbors:
            neighbor_dist = 1
            new_dist = dist[next_vertex] + neighbor_dist
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = next_vertex
                # todo update min_heap: sift_down/increase_key
                # heapq._sift_down(min_heap, neighbor, new_dist)

    next_node = prev[d]
    path = [d]
    while next_node:
        path.append(next_node)
        next_node = prev[next_node]

    return path[::-1]


def find_shortest_path_bfs_path(s: str, d: str, edges: list[list[str]]) -> list[str] | int:
    from collections import deque

    adj_list = to_adjacency_list(edges)
    queue = deque([[s, node] for node in adj_list[s]])
    while queue:
        current = queue.popleft()
        neighbors = adj_list[current[-1]]
        for neighbor in neighbors:
            path = current[:]
            if neighbor not in path:
                path.append(neighbor)
                queue.append(path)

            if path[-1] == d:
                return path

    return -1


'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''


def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
    # from min_heap import MinHeap
    return find_shortest_path(s, d, edges)


'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
    from collections import deque
    no_incoming = deque()
    top_sorted = list()

    # find max
    # for list/index approach
    # O(E)
    max_vert = 0
    for edge in prerequisites:
        if edge[1] > max_vert:
            max_vert = edge[1]

    # O(2V)
    in_degrees = [0] * (max_vert + 1)
    out_degrees: list[list[int]] = [[] for _ in range(max_vert + 1)]

    # find degrees
    # O(E)
    for edge in prerequisites:
        in_degrees[edge[1]] += 1
        out_degrees[edge[0]].append(edge[1])

    # find zero in-degrees
    # O(E) (max(V, E) where E >= V)
    for vertex_index in range(len(in_degrees)):
        if in_degrees[vertex_index] == 0:
            no_incoming.append(vertex_index)

    # while zero incoming exist,
    # decrement their outgoing,
    # adding newly zero incoming to queue
    # O(V + E)
    while no_incoming:
        vertex_index = no_incoming.popleft()
        top_sorted.append(vertex_index)
        for neighbor in out_degrees[vertex_index]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                no_incoming.append(neighbor)

    return top_sorted if len(top_sorted) == (max_vert + 1) else None


'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''


# 'lazy' Prim's
def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    import heapq
    mst = list()

    # build adjacency list
    mst_adj_list = dict()
    for edge in edges:
        if edge[0] not in mst_adj_list:
            mst_adj_list[edge[0]] = list()
        mst_adj_list[edge[0]].append((edge[2], edge[0], edge[1]))
        # undirected (v1, v2) implies both v1 -> v2 and v2 -> v1
        if edge[1] not in mst_adj_list:
            mst_adj_list[edge[1]] = list()
        mst_adj_list[edge[1]].append((edge[2], edge[1], edge[0]))

    vertex = edges[0][0]  # arbitrarily select starting vertex
    pq = mst_adj_list[vertex]  # seed pq
    heapq.heapify(pq)
    visited = {vertex}

    while pq and len(mst) < len(mst_adj_list):
        next_edge = heapq.heappop(pq)
        vertex = next_edge[2]
        if vertex in visited:
            continue

        mst.append(next_edge)
        visited.add(vertex)
        edges = mst_adj_list[vertex]
        for edge in edges:
            if edge[2] not in visited:
                heapq.heappush(pq, edge)

    print(mst)
    print(sorted(mst))
    return sorted(mst)


class TestClass(unittest.TestCase):
    adj_list = dict()
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

    graph = list()
    graph.append(("e1", "e2", 6))
    graph.append(("e2", "e3", 2))
    graph.append(("e1", "e3", 4))
    graph.append(("e4", "e5", 3))
    graph.append(("e1", "e4", 5))

    mst = [("e2", "e3", 2), ("e4", "e5", 3), ("e1", "e3", 4), ("e1", "e4", 5)]

    def test_to_adjacency_list_1(self):
        assert to_adjacency_list(self.edges) == self.adj_list

    def test_to_adjacency_matrix_1(self):
        assert to_adjacency_matrix(self.edges) == self.adj_matrix

    def test_find_shortest_path_distance_1(self):
        assert find_shortest_path_distance("v1", "v4", self.edges) == 2

    def test_find_shortest_path_distance_2(self):
        assert find_shortest_path_distance("v4", "v5", self.edges) == -1

    def test_find_shortest_path_1(self):
        assert find_shortest_path("v1", "v4", self.edges) == ["v1", "v2", "v4"]

    def test_find_shortest_path_2(self):
        assert find_shortest_path("v1", "v6", self.edges) == ["v1", "v2", "v5", "v6"]

    def test_find_shortest_path_wt_1(self):
        assert find_shortest_path_wt("v1", "v6", self.edges, 5) == ["v1", "v2", "v5", "v6"]

    def test_find_valid_course_ordering_if_exists_1(self):
        assert find_valid_course_ordering_if_exists(self.courses, 4) == [0, 1, 2, 3]

    def test_find_valid_course_ordering_if_exists_2(self):
        assert find_valid_course_ordering_if_exists(self.courses_none, 4) is None

    def test_output_mst_1(self):
        assert set(output_mst(self.graph)) == set(self.mst)

    # from stencil import *
    # from main_test import *

    # order should not be assumed
    edges_ooo = [["v4", "v3"], ["v5", "v6"], ["v6", "v4"], ["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"]]

    def test_to_adjacency_matrix_2(self):
        assert to_adjacency_matrix(self.edges_ooo) == self.adj_matrix
