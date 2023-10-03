from __future__ import annotations
import unittest

'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
Question 1. Solve the above problem using Top Down Dynamic Programming
'''


def unique_paths_top_down(m: int, n: int) -> int:
    pass


'''
Question 2. Solve the above problem using Bottom Up Dynamic Programming
'''


def unique_paths_bottom_up(m: int, n: int) -> int:
    pass


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
