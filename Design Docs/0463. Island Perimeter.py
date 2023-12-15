from typing import List


class SolutionIterative:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """ counts adjacent land """
        rows = len(grid)
        cols = len(grid[0])

        adjacent = 0
        agenda = list()  # stack
        visited = set()

        # find land
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    agenda.append((i, j))
                    break
            else:
                continue
            break

        # explore land (DFS)
        while agenda:
            # get next node and mark visited
            current = agenda.pop()
            if current in visited:
                continue
            visited.add(current)

            # explore NSEW
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
            for direction in directions:
                i = current[0] + direction[0]
                j = current[1] + direction[1]
                # boundary test and land test
                if (rows > i > -1 and cols > j > -1) and grid[i][j] == 1:
                    adjacent += 1
                    agenda.append((i, j))  # add explorable land to agenda

        return (4 * len(visited)) - adjacent


class SolutionRecursive:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """ counts water/boundary """
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        # find land
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return self.dfs(grid, (i, j), visited)

    # count water edges and boundaries
    def dfs(self, grid: List[List[int]], pos: tuple[int, int], visited: set) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # update visited set
        if pos in visited:
            return 0
        visited.add(pos)

        # explore NSEW
        count = 0
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        for direction in directions:
            i = pos[0] + direction[0]
            j = pos[1] + direction[1]
            # oo bounds test
            if (i < 0 or i >= rows) or (j < 0 or j >= cols):
                count += 1
            # water test
            elif grid[i][j] == 0:
                count += 1
            # not oob, not water; visited check
            elif (i, j) not in visited:
                count += self.dfs(grid, (i, j), visited)

        return count





if __name__ == '__main__':
    test_cases = [
        (
            [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]],
            16
        ),
        (
            [[1]],
            4
        ),
        (
            [[1], [1]],
            6
        ),
        (
            [[1, 1], [1, 1]],
            8
        ),
    ]

    for test in test_cases:
        inp = test[0]
        exp = test[1]
        # act = SolutionIterative().islandPerimeter(inp)
        act = SolutionRecursive().islandPerimeter(inp)
        print("input: ", str(inp) + '\n', "expected: ", str(exp) + '\n', "actual: ", act, sep='')
        assert act == exp
