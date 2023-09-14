import unittest


class MaxHeap:
    """
    one-based indexing. \n
    tuples are limited to (value, object)
    """
    def __init__(self, heapify_list=None, track_index=False):
        """
        :param heapify_list: strictly (value, object)
        :param track_index: used for, e.g. Dijkstra's
        """
        self.track_index = track_index
        self.index_map = dict()

        if heapify_list is None:
            heapify_list = []
        if not isinstance(heapify_list, list):
            raise TypeError
        if heapify_list and isinstance(heapify_list[0], tuple):
            if len(heapify_list[0]) > 2:
                raise ValueError('tuples are limited to (value, object)')

        self.heap = [0] + heapify_list
        if len(self.heap) > 2:
            self.build_heap()

    def __repr__(self):
        return str(self.heap[1:])

    def __bool__(self):
        if len(self.heap) < 2:
            return False
        return True

    def push(self, element: int | tuple) -> None:
        self.heap.append(element)

        if self.track_index:
            self._update_index_map(-1)

        self._sift_up()

    def _sift_up(self, child_i: int | None = None) -> None:
        if len(self.heap) < 3:
            return

        # default operation assumes appended to list
        if child_i is None:
            child_i = len(self.heap) - 1
        parent_i = child_i // 2

        while parent_i > 0 and self.heap[child_i] > self.heap[parent_i]:
            self.heap[parent_i], self.heap[child_i] = self.heap[child_i], self.heap[parent_i]

            if self.track_index:
                self._update_index_map(child_i)
                self._update_index_map(parent_i)

            child_i = parent_i
            parent_i = child_i // 2

    def pop(self) -> tuple[int, object]:
        if len(self.heap) < 2:
            raise IndexError("Cannot remove element from empty heap.")

        if len(self.heap) > 1:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]

            if self.track_index:
                self._update_index_map(1)
                # self._update_index_map(-1)

        # remove from heap and index mapper
        pop_element = self.heap.pop()  # list.pop()
        if self.track_index:
            if isinstance(pop_element, tuple):
                pop_element = pop_element[1]
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
                self._update_index_map(child_i)
                self._update_index_map(parent_i)

            parent_i = child_i
            child_i = parent_i * 2
            if child_i >= len(self.heap):
                break
            right = child_i + 1 if child_i + 1 < len(self.heap) else child_i
            if self.heap[right] > self.heap[child_i]:
                child_i = right

    # pop root and push new key (avoids duplicate balance)
    def replace(self, replace_max_with: int | tuple) -> int:
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
                self._update_index_map(i + 1)

        last_parent = (len(self.heap) - 1) // 2
        for i in range(last_parent, 0, -1):
            self._sift_down(i)

        return self.heap[1:]

    def update_element(self, element: int | tuple, new_val: int | tuple) -> None:
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

    def _update_index_map(self, heap_index: int) -> None:
        element = self.heap[heap_index]
        if isinstance(element, tuple):
            element = element[1]
        self.index_map[element] = heap_index


class TestMaxHeap(unittest.TestCase):
    # expected, actual
    # mixed types? [3, (2, 'a'), 5]

    def test_error_create_1(self):
        self.assertRaises(TypeError, MaxHeap, (1, 2, 3))

    def test_error_create_2(self):
        self.assertRaises(TypeError, MaxHeap, {1, 2, 3})

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

    def test_tuple_track_index_1(self):
        h = MaxHeap([(5, 'y'), (3, 'b'), (1, 99), (8, 'z'), (6, 'a')], True)
        expected = [(8, 'z'), (6, 'a'), (1, 99), (3, 'b'), (5, 'y')]
        expected = {k[1]: i + 1 for i, k in enumerate(expected)}
        actual = h.index_map
        self.assertEqual(expected, actual)

    def test_tuple_size_1(self):
        self.assertRaises(ValueError, MaxHeap, [(3, 4, 5)])

    def test_tuple_size_2(self):
        self.assertRaises(ValueError, MaxHeap, [(3, 'a', [1, 2])])

    def test_tuple_size_3(self):
        h = MaxHeap([(3, [1, 2])])
        expected = [(3, [1, 2])]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_bool_1(self):
        h = MaxHeap()
        expected = False
        self.assertEqual(bool(h), expected)

    def test_bool_2(self):
        h = MaxHeap([0])
        expected = True
        self.assertEqual(bool(h), expected)

    def test_bool_3(self):
        h = MaxHeap([0, 1])
        expected = True
        self.assertEqual(bool(h), expected)

    def test_bool_4(self):
        h = MaxHeap([0, 1])
        h.pop()
        expected = True
        self.assertEqual(bool(h), expected)

    def test_bool_5(self):
        h = MaxHeap([0, 1])
        h.pop()
        h.pop()
        expected = False
        self.assertEqual(bool(h), expected)

    def test_error_empty_pop_1(self):
        h = MaxHeap()
        self.assertRaises(IndexError, h.pop)

    def test_error_empty_pop_2(self):
        h = MaxHeap([2])
        h.pop()
        self.assertRaises(IndexError, h.pop)


