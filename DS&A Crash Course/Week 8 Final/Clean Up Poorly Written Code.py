###############################################################################
#                                   PART I                                    #
###############################################################################

# The bad code, cleaned up.

# x-y shouldn't be used for nested list data structures
# use i (y), j (x)

class NetworkNode:                                                              # network_node -> NetworkNode; case convention  # noqa
    def __init__(self, node_type: str, value: int):                             # type -> node_type; shadows built-in
        self.node_type = node_type                                              # self.type -> self.node_type; shadows built-in  # noqa
        self.value = value

                                                                                # PEP8 spaces  # noqa
def check_connected(grid: list[list[NetworkNode]], max_diff: int) -> bool:      # List -> list; removed import  # noqa
    explored = set()                                                            # goodNodes -> good_nodes; naming convention  # noqa
                                                                                # good_nodes -> explored; convention  # noqa
    node_queue = [(0, 0)]                                                       # todo_NodeQ -> node_queue; naming convention  # noqa
                                                                                # could also use "agenda", or similr standard  # noqa

    while len(node_queue):                                                      # len(node_queue) > 0 -> len(node_queue); personal convention  # noqa
                                                                                # ... or even just node_queue  # noqa
        node = node_queue.pop()
        if node not in explored:
            explored.add(node)
            if node == (len(grid) - 1, len(grid[0]) - 1):
                return True

            if 0 <= (node[0] + 1) < len(grid):                                  # simplify chained comparision w/ personal ( ) addition  # noqa
                current_node = grid[node[0]][node[1]]                           # cur_Node -> current_node; naming convention  # noqa
                up = grid[node[0] + 1][node[1]]                                 # nodeplusOne_toX -> up; naming convention w/ personal    # noqa
                if up.node_type == current_node.node_type:
                    explored.add((node[0] + 1, node[1]))
                    node_queue.append((node[0] + 1, node[1]))

                elif abs(current_node.value - up.value) <= max_diff:
                    explored.add((node[0] + 1, node[1]))
                    node_queue.append((node[0] + 1, node[1]))

            if 0 <= (node[0] - 1) < len(grid):
                current_node = grid[node[0]][node[1]]
                down = grid[node[0] - 1][node[1]]                               # nodeMinusOne_toX -> down; naming convention w/ personal  # noqa
                if down.node_type == current_node.node_type:
                    explored.add((node[0] - 1, node[1]))
                    node_queue.append((node[0] - 1, node[1]))

                elif abs(current_node.value - down.value) <= max_diff:
                    explored.add((node[0] - 1, node[1]))
                    node_queue.append((node[0] - 1, node[1]))

            # switched with left
            if 0 <= node[1] + 1 and node[0] + 1 < len(grid[0]):                 # syntatical error: len(grid)[0] -> len(grid[0])  # noqa
                current_node = grid[node[0]][node[1]]
                right = grid[node[0]][node[1] + 1]                              # nodePlusOne_toY -> right; naming convetion w/ personal  # noqa
                if right.node_type == current_node.node_type:
                    explored.add((node[0], node[1] + 1))
                    node_queue.append((node[0], node[1] + 1))

                elif abs(current_node.value - right.value) <= max_diff:
                    explored.add((node[0], node[1] + 1))
                    node_queue.append((node[0], node[1] + 1))

            # switched with right
            if 0 <= node[1] - 1 and node[0] - 1 < len(grid[0]):                 # syntatical error: len(grid)[0] -> len(grid[0])  # noqa
                current_node = grid[node[0]][node[1]]
                left = grid[node[0]][node[1] - 1]                               # nodeMinusOne_toY -> left; naming convention w/ personal  # noqa
                if left.node_type == current_node.node_type:
                    explored.add((node[0], node[1] - 1))
                    node_queue.append((node[0], node[1] - 1))

                elif abs(current_node.value - left.value) <= max_diff:
                    explored.add((node[0], node[1] - 1))
                    node_queue.append((node[0], node[1] - 1))
                                                                                # PEP8 spacing  # noqa
    if (len(grid) - 1, len(grid[0]) - 1) in explored:
        return True

    return False


###############################################################################
#                                   PART II                                   #
#                         restructure/refactor/rewrite                        #
###############################################################################

# too many structural errors

class NetworkNode:
    def __init__(self, node_type: str, value: int):
        self.node_type = node_type
        self.value = value


def check_connected(grid: list[list[NetworkNode]], max_diff: int) -> bool:
    # cardinal -> north, south, east, west
    cardinal = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    explored = set()
    node_queue = [(0, 0)]

    while node_queue:
        node = node_queue.pop()
        if node in explored:
            continue
        explored.add(node)

        if node == (len(grid) - 1, len(grid[0]) - 1):
            return True

        # cardinal -> north, south, east, west
        for direction in cardinal:
            seen = (node[0] + direction[0], node[1] + direction[1])
            # bounds check
            if (seen[0] < 0) or (seen[1] < 0):
                continue
            if (seen[0] >= len(grid[0])) or (seen[1] >= len(grid[1])):
                continue
            # node "type" (color) check
            if grid[node[0]][node[1]].node_type == grid[seen[0]][seen[1]].node_type:
                node_queue.append(seen)
                continue
            # difference (value) check
            if abs(grid[node[0]][node[1]].value - grid[seen[0]][seen[1]].value) <= max_diff:
                node_queue.append(seen)

    return False


test = [
    [NetworkNode('blue', 1,), NetworkNode('blue', 4), NetworkNode('red', 7)],
    [NetworkNode('red', 4,), NetworkNode('blue', 10), NetworkNode('yellow', 7)],
    [NetworkNode('blue', 4,), NetworkNode('yelloow', 8), NetworkNode('yellow', 7)]
]

print(check_connected(test, 2))
