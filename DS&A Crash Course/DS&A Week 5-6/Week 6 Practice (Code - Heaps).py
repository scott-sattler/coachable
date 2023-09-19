from __future__ import annotations


'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''


class StreamHandlerKLargest:
    def __init__(self, k: int) -> None:
        self.k = k
        self.heap = list()

    '''
    This method adds the stream element to the collection. 
    You only need to store the k largest elements seen so far at any given point in time.
    '''

    def add_stream_element(self, e: int) -> None:
        self.heap.append(e)
        self.heapify()

    ''' 
    This method returns the k largest elements seen so far.
    '''

    def k_largest(self) -> list[int]:
        k_largest = list()
        for _ in range(self.k):
            k_largest += self.pop_root()
            self.heapify()
        return k_largest

    # pop
    def pop_root(self):
        if self.heap:
            self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        return self.heap[-1] if len(self.heap) > 0 else []

    # heapify
    def heapify(self):
        pass

'''
Complete the StreamHandlerKSmallest class that has a capacity k by filling in the methods.
'''


class StreamHandlerKSmallest:
    def __init__(self, k: int) -> None:
        self.k = k

    '''
    This method adds the stream element to the collection. 
    You only need to store the k smallest elements seen so far at any given point in time.
    '''

    def add_stream_element(self, e: int) -> None:
        pass

    ''' 
    This method returns the k smallest elements seen so far.
    '''

    def k_smallest(self) -> list[int]:
        return []


''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''


def heapsort(input_list: list[int]) -> list[int]:
    return []


'''
Suppose we have some data that can be expressed as a tuple (a, b, c). 
We want to get the top k tuples out of a collection of n total tuples, 
where k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, 
and the higher the score, the greater the datapoint. 
Complete the class for this datapoint object, and complete the below function, using a heap to do so.
'''


class Datapoint:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.a, self.b, self.c)

    # TODO: you may need to add additional methods here.
    def score(self, data: Datapoint):
        return 2*self.a + 5*self.b + 10*self.c


# Return them as tuples, using the to_tuple method in the Datapoint class.
def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
    return set()


# included testing #

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

def test_k_largest_1():
  assert shkl1.k_largest() == []

def test_k_largest_2():
  assert sorted(shkl2.k_largest()) == [3, 5]

def test_k_largest_3():
  assert sorted(shkl3.k_largest()) == [5, 7, 9]

def test_k_largest_4():
  assert sorted(shkl4.k_largest()) == [5, 7, 9]

def test_k_smallest_1():
  assert shks1.k_smallest() == []

def test_k_smallest_2():
  assert sorted(shks2.k_smallest()) == [3, 5]

def test_k_smallest_3():
  assert sorted(shks3.k_smallest()) == [3, 5, 7]

def test_k_smallest_4():
  assert sorted(shks4.k_smallest()) == [3, 5, 7]

def test_heapsort_1():
  assert heapsort([9, 6, 2, 11, 15]) == [2, 6, 9, 11, 15]

def test_get_top_k_datapoints_1():
  assert get_top_k_datapoints([Datapoint(1,2,3), Datapoint(2,3,1), Datapoint(3,2,1)], 2) == set([(1,2,3), (2,3,1)])


# added calls for testing #

test_k_largest_1()
test_k_largest_2()
test_k_largest_3()
test_k_largest_4()
test_k_smallest_1()
test_k_smallest_2()
test_k_smallest_3()
test_k_smallest_4()
test_heapsort_1()
test_get_top_k_datapoints_1()