import unittest


class MaxHeap:
    """    one-based indexing    """
    def __init__(self, default=None):
        if default is None:
            default = []
        if not isinstance(default, list):
            raise TypeError

        self.heap = [0] + default

        if len(self.heap) > 2:
            self.heapify()

    def __repr__(self):
        return str(self.heap[1:])

    def push(self, element: int | float) -> None:
        self.heap.append(element)
        self._sift_up()

    def _sift_up(self) -> None:
        child_i = len(self.heap) - 1
        parent_i = child_i // 2
        while self.heap[child_i] > self.heap[parent_i]:
            self.heap[parent_i], self.heap[child_i] = self.heap[child_i], self.heap[parent_i]

            child_i = parent_i
            parent_i = child_i // 2

            if parent_i < 1:
                break

    def pop(self) -> any:
        if len(self.heap) < 2:
            return None

        if len(self.heap) > 2:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        else:
            self.heap[0], self.heap[1] = self.heap[1], self.heap[0]
            return self.heap.pop()

        pop_element = self.heap.pop()
        self._sift_down()

        return pop_element

    def _sift_down(self, parent: int = 1) -> None:
        parent_i = parent
        child_i = parent_i * 2
        if child_i >= len(self.heap):
            return None

        right = child_i + 1 if child_i + 1 < len(self.heap) else child_i
        if self.heap[right] > self.heap[child_i]:
            child_i = right

        while self.heap[parent_i] < self.heap[child_i]:
            self.heap[parent_i], self.heap[child_i] = self.heap[child_i], self.heap[parent_i]

            parent_i = child_i
            child_i = parent_i * 2
            if child_i >= len(self.heap):
                break
            right = child_i + 1 if child_i + 1 < len(self.heap) else child_i
            if self.heap[right] > self.heap[child_i]:
                child_i = right

    # pop root and push new key (avoids duplicate balance)
    def replace(self, replace_max_with):
        replaced_elem = self.heap[1]
        self.heap[1] = replace_max_with
        self._sift_down()
        return replaced_elem

    # O(n)
    # https://stackoverflow.com/q/9755721
    def heapify(self) -> list:
        # siftdown avoids last level
        last_parent = (len(self.heap) - 1) // 2
        for i in range(last_parent, 0, -1):
            self._sift_down(i)

        return self.heap[1:]

    @staticmethod
    def _parent(index: int):
        return index // 2

    @staticmethod
    def _left_child(index: int):
        return index * 2

    @staticmethod
    def _right_child(index: int):
        return index * 2 + 1


class TestMaxHeap(unittest.TestCase):
    # actual, expected
    def test_create_1(self):
        h = MaxHeap()
        expected = []
        self.assertEqual(h.heap[1:], expected)

    def test_create_2(self):
        h = MaxHeap([0])
        expected = [0]
        self.assertEqual(h.heap[1:], expected)

    def test_create_3(self):
        h = MaxHeap([1, 0])
        expected = [1, 0]
        self.assertEqual(h.heap[1:], expected)

    def test_create_4(self):
        h = MaxHeap([0, 1])
        expected = [1, 0]
        self.assertEqual(h.heap[1:], expected)

    def test_create_5(self):
        h = MaxHeap([0, 1, 2])
        expected = [2, 1, 0]
        self.assertEqual(h.heap[1:], expected)

    def test_create_6(self):
        h = MaxHeap([0, 1, 2, 3, 4, 5, 6, 7])
        expected = [7, 4, 6, 3, 0, 5, 2, 1]
        self.assertEqual(h.heap[1:], expected)

    def test_create_7(self):
        h = MaxHeap([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        expected = [11, 10, 6, 8, 9, 5, 0, 7, 3, 1, 4, 2]
        self.assertEqual(h.heap[1:], expected)

    def test_push_1(self):
        h = MaxHeap([0])
        h.push(1)
        h.push(2)
        expected = [2, 0, 1]
        self.assertEqual(h.heap[1:], expected)

    def test_pop_1(self):
        h = MaxHeap([8, 6, 1, 3, 5])
        h.pop()
        expected = [6, 5, 1, 3]
        self.assertEqual(h.heap[1:], expected)

    def test_pop_2(self):
        h = MaxHeap([8, 6, 1, 3, 5])
        h.pop()
        h.pop()
        expected = [5, 3, 1]
        self.assertEqual(h.heap[1:], expected)

    def test_pop_3(self):
        h = MaxHeap([6, 5, 1, 3])
        h.pop()
        expected = [5, 3, 1]
        self.assertEqual(h.heap[1:], expected)

    def test_sift_down_heapify_1(self):
        h = MaxHeap([5, 3, 1, 8, 6])
        expected = [8, 6, 1, 3, 5]
        self.assertEqual(h.heap[1:], expected)

# h = MaxHeap()
# print(h)
# h.push(0)
# print(h)
# h.push(1)
# print(h)
# h.push(2)
# print(h)
# h.push(3)
# print(h)
# h.push(4)
# print(h)
# h.push(5)
# print(h)
#
# print('pop', h.pop(), end=' ')
# print(h)
# print('pop', h.pop(), end=' ')
# print(h)
# print('pop', h.pop(), end=' ')
# print(h)
# print('pop', h.pop(), end=' ')
# print(h)
# print('pop', h.pop(), end=' ')
# print(h)
# print('pop', h.pop(), end=' ')
# print(h)
# print('pop', h.pop(), end=' ')
# print(h)


# h = MaxHeap([1])
# print(h.heap)
# h = MaxHeap([1, 2])
# print(h.heap)
# h = MaxHeap([1, 2, 3])
# print(h.heap)
# h = MaxHeap([1, 2, 3, 4])
# print(h.heap)
# h = MaxHeap([1, 2, 3, 4, 5])
# print(h.heap)



# a_heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# #                   1                       1   1
# #           2                 3             2   3
# #       4       5         6       7         4   7
# #     8   9  10   11    12  13  14  15      8   15
#
# i = 1
# parent = i // 2  # parent
# left_child = i * 2
# right_child = i * 2 + 1