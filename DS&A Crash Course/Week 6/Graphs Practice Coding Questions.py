from __future__ import annotations

import unittest

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] 
means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''


def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
    # create a dictionary of parent -> list[children]
    adj_list = dict()
    for edge in edges:
        # create entry if node un-encountered
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        # update node's neighbor list
        adj_list[edge[0]].append(edge[1])
        # ensure any nodes that have no
        # children, still have an entry
        if edge[1] not in adj_list:
            adj_list[edge[1]] = []

    return adj_list


'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''


def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
    # never sure about how to impose order...

    # preprocessing
    adj_list = to_adjacency_list(edges)
    index_map = {k: i for i, k in enumerate(adj_list.keys())}

    # matrix construction
    adj_matrix = list()
    for parent in adj_list:  # preserves /appearance/ order
        row = [0] * len(adj_list)
        for child in adj_list[parent]:
            index = index_map[child]
            row[index] = 1
        adj_matrix.append(row)

    return adj_matrix


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
    import heapq  # heapq limited
    # import min_heap

    # 'lazy' heap (below):
    # increases time complexity from O((V + E) * log V) to O((V + E) * log E)
    # increases space complexity from O(V) to O(E)

    adj_list = to_adjacency_list(edges)
    min_h = list()
    dist = dict()
    visited = set()  # dict -> (status, previous node)

    # initialize unbound
    for vert in adj_list.keys():
        min_h.append((float('inf'), vert))
        dist[vert] = float('inf')

    # min_h.append(0, s)
    visited.add(s)
    dist[s] = 0
    # min_h.update(s, 0)

    # while unexplored nodes
    while min_h:
        # pick the next shortest path node (greedy)
        next_vert = heapq.heappop(min_h)[1]
        # consider all neighbors
        for neighbor in adj_list[next_vert]:
            if neighbor in visited:
                continue
            # if better distance found, relax
            if dist[next_vert] + 1 < dist[neighbor]:
                dist[neighbor] = dist[next_vert] + 1
                # update heap (decrease key not implemented in heapq)
                heapq.heappush(min_h, (dist[neighbor], neighbor))  # 'lazy'
                # for O((V + E) * log V): min_h.update(neighbor, dist[neighbor]), using min_heap

    return dist[d] if dist[d] < float('inf') else -1


'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''


def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
    # Dijkstra's
    import heapq

    adj_list = to_adjacency_list(edges)
    heap = list()
    visited = set()
    distance = dict()
    prev = dict()

    # initialize
    for node in adj_list.keys():
        distance[node] = float('inf')
        prev[node] = None
        heapq.heappush(heap, (float('inf'), node))

    distance[s] = 0
    visited.add(s)
    heapq.heappush(heap, (0, s))

    # while unexplored nodes exist
    while heap:
        # get the next nearest node (greedy)
        next_node = heapq.heappop(heap)[1]
        # and explore it
        for neighbor in adj_list[next_node]:
            # if not already explored
            if neighbor in visited:
                continue
            new_dist = distance[next_node] + 1  # + edge wight
            # relax distance if shorter path found
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                prev[neighbor] = next_node
                heapq.heappush(heap, (new_dist, neighbor))  # no .update() -> worse time/space O((V + E) * log E)/O(E)

    # construct path
    path = list()
    node = d
    while node:
        path.append(node)
        node = prev[node]

    return path[::-1] if path[-1] == s else -1


'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''


def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
    # Dijkstra's
    import heapq

    adj_list = to_adjacency_list(edges)
    heap = list()
    visited = set()
    distance = dict()
    prev = dict()

    # initialize
    for node in adj_list.keys():
        distance[node] = float('inf')
        prev[node] = None
        heapq.heappush(heap, (float('inf'), node))

    distance[s] = 0
    visited.add(s)
    heapq.heappush(heap, (0, s))

    # while unexplored nodes exist
    while heap:
        # get the next nearest node (greedy)
        next_node = heapq.heappop(heap)[1]
        # and explore it
        for neighbor in adj_list[next_node]:
            # if not already explored
            if neighbor in visited:
                continue
            new_dist = distance[next_node] + k  # + edge wight
            # relax distance if shorter path found
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                prev[neighbor] = next_node
                heapq.heappush(heap, (new_dist, neighbor))  # no .update() -> worse time/space O((V + E) * log E)/O(E)

    # construct path
    path = list()
    node = d
    while node:
        path.append(node)
        node = prev[node]

    return path[::-1] if path[-1] == s else -1

    pass


'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''


def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
    top_sorted = list()

    # topological order is an ordering where all predecessors come before their successors

    # not sure how to properly set list size...
    out_degrees = dict()
    in_degrees = dict()

    for parent, child in prerequisites:
        # out-degrees
        if parent not in out_degrees:
            out_degrees[parent] = []
        out_degrees[parent].append(child)
        if child not in out_degrees:
            out_degrees[child] = []

        # in-degrees
        if child not in in_degrees:
            in_degrees[child] = 0
        in_degrees[child] += 1
        # instances where node has 0 in-degrees
        if parent not in in_degrees:
            in_degrees[parent] = 0

    # find zero incoming
    no_incoming = list()  # stack
    for node in in_degrees:
        if in_degrees[node] == 0:
            no_incoming.append(node)

    # while nodes without dependencies exist
    while no_incoming:
        # decrement children of nodes
        # with zero dependencies
        next_node = no_incoming.pop()
        top_sorted.append(next_node)
        for node in out_degrees[next_node]:
            in_degrees[node] -= 1
            if in_degrees[node] == 0:
                no_incoming.append(node)

    return top_sorted if len(top_sorted) == len(set(in_degrees).union(out_degrees)) else None


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
    # 'Lazy' Prim's (not eager)
    import heapq
    queue = list()
    visited = set()
    mst = list()

    # arbitrarily select starting node
    # while PQ or MST incomplete:
    # add all neighboring edges to PQ
    # find the smallest edge not stale
    # add next vertex to MST

    # includes:
    # 'lazy' - adding edges when encountered (this works bc greedy - Dijkstra's)
    #          also possibly because our queue is polluted ?
    # 'early termination' - terminate when all nodes visited (remaining edges are all worse or stale)

    # bidirectional adjacency list
    mst_adj_list = dict()
    for parent, child, value in edges:
        if parent not in mst_adj_list:
            mst_adj_list[parent] = []
        mst_adj_list[parent].append((value, parent, child))
        if child not in mst_adj_list:
            mst_adj_list[child] = []
        mst_adj_list[child].append((value, child, parent))

    edges = [(value, parent, child) for parent, child, value in edges]  # adds O(E)
    vertex = edges[0][1]  # arbitrarily select starting node
    queue = mst_adj_list[vertex]  # seed queue
    heapq.heapify(queue)

    # dequeue until empty or mst complete
    while queue and len(mst) < len(mst_adj_list):
        # traverse to next unvisited node
        value, parent, child = heapq.heappop(queue)
        if child in visited:
            continue
        visited.add(child)

        mst.append(tuple(sorted([parent, child]) + [value]))

        # add unvisited, connected edges to queue
        for value, parent, child in mst_adj_list[child]:
            if child in visited:
                continue
            heapq.heappush(queue, (value, parent, child))  # O(E * log E) ?

    return mst if (len(mst) + 1) == len(mst_adj_list) else list()


class TestClass(unittest.TestCase):
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
        assert find_valid_course_ordering_if_exists(self.courses_none, 4) == None

    def test_output_mst_1(self):
        assert set(output_mst(self.graph)) == set(self.mst)
