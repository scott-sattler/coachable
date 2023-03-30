
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


# brute force
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
    memo: dict[tuple[int, int], int] = {(0, 0): 0}
    memo.update({(row, 0): 1 for row in range(1, m)})
    memo.update({(0, col): 1 for col in range(1, n)})
    return _unique_paths_top_down(memo, 1, 1, m, n)


def _unique_paths_top_down(memo, i: int, j: int, m: int, n: int) -> int:
    if i > m or j > n:
        return 0
    if i == m and j == n:
        return 1
    if (m, n) not in memo:
        prev_up = 0
        if i > 0 and memo.get((i - 1, j)) is not None:
            prev_up = memo[(i - 1, j)]

        prev_left = 0
        if j > 0 and memo.get((i, j - 1)) is not None:
            prev_left = memo[(i, j - 1)]

        memo[(i, j)] = min(1, prev_up) + min(1, prev_left)

    return _unique_paths_top_down(memo, i + 1, j, m, n) + _unique_paths_top_down(memo, i, j + 1, m, n)


# Question 2. Solve the above problem using Bottom Up Dynamic Programming
# time: O(m * n)
# auxiliary O(m * n)
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


###############


# table space optimization
# time: O(m * n)
# auxiliary O(min(m, n))
def unique_paths_bottom_up_opt(m: int, n: int) -> int:
    table_min = [1 for _ in range(min(m, n))]

    for _ in range(1, max(m, n)):
        for a in range(1, min(m, n)):
            table_min[a] = table_min[a] + table_min[a - 1]

    return table_min[-1]


# lesser table space optimization with obstacles
# time: O(m * n)
# auxiliary O(m)
def unique_paths_bottom_up_opt_obst(obstacles: list[list[int]]) -> int:
    m = len(obstacles)
    n = len(obstacles[0])
    table = [1 for _ in range(m)]

    for i in range(1, n):
        for j in range(1, m):
            if obstacles[i][j] == 0:
                table[j] = table[j] + table[j - 1]
            else:
                table[j] = 0
    return table[-1]


# path lists
# time: O(n * m)
# auxiliary O(m * n)
# can use dfs queue w/ auxiliary O(n + m)
def unique_path_lists(m: int, n: int) -> int:
    agenda = [[(0, 0)]]
    count = 0
    while agenda:
        cur_path = agenda.pop()
        if cur_path[-1] == (m - 1, n - 1):
            count += 1
            continue
        # extend paths and update agenda
        if cur_path[-1][0] < m and cur_path[-1][1] < n:
            down = cur_path + [(cur_path[-1][0] + 1, cur_path[-1][1])]
            right = cur_path + [(cur_path[-1][0], cur_path[-1][1] + 1)]
            agenda += [down, right]
    return count


tests = [
    (3, 5),
    (5, 3),
    (1, 1),
    (2, 2),
    (1, 2),
    (2, 1),
    (3, 3),
    (5, 2),
    (4, 6),
    (1, 7),
    (5, 7),
    (6, 6),
]
for i, j in tests:
    print((i, j), unique_paths_bottom_up(i, j))
    print((i, j), unique_paths(i, j))
    print((i, j), unique_paths_top_down(i, j))
    print((i, j), unique_path_lists(i, j))

    print((i, j), unique_paths_bottom_up_opt(i, j))
    print('----')

matrices = {
    'obst_3x3': [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ],
    'obst_5x5a': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    'obst_5x5b': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ],
    'obst_5x5c': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ],
}
for k, v in matrices.items():
    print(k, v, unique_paths_bottom_up_opt_obst(v))
