
from __future__ import annotations

'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot 
tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any 
point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
bottom-right corner.

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


# extended learning: brute force solution
# time: O(2^(m + n))
# auxiliary O(m + n)
def unique_paths(m: int, n: int) -> int:
    return _unique_paths(0, 0, m, n)


def _unique_paths(i: int, j: int, m: int, n: int) -> int:
    if i > m or j > n:
        return 0
    if i == (m - 1) and j == (n - 1):
        return 1
    return _unique_paths(i + 1, j, m, n) + _unique_paths(i, j + 1, m, n)


###############


# Question 1. Solve the above problem using Top Down Dynamic Programming
def unique_paths_top_down(m: int, n: int) -> int:
    # recursion
    # memoization
    memo = {(0, 0): 0}
    return -1


# Question 2. Solve the above problem using Bottom Up Dynamic Programming
# time: O(m + n)
# auxiliary O(m * x)
def unique_paths_bottom_up(m: int, n: int) -> int:
    # iteration
    # tabulation
    table = [[0 for _ in range(n)] for _ in range(m)]

    # first row
    for j in range(n):
        table[0][j] = 1

    # first column
    for i in range(m):
        table[i][0] = 1

    # fill table
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[m - 1][n - 1]







for i in range(1, 5):
    ans = unique_paths_bottom_up(i, i)
    print(i, ans)

    print(i, unique_paths(i, i))
