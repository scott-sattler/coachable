from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        solutions = list()

        # create solution sets
        # i = 0 and j = 0 are top/left solutions
        goal_p = set((0, j) for j in range(cols))
        goal_p.update((i, 0) for i in range(rows))
        # i = len - 1 and j = len - 1 are bottom/right solutions
        goal_a = set((i, cols - 1) for i in range(rows))
        goal_a.update((rows - 1, j) for j in range(cols))

        # dfs across every cell
        for i in range(rows):
            for j in range(cols):
                visited = set()
                self.dfs(heights, visited, goal_p, (i, j), (i, j), i, j)
                visited = set()
                self.dfs(heights, visited, goal_a, (i, j), (i, j), i, j)

        # return solution set intersections
        # between Pacific and Atlantic
        for p in goal_p:
            if p in goal_a:
                solutions.append(p)
        return solutions

    def dfs(self, heights, visited, goal, orig, prev_ij, i, j):
        # boundary test
        if not (len(heights) > i > -1 and len(heights[0]) > j > -1):
            return

        # problem constraint test
        # must be equal or decreasing
        if heights[i][j] > heights[prev_ij[0]][prev_ij[1]]:
            return

        # exclude visited nodes
        if (i, j) in visited:
            return
        visited.add((i, j))

        # update goal set if
        # goal path found
        if (i, j) in goal:
            if (i, j) != prev_ij:
                goal.add(orig)
            return

        # explore
        self.dfs(heights, visited, goal, orig, (i, j), i - 1, j)
        self.dfs(heights, visited, goal, orig, (i, j), i + 1, j)
        self.dfs(heights, visited, goal, orig, (i, j), i, j - 1)
        self.dfs(heights, visited, goal, orig, (i, j), i, j + 1)




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
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
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
