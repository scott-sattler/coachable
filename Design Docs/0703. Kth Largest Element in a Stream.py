from typing import List
import heapq

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# use a min heap to track the kth largest elements
# heapify input
# continue to add to heap until size k
# at size k, when an incoming element is larger than the min
# we need to push the new element and pop the min


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)

        # for nums input larger than k
        # pop heap until heap is of size k
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # if heap less than size k
        # push element and return min
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
            return self.minheap[0]

        # else, push element if greater than min
        # otherwise, discard and return min
        #     heappushpop() is more efficient
        #     this method replaces the min, and sift-down.
        #     heapq's sift-down (there, sift-up) is protected
        heapq.heappushpop(self.minheap, val)
        return self.minheap[0]
