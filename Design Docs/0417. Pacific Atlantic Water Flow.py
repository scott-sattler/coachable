from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        solutions = list()

        # create solution sets
        solutions_p = set()
        solutions_a = set()

        # # dfs from pacific and atlantic
        # pacific
        visited = set()
        # top
        for j in range(len(heights[0])):
            # visited = set()
            self.dfs(heights, visited, solutions_p, heights[0][j], 0, j)
        # left
        for i in range(len(heights)):
            # visited = set()
            self.dfs(heights, visited, solutions_p, heights[i][0], i, 0)

        # atlantic
        visited = set()
        # right
        for i in range(len(heights)):
            j = len(heights[0]) - 1
            self.dfs(heights, visited, solutions_a, heights[i][j], i, j)
        # bottom
        for j in range(len(heights[0])):
            i = len(heights) - 1
            self.dfs(heights, visited, solutions_a, heights[i][j], i, j)

        for p in solutions_p:
            if p in solutions_a:
                solutions.append(p)
        return solutions

    # dfs from oceans
    def dfs(self, heights, visited, solutions, prev_val, i, j):
        # optimization
        if (i, j) in solutions:
            return

        # boundaries
        if not (len(heights) > i > -1 and len(heights[0]) > j > -1):
            return

        # bail on bad paths
        if heights[i][j] < prev_val:
            return

        # add to visited set
        if (i, j) in visited:
            return
        visited.add((i, j))

        solutions.add((i, j))

        self.dfs(heights, visited, solutions, heights[i][j], i - 1, j)
        self.dfs(heights, visited, solutions, heights[i][j], i + 1, j)
        self.dfs(heights, visited, solutions, heights[i][j], i, j - 1)
        self.dfs(heights, visited, solutions, heights[i][j], i, j + 1)


if __name__ == '__main__':
    test_cases = [
        (
            [[1, 2, 2, 3, 5],
             [3, 2, 3, 4, 4],
             [2, 4, 5, 3, 1],
             [6, 7, 1, 4, 5],
             [5, 1, 1, 2, 4]],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        ),
        (
            [[1, 1], [1, 1]],
            [[i, j] for j in range(2) for i in range(2)]
        ),
        (
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[i, j] for j in range(4) for i in range(4)]
        ),

        (
            [[10, 10, 10], [10, 1, 10], [10, 10, 10]],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
        ),
        (
            [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]],
            [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        ),

    ]

    for test in test_cases:
        inp = test[0]
        exp = test[1]
        exp = sorted(exp)
        # act = SolutionIterative().islandPerimeter(inp)
        # act = SolutionRecursive().islandPerimeter(inp)
        act = Solution().pacificAtlantic(inp)
        convert = lambda x: [list(i) for i in x]  # noqa
        act = convert(act)
        act = sorted(act)
        print("input: ", str(inp) + '\n', "expected: ", str(exp) + '\n', "actual: ", act, sep='')
        print()
        assert act == exp
