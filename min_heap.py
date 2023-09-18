import unittest


class MinHeap:
    """
    One-based indexing. \n
    Includes increase/decrease key functionality. \n
    Works with Dijkstra's Algorithm.
    """

    def __init__(self, to_heapify: list[tuple[int, any]] = None):
        """
        :param to_heapify: A list of tuples: [(value, object), ...]
        """
        # force two-tuples of the form: (value, object)
        self.heap = to_heapify
        self._force_type()  # strict type check

        # O(log n) runtime updates
        # at the cost of O(n) space
        self.id_map = dict()  # obj_id -> heap_index

        # heapify input
        zeroth = (0, False)
        if self.heap:
            self.heap.append(zeroth)
            self._swap(0, -1)
            self.heapify()
        else:
            self.heap = [zeroth]

    def __repr__(self): return str(self.heap[1:])  # exclude 0th index
    def __bool__(self): return False if len(self.heap) < 2 else True  # preserve 0-indexed behavior

    # O(n) time complexity
    def heapify(self) -> None:
        # start at bottommost parent
        # iterate to root, sifting-down
        start = (len(self.heap) - 1) // 2
        for i in range(start, 0, -1):
            self._sift_down(i)

    def push_heap(self, element) -> None:
        self.heap.append(element)  # list append
        self._sift_up(len(self.heap) - 1)

    def pop_heap(self):
        self._swap(1, -1)
        pop_element = self.heap.pop()  # list pop
        self._sift_down(1)
        return pop_element

    def _sift_up(self, from_i) -> None:
        child_i = from_i
        parent_i = child_i // 2
        while parent_i > 0:
            if self._val(child_i) < self._val(parent_i):
                self._swap(child_i, parent_i)
            child_i = parent_i
            parent_i //= 2

    def _sift_down(self, from_i) -> None:
        length = len(self.heap)
        parent_i = from_i
        child_i = (2 * from_i)
        while child_i < length:
            if child_i + 1 < length:
                if self._val(child_i) > self._val(child_i + 1):
                    child_i += 1
            if self.heap[parent_i] < self.heap[child_i]:
                break
            self._swap(parent_i, child_i)
            parent_i = child_i
            child_i *= 2

    # O(log n) time complexity
    def update(self, obj_id, new_val):
        obj_index = self.id_map[obj_id]
        old_val = self.heap[obj_index][0]
        self.heap[obj_index] = (new_val, obj_id)
        # increase or decrease priority
        if new_val < old_val:
            self._sift_up(obj_index)
        else:
            self._sift_down(obj_index)

    # for extensibility
    def _val(self, i):
        val = self.heap[i]
        if type(self.heap[i]) is tuple:
            val = self.heap[i][0]
        return val

    def _swap(self, i1: int, i2: int) -> None:
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]
        self.id_map[self.heap[i1][1]] = i1
        self.id_map[self.heap[i2][1]] = i2

    # force two-tuples of the form: (value, object)
    def _force_type(self):
        heap = self.heap
        if heap is None:
            return
        if type(heap) is not list:
            raise TypeError
        if len(heap) < 1:
            # raise TypeError('An empty list is not a valid element.')
            return
        if type(heap[0]) is not tuple:
            raise TypeError
        if len(heap[0]) != 2:
            raise TypeError
        if type(heap[0][0]) is not int:
            raise TypeError


class MinHeapTests(unittest.TestCase):
    """ expected, actual """
    # todo: more testing
    #       negatives
    #       force correct comp behavior

    """
    errors
    """
    def test_type_error_input_1(self):
        bad_inputs = [tuple(), dict(), set()]
        for bad_input in bad_inputs:
            self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_2(self):
        bad_input = (None,)
        self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_3(self):
        bad_input = (0,)
        self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_4(self):
        bad_input = ((1, 'v2'), )
        self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_5(self):
        bad_input = ((1, 'v2'), (0, 'v1'))
        self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_6(self):
        bad_input = [1, 2, 3]
        self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_7(self):
        bad_input = (1, 2, 3)
        self.assertRaises(TypeError, MinHeap, bad_input)

    def test_type_error_input_8(self):
        bad_input = {1, 2, 3}
        self.assertRaises(TypeError, MinHeap, bad_input)

    """
    valid inputs
    """
    def test_valid_inputs_1(self):
        h = MinHeap()
        expected = []
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_valid_inputs_2(self):
        inp = []
        h = MinHeap(inp)
        expected = []
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_valid_inputs_3(self):
        inp = self._convert([0])
        h = MinHeap(inp)
        expected = [(0, 0)]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_valid_inputs_4(self):
        inp = [(3, 'v2')]
        h = MinHeap(inp)
        expected = [(3, 'v2')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_valid_inputs_5(self):
        inp = [(1_111_111, 'z')]
        h = MinHeap(inp)
        expected = [(1_111_111, 'z')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_valid_inputs_6(self):
        inp = [(-1_111_111, 'b')]
        h = MinHeap(inp)
        expected = [(-1_111_111, 'b')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    """
    correctness
    """
    def test_correctness_1(self):
        inp = self._convert([1, 1, 1, 3, 4, 5, 1])
        h = MinHeap(inp)
        expected = [(1, 1), (1, 2), (1, 6), (4, 4), (5, 5), (3, 3), (1, 0)]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    # pop functionality
    # pop's correct element
    def test_correctness_2(self):
        inp = self._convert([1, 1, 1, 3, 4, 5, 1])
        h = MinHeap(inp)
        h.pop_heap()  # pop'd value has unique id (hence, checked itself)
        expected = [(1, 0), (1, 2), (1, 6), (4, 4), (5, 5), (3, 3)]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_3(self):
        inp = [(1, 'a'), (1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (1, 'g')]
        h = MinHeap(inp)
        expected = [(1, 'b'), (1, 'c'), (1, 'g'), (4, 'e'), (5, 'f'), (3, 'd'), (1, 'a')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    """
    correctness: pop
    """
    def test_correctness_pop_1(self):
        inp = [(1, 'v1'), (1, 'v2')]
        h = MinHeap(inp)
        h.pop_heap()
        expected = [(1, 'v2')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_pop_2(self):
        inp = [(1, 'v1'), (1, 'v2')]
        h = MinHeap(inp)
        h.pop_heap()
        h.pop_heap()
        expected = []
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_pop_3(self):
        inp = [(1, 'a'), (1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (1, 'g')]
        h = MinHeap(inp)
        h.pop_heap()
        expected = [(1, 'a'), (1, 'c'), (1, 'g'), (4, 'e'), (5, 'f'), (3, 'd')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_pop_4(self):
        inp = [(1, 'a'), (1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (1, 'g')]
        h = MinHeap(inp)
        h.pop_heap()
        h.pop_heap()
        expected = [(1, 'c'), (3, 'd'), (1, 'g'), (4, 'e'), (5, 'f')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_pop_5(self):
        inp = [(1, 'a'), (1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (1, 'g')]
        h = MinHeap(inp)
        h.pop_heap()
        h.pop_heap()
        h.pop_heap()
        expected = [(1, 'g'), (3, 'd'), (5, 'f'), (4, 'e')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_pop_6(self):
        inp = [(1, 'a'), (1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (1, 'g')]
        h = MinHeap(inp)
        h.pop_heap()
        h.pop_heap()
        h.pop_heap()
        h.pop_heap()
        expected = [(3, 'd'), (4, 'e'), (5, 'f')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_pop_7(self):
        inp = [(1, 'a'), (1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (1, 'g')]
        h = MinHeap(inp)
        h.pop_heap()
        h.pop_heap()
        h.pop_heap()
        h.pop_heap()
        h.pop_heap()
        expected = [(4, 'e'), (5, 'f')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    """
    correctness: push
    """
    # default argument
    def test_correctness_push_1(self):
        h = MinHeap()
        h.push_heap((1, 'a'))
        expected = [(1, 'a')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_push_2(self):
        inp = []
        h = MinHeap(inp)
        h.push_heap((1, 'a'))
        expected = [(1, 'a')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_push_3(self):
        inp = []
        h = MinHeap(inp)
        h.push_heap((1, 'a'))
        h.push_heap((1, 'b'))
        expected = [(1, 'a'), (1, 'b')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_push_4(self):
        inp = [(1, 'a'), (1, 'b')]
        h = MinHeap(inp)
        h.push_heap((4, 'e'))
        h.push_heap((3, 'd'))
        expected = [(1, 'a'), (1, 'b'), (4, 'e'), (3, 'd')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_push_5(self):
        inp = [(1, 'a'), (1, 'b')]
        h = MinHeap(inp)
        h.push_heap((3, 'd'))
        h.push_heap((4, 'e'))
        expected = [(1, 'a'), (1, 'b'), (3, 'd'), (4, 'e')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_push_6(self):
        inp = []
        h = MinHeap(inp)
        h.push_heap((3, 'a'))
        h.push_heap((1, 'b'))
        expected = [(1, 'b'), (3, 'a')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    def test_correctness_push_7(self):
        inp = [(1, 'b'), (1, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]
        h = MinHeap(inp)
        h.push_heap((99, 'h'))
        expected = [(1, 'b'), (1, 'c'), (4, 'e'), (5, 'f'), (3, 'd'), (99, 'h')]
        actual = h.heap[1:]
        self.assertEqual(expected, actual)

    """
    correctness: bool (truthy/falsy)
    """
    def test_bool_1(self):
        h = MinHeap()
        expected = False
        self.assertEqual(bool(h), expected)

    def test_bool_2(self):
        h = MinHeap([(0, 'a')])
        expected = True
        self.assertEqual(bool(h), expected)

    def test_bool_3(self):
        h = MinHeap([(0, 'a'), (1, 'b')])
        expected = True
        self.assertEqual(bool(h), expected)

    def test_bool_4(self):
        h = MinHeap([(0, 'a'), (1, 'b')])
        h.pop_heap()
        expected = True
        self.assertEqual(bool(h), expected)

    def test_bool_5(self):
        h = MinHeap([(0, 'a'), (1, 'b')])
        h.pop_heap()
        h.pop_heap()
        expected = False
        self.assertEqual(bool(h), expected)

    @staticmethod
    def _convert(inp):
        return [(x, i) for i, x in enumerate(inp)]
