from __future__ import annotations


class heap:
    def __init__(self):
        self.heap_array = list()

    def push(self, element: int | float):
        raise NotImplemented

    def pop(self):
        raise NotImplemented

    def heapify(self, arr: list):
        while arr:
            self.push(arr.pop())
        return self.heap_array




a_heap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#                   0                       1   1
#           1                 2             2   3
#       3       4         5       6         4   7
#     7   8   9   10    11  12  13  14      8   15

i = 0
parent = (i - 1) / 2  # parent
left_child = (2 * i) + 1
right_child = (2 * i) + 2

# a_heap[left_child]


# for i in range(len(a_heap)):
#     parent = (i - 1) / 2
#     left_child = (2 * i) + 1
#     right_child = (2 * i) + 2
#     print(parent, left_child, right_child)

