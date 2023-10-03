from __future__ import annotations

import unittest

'''
There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the 
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the 
bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
Question 1. Solve the above problem using Top Down Dynamic Programming
'''


# time: O(m*n)
# space: O(1) input; O(m+n) call stack; O(m*n) memo
def unique_paths_top_down(m: int, n: int) -> int:
    '''
    invert path:
    (0, 0)


            (m-1, n-1)
    '''
    memo = dict()
    return _unique_paths_top_down(m, n, memo)


def _unique_paths_top_down(m: int, n: int, memo) -> int:
    # memo check
    if (m, n) in memo:
        return memo[(m, n)]

    # boundary
    if m < 1 or n < 1:
        memo[(m, n)] = 0
    # check path found
    elif (m, n) == (1, 1):
        memo[(m, n)] = 1
    # look up (m) and left (n)
    else:
        memo[(m, n)] = _unique_paths_top_down(m - 1, n, memo) + _unique_paths_top_down(m, n - 1, memo)

    return memo[(m, n)]


'''
Question 2. Solve the above problem using Bottom Up Dynamic Programming
'''


# time: O(m*n)
# space: O(1) input; O(n) aux
def unique_paths_bottom_up(m: int, n: int) -> int:
    '''
    (0, 0)


          (m-1, n-1)
    '''
    '''
    [0, 1, 1, 1]
    [1, 2, 3, 4]
    [1, 3, 4, 5]
    
    '''
    '''
    [10, 06, 03, 01]
    [04, 03, 02, 01]
    [01, 01, 01, 00]
    '''

    prev = [1] * n

    for _ in range(1, m):
        for j in range(1, n):
            prev[j] = prev[j - 1] + prev[j]

    return prev[-1]


class TestClass(unittest.TestCase):

    def test_unique_paths_top_down_1(self):
        assert unique_paths_top_down(3, 7) == 28

    def test_unique_paths_top_down_2(self):
        assert unique_paths_top_down(7, 3) == 28

    def test_unique_paths_top_down_3(self):
        assert unique_paths_top_down(3, 2) == 3

    def test_unique_paths_top_down_4(self):
        assert unique_paths_top_down(2, 3) == 3

    def test_unique_paths_bottom_up_1(self):
        assert unique_paths_bottom_up(3, 7) == 28

    def test_unique_paths_bottom_up_2(self):
        assert unique_paths_bottom_up(7, 3) == 28

    def test_unique_paths_bottom_up_3(self):
        assert unique_paths_bottom_up(3, 2) == 3

    def test_unique_paths_bottom_up_4(self):
        assert unique_paths_bottom_up(2, 3) == 3
