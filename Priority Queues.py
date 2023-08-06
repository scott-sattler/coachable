from queue import PriorityQueue

print('>> existing implementation:')

pq = PriorityQueue()
pq.put((1, 'h'))
pq.put((0, 'n'))
pq.put((4, 'o'))
pq.put((3, 'x'))
print(pq)
print(pq.get())
print(pq)
print(pq.get())
print(pq)
print(pq.get())
print(pq)
print(pq.get())
print(pq, '\n')


class _PriorityQueue(PriorityQueue):
    ''' https://github.com/python/cpython/blob/main/Lib/queue.py '''  # noqa

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return str(self.queue)


print('>> readable representation:')

# note: this is NOT a sorted list
pq = _PriorityQueue()
pq.put((1, 'h'))
pq.put((0, 'n'))
pq.put((4, 'o'))
pq.put((3, 'x'))
print(pq)
print(pq.get())
print(pq)
print(pq.get())
print(pq)
print(pq.get())
print(pq)
print(pq.get())
print(pq, '\n')


########################################################################################################################

import heapq  # noqa


heap = list()
heapq.heappush(heap, (1, 'h'))
heapq.heappush(heap, (0, 'n'))
heapq.heappush(heap, (4, 'o'))
heapq.heappush(heap, (3, 'x'))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)
