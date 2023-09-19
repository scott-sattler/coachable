from __future__ import annotations
import heapq
import unittest
from heapq import _siftup  # heapq has up/down inverted

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in 
the methods.
'''


class StreamHandlerKLargest:
    def __init__(self, k: int) -> None:
        self.k = k
        self.heap = list()

    '''
    This method adds the stream element to the collection. 
    You only need to store the k largest elements seen so far at any given point 
    in time.
    '''

    def add_stream_element(self, e: int) -> None:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, e)
            return

        if e > self.heap[0]:
            # heapq.heappop(self.heap)
            # heapq.heappush(e)
            # or
            # heapq.heappushpop(self.heap, e)
            # or
            # heapq.heapreplace(self.heap, e)
            # or
            self.heap[0] = e
            heapq._siftup(self.heap, 0)

    ''' 
    This method returns the k largest elements seen so far.
    '''

    def k_largest(self) -> list[int]:
        return self.heap  # no order specified


'''
Complete the StreamHandlerKSmallest class that has a capacity k by filling in 
the methods.
'''


class StreamHandlerKSmallest:
    def __init__(self, k: int) -> None:
        self.k = k
        self.heap = list()

    '''
    This method adds the stream element to the collection. 
    You only need to store the k smallest elements seen so far at any given point 
    in time.
    '''

    def add_stream_element(self, e: int) -> None:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, -e)
            return

        if e < -(self.heap[0]):
            self.heap[0] = -e
            heapq._siftup(self.heap, 0)

    ''' 
    This method returns the k smallest elements seen so far.
    '''

    def k_smallest(self) -> list[int]:
        return [-i for i in self.heap]


''' 
Write a function that creates a copy of the list, and sorts it in ascending 
order using a heap.
'''


def heapsort(input_list: list[int]) -> list[int]:
    import heapq
    heapq.heapify(input_list)
    heap_sorted = list()

    while input_list:
        heap_sorted.append(heapq.heappop(input_list))

    return heap_sorted


'''
Suppose we have some data that can be expressed as a tuple (a, b, c).

We want to get the top k tuples out of a collection of n total tuples, where 
k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, and the higher 
the score, the greater the datapoint.

Complete the class for this datapoint object, and complete the below function, 
using a heap to do so.
'''


class Datapoint:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def score(self):
        return self.a * 2 + self.b * 5 + self.c * 10

    def __lt__(self, obj):
        if self.score() < obj.score():
            return True
        return False

    def to_tuple(self) -> tuple[int, int, int]:
        return self.a, self.b, self.c


# Return them as tuples, using the to_tuple method in the Datapoint class.
def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
    h = list()

    for point in data_collection:
        if len(h) < k:
            heapq.heappush(h, point)
            continue

        if point > h[0]:
            h[0] = point
            heapq._siftup(h, 0)

    return set(dpoint.to_tuple() for dpoint in h)


class TestHeaps(unittest.TestCase):
    shkl1 = StreamHandlerKLargest(3)

    shkl2 = StreamHandlerKLargest(3)
    shkl2.add_stream_element(5)
    shkl2.add_stream_element(3)

    shkl3 = StreamHandlerKLargest(3)
    shkl3.add_stream_element(5)
    shkl3.add_stream_element(3)
    shkl3.add_stream_element(7)
    shkl3.add_stream_element(9)

    shkl4 = StreamHandlerKLargest(3)
    shkl4.add_stream_element(5)
    shkl4.add_stream_element(7)
    shkl4.add_stream_element(9)
    shkl4.add_stream_element(3)

    shks1 = StreamHandlerKSmallest(3)

    shks2 = StreamHandlerKSmallest(3)
    shks2.add_stream_element(5)
    shks2.add_stream_element(3)

    shks3 = StreamHandlerKSmallest(3)
    shks3.add_stream_element(5)
    shks3.add_stream_element(9)
    shks3.add_stream_element(7)
    shks3.add_stream_element(3)

    shks4 = StreamHandlerKSmallest(3)
    shks4.add_stream_element(3)
    shks4.add_stream_element(5)
    shks4.add_stream_element(7)
    shks4.add_stream_element(9)

    def test_k_largest_1(self):
        assert self.shkl1.k_largest() == []

    def test_k_largest_2(self):
        assert sorted(self.shkl2.k_largest()) == [3, 5]

    def test_k_largest_3(self):
        assert sorted(self.shkl3.k_largest()) == [5, 7, 9]

    def test_k_largest_4(self):
        assert sorted(self.shkl4.k_largest()) == [5, 7, 9]

    def test_k_smallest_1(self):
        assert self.shks1.k_smallest() == []

    def test_k_smallest_2(self):
        assert sorted(self.shks2.k_smallest()) == [3, 5]

    def test_k_smallest_3(self):
        assert sorted(self.shks3.k_smallest()) == [3, 5, 7]

    def test_k_smallest_4(self):
        assert sorted(self.shks4.k_smallest()) == [3, 5, 7]

    def test_heapsort_1(self):
        assert heapsort([9, 6, 2, 11, 15]) == [2, 6, 9, 11, 15]

    def test_get_top_k_datapoints_1(self):
        assert get_top_k_datapoints([Datapoint(1, 2, 3), Datapoint(2, 3, 1), Datapoint(3, 2, 1)], 2) == set(
            [(1, 2, 3), (2, 3, 1)])
