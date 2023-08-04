from __future__ import annotations

'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. Given an input n, where n >= 1, return 
the number of ways you can reach the top of the staircase. 

Do not worry about writing an optimal solution, and focus only on correctness.

Example Input: n = 3
Example Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


def question9(n: int) -> int:
    k = 0
    return _question9(k, n)


def _question9(k, n):
    if k == n:
        return 1

    if k > n:
        return 0

    return _question9(k + 1, n) + _question9(k + 2, n)


'''
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner. Coordinate (0,0)
The robot tries to move to the bottom-right corner. coordinates(m-1, n-1)
The robot can only move either down or right at any point in time.
m, n are strictly positive. 

Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.

Write a recursive solution to solve this problem. 

Do not worry about writing an optimal solution, and focus only on correctness.

Example Input: m = 3, n = 2
Example Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''


def question10(m: int, n: int) -> int:
    i, j = 0, 0
    return _question10(i, j, -(m - 1), -(n - 1))


def _question10(i, j, m, n) -> int:
    # here, (m, n) are indices
    if (i, j) == (m, n):
        return 1

    if i < m or j < n:
        return 0

    return _question10(i - 1, j, m, n) + _question10(i, j - 1, m, n)


# from stencil import *

def test_question9_case1():
    assert question9(1) == 1


def test_question9_case2():
    assert question9(2) == 2


def test_question9_case3():
    assert question9(3) == 3


def test_question9_case4():
    assert question9(7) == 21


def test_question10_case1():
    assert question10(3, 7) == 28


def test_question10_case2():
    assert question10(3, 2) == 3


def test_question10_case3():
    assert question10(2, 3) == 3


def test_question10_case4():
    assert question10(1, 1) == 1
