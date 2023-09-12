import unittest

# unused
class HeapNode:
    def __init__(self, val, obj, reverse=False):
        self.val = val
        self.obj = obj
        self.rev = reverse

    def __repr__(self):
        return str(f'value: {self.val}, object: {self.obj}')


class MaxHeap:
    """    one-based indexing    """
    """    only supports values and 2-length tuples    """
    def __init__(self, default=None, track_index=False):
        self.track_index = track_index
        self.index_map = dict()

        if default is None:
            default = []
        if not isinstance(default, list):
            raise TypeError
        if default and isinstance(default[0], tuple):
            if len(default[0]) > 2:
                raise ValueError('tuples are limited to (value, object)')

        self.heap = [0] + default
        if len(self.heap) > 2:
            self.build_heap()

    def __repr__(self):
        return str(self.heap[1:])

    def push(self, element) -> None:
        if self.track_index:
            key = self._get_key(element)
            self.index_map[key] = len(self.heap)

        self.heap.append(element)
        self._sift_up()

    def _sift_up(self, child_i: int = -1) -> None:
        if len(self.heap) < 3:
            return

        if child_i < 1:
            child_i = len(self.heap) - 1
        parent_i = child_i // 2
        while self.heap[child_i] > self.heap[parent_i]:
            self.heap[parent_i], self.heap[child_i] = self.heap[child_i], self.heap[parent_i]

            if self.track_index:
                # todo _update_index_map
                key_p = self._get_key(self.heap[parent_i])
                key_c = self._get_key(self.heap[child_i])
                self.index_map[key_p] = parent_i
                self.index_map[key_c] = child_i

            child_i = parent_i
            parent_i = child_i // 2

            if parent_i < 1:
                break

    def pop(self) -> any:
        if len(self.heap) < 2:
            return None

        if len(self.heap) > 1:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            if self.track_index:
                self.index_map[self.heap[1]] = 1
                self.index_map[self.heap[-1]] = len(self.heap) - 1

        pop_element = self.heap.pop()
        if self.track_index:
            self.index_map.pop(pop_element)
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

            if self.track_index:
                # todo _update_index_map
                key_c = self._get_key(self.heap[child_i])
                key_p = self._get_key(self.heap[parent_i])
                self.index_map[key_c] = child_i
                self.index_map[key_p] = parent_i

            parent_i = child_i
            child_i = parent_i * 2
            if child_i >= len(self.heap):
                break
            right = child_i + 1 if child_i + 1 < len(self.heap) else child_i
            if self.heap[right] > self.heap[child_i]:
                child_i = right

    # pop root and push new key (avoids duplicate balance)
    def replace(self, replace_max_with) -> int:
        if self.track_index:
            raise NotImplementedError

        replaced_elem = self.heap[1]
        self.heap[1] = replace_max_with
        self._sift_down()
        return replaced_elem

    # O(n)
    # https://stackoverflow.com/q/9755721
    def build_heap(self) -> list:
        if self.track_index:
            for i, ele in enumerate(self.heap[1:]):
                key = self._get_key(ele)
                self.index_map[key] = i + 1

        last_parent = (len(self.heap) - 1) // 2
        for i in range(last_parent, 0, -1):
            self._sift_down(i)

        return self.heap[1:]

    def update_element(self, element, new_val) -> None:
        if not self.track_index:
            raise AttributeError

        element_i = self.index_map[element]
        if isinstance(self.heap[element_i], tuple):
            old_val = self.heap[element_i][0]
            self.heap[element_i] = (new_val, element)
        else:
            old_val = self.heap[element_i]
            self.heap[element_i] = new_val

        if new_val > old_val:
            self._sift_up(element_i)
        else:
            self._sift_down(element_i)

    def _update_index_map(self):  # todo
        pass

    @staticmethod
    def _get_key(element):
        if isinstance(element, tuple):
            return element[1]
        return element


class TestMaxHeap(unittest.TestCase):
    # expected, actual
    def test_create_1(self):
        h = MaxHeap()
        expected = []
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_create_2(self):
        h = MaxHeap([0])
        expected = [0]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_create_3(self):
        h = MaxHeap([1, 0])
        expected = [1, 0]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_create_4(self):
        h = MaxHeap([0, 1])
        expected = [1, 0]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_create_5(self):
        h = MaxHeap([0, 1, 2])
        expected = [2, 1, 0]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_create_6(self):
        h = MaxHeap([0, 1, 2, 3, 4, 5, 6, 7])
        expected = [7, 4, 6, 3, 0, 5, 2, 1]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_create_7(self):
        h = MaxHeap([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        expected = [11, 10, 6, 8, 9, 5, 0, 7, 3, 1, 4, 2]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_push_1(self):
        h = MaxHeap([0])
        h.push(1)
        h.push(2)
        expected = [2, 0, 1]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_push_2(self):
        h = MaxHeap([(0, 3)])
        h.push((1, 2))
        h.push((2, 1))
        expected = [(2, 1), (0, 3), (1, 2)]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_pop_1(self):
        h = MaxHeap([8, 6, 1, 3, 5])
        h.pop()
        expected = [6, 5, 1, 3]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_pop_2(self):
        h = MaxHeap([8, 6, 1, 3, 5])
        h.pop()
        h.pop()
        expected = [5, 3, 1]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_pop_3(self):
        h = MaxHeap([6, 5, 1, 3])
        h.pop()
        expected = [5, 3, 1]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_pop_4(self):
        h = MaxHeap([(2, 1), (0, 3), (1, 2)])
        h.pop()
        expected = [(1, 2), (0, 3)]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_push_pop_1(self):
        h = MaxHeap([(0, 3)])
        h.push((1, 2))
        h.push((2, 1))
        h.pop()
        expected = [(1, 2), (0, 3)]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_sift_down_build_heap_1(self):
        h = MaxHeap([5, 3, 1, 8, 6])
        expected = [8, 6, 1, 3, 5]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_track_index_1(self):
        h = MaxHeap([5, 3, 1, 8, 6], True)
        expected = [8, 6, 1, 3, 5]
        expected = {k: i + 1 for i, k in enumerate(expected)}
        actual = h.index_map
        self.assertEqual(expected, actual)

    def test_update_element_1(self):
        h = MaxHeap([5, 3, 1, 8, 6])
        self.assertRaises(AttributeError, h.update_element, element=1, new_val=1)

    def test_update_element_2(self):
        h = MaxHeap([5, 3, 1, 8, 6], True)
        # heap: [8, 6, 1, 3, 5]
        h.update_element(1, 9)
        expected = [9, 6, 8, 3, 5]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_tuple_track_index_1(self):  # todo
        h = MaxHeap([(5, 'y'), (3, 'b'), (1, 99), (8, 'z'), (6, 'a')], True)
        expected = [(8, 'z'), (6, 'a'), (1, 99), (3, 'b'), (5, 'y')]
        expected = {k[1]: i + 1 for i, k in enumerate(expected)}
        actual = h.index_map
        self.assertEqual(expected, actual)

    def test_tuple_size_1(self):  # todo
        pass

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
