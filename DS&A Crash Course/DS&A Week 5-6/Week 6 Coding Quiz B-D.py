from __future__ import annotations
from collections import deque

'''
For Questions 6-8, you'll be given a recurrence relation and asked to turn it into code. 
You do not have to do it optimally. Assume that the input provided will always be nonnegative. 
'''

'''
Question 6. 
f(n) = f(n-1) + f(n-2)
f(0) = f(1) = 1
'''
def question6(n):
    if n < 2:
        return 1
    return question6(n - 1) + question6(n - 2)


'''
Question 7. 
f(n) = f(n-1) + f(n-2) + f(n-3)
f(0) = f(1) = f(2) = 1
'''
def question7(n):
    if n < 3:
        return 1
    return question7(n - 1) + question7(n - 2) + question7(n - 3)


'''
Question 8. 
is_even(n) = is_odd(n-1)
is_odd(n) = is_even(n-1)
is_even(0) = True
is_odd(0) = False

Return "even" if even, "odd" if odd, but your solution must use 
the above recursive structure and helper functions is_even(n) and is_odd(n).
'''
def question8(n):
    if n % 2 == 0:
        return "even"
    if n % 2 != 0:
        return "odd"
    return question8(n - 1)


# from stencil import *

def test_question6_case1():
    assert question6(10) == 89


def test_question7_case1():
    assert question7(10) == 193


def test_question8_case1():
    assert question8(0) == "even"


def test_question8_case2():
    assert question8(3) == "odd"


def test_question8_case3():
    assert question8(6) == "even"


assert question6(10) == 89
assert question7(10) == 193
assert question8(0) == "even"
assert question8(3) == "odd"
assert question8(6) == "even"



##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####


# from __future__ import annotations

'''
Question 9.

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and 
no other cities outside of the group.

You are given an n x n matrix is_connected where 
is_connected[i][j] = 1 if the ith city and the jth city are directly connected, 
and is_connected[i][j] = 0 otherwise.

Return the total number of provinces.

Note that 
* is_connected[i][i] == 0
* is_connected[i][j] == is_connected[j][i]
'''


def question9(is_connected: list[list[int]]) -> int:
    pass


# from stencil import *

def test_question9_case1():
    assert question9([[0]]) == 1


def test_question9_case2():
    assert question9([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == 2


def test_question9_case3():
    assert question9([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 3


def test_question9_case4():
    assert question9([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) == 1


def test_question9_case5():
    assert question9([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == 1


# assert question9([[0]]) == 1
# assert question9([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == 2
# assert question9([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 3
# assert question9([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) == 1
# assert question9([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == 1



##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####


# from __future__ import annotations

'''
Question 10.

There are a total of num_courses courses you have to take, 
labeled from 0 to num_courses - 1. 
You are given a list prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty list.
'''


def question10(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    # bi depends upon ai
    topologically_ordered = []

    # lol boo
    if len(prerequisites) < 1:
        return [i for i in range(num_courses)]

    adjacency_dict = dict()

    for each_prerequisite in prerequisites:
        parent = each_prerequisite[1]
        child = each_prerequisite[0]
        if parent in adjacency_dict:
            adjacency_dict[parent] += [child]
        else:
            adjacency_dict[parent] = [child]
        if child not in adjacency_dict:
            adjacency_dict[child] = []

    adjacency_list = adjacency_dict

    in_degrees = {k: 0 for k in adjacency_list}
    no_incoming = deque()

    # in-degrees
    for k in adjacency_dict.keys():
        for node in adjacency_dict[k]:
            in_degrees[node] += 1

    # no dependencies
    for k, v in in_degrees.items():
        if not v:
            no_incoming.append(k)

    while no_incoming:
        node = no_incoming.popleft()
        topologically_ordered.append(node)
        for neighbor in adjacency_list[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                no_incoming.append(neighbor)

    return topologically_ordered if len(topologically_ordered) == num_courses else []


# from stencil import *

def test_question10_case1():
    assert question10(2, [[1, 0]]) == [0, 1]


def test_question10_case2():
    assert question10(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in [[0, 1, 2, 3], [0, 2, 1, 3]]


def test_question10_case3():
    assert question10(1, []) == [0]


def test_question10_case4():
    assert question10(2, []) in [[0, 1], [1, 0]]


def test_question10_case5():
    assert question10(3, [[1, 0], [2, 1], [1, 2]]) == []


assert question10(2, [[1, 0]]) == [0, 1]
assert question10(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in [[0, 1, 2, 3], [0, 2, 1, 3]]

assert question10(1, []) == [0]
assert question10(2, []) in [[0, 1], [1, 0]]

assert question10(3, [[1, 0], [2, 1], [1, 2]]) == []
