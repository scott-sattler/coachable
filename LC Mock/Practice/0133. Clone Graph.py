"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # map: original -> deep copy
        node_map = dict()

        ## create copy of each node
        # track visited
        visited = set()
        # seed agenda
        agenda = [node]
        while agenda:
            # get next node
            current_node = agenda.pop()
            if current_node in visited:
                continue
            # add to visited
            visited.add(current_node)
            # update node map
            node_map[current_node] = Node(current_node.val)
            # push unvisited neighbors to stack
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    agenda.append(neighbor)

        ## link each node
        visited = set()
        agenda = [node]
        while agenda:
            current_node = agenda.pop()
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor in current_node.neighbors:
                # link copy to each neighbor copy
                node_map[current_node].neighbors.append(node_map[neighbor])
                if neighbor not in visited:
                    agenda.append(neighbor)

        return node_map[node]
