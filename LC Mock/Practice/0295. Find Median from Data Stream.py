###############################################################################
# improved solution
# O(log2 n) push; O(1) find

import heapq

class MedianFinder(object):

    def __init__(self):
        self.left = list()  # max heap
        self.right = list()  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # always push left
        heappush(self.left, -num)

        # size(left) too large
        if len(self.left) > len(self.right):
            heappush(self.right, -heappop(self.left))

        # left root is larger than right root
        # heap swap left root and right root
        if self.left and -self.left[0] > self.right[0]:
            heappush(self.right, -heappop(self.left))
            heappush(self.left, -heappop(self.right))


    def findMedian(self):
        """
        :rtype: float
        """
        # heaps are either balanced
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2.0
        # or the right is larger
        return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


###############################################################################
# live solution
# O(log2 n) push; O(1) find

import heapq


class MedianFinder(object):

    def __init__(self):
        self.left = list()  # max heap
        self.right = list()  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.left, -num)

        # size(left) too large
        if len(self.left) - len(self.right) > 1:
            transfer = -heapq.heappop(self.left)
            heapq.heappush(self.right, transfer)

        # empty: (both) or (one heap)
        if not self.left or not self.right:
            return

        # left root is larger than right root
        if -self.left[0] > self.right[0]:
            transfer = -heapq.heappop(self.left)
            heapq.heappush(self.right, transfer)

        # size(right) too large
        if len(self.right) - len(self.left) > 1:
            transfer = -heapq.heappop(self.right)
            heapq.heappush(self.left, transfer)

    def findMedian(self):
        """
        :rtype: float
        """
        # return left when left larger
        if len(self.left) > len(self.right):
            return -self.left[0]

        # return right when right larger
        if len(self.left) < len(self.right):
            return self.right[0]

        # return mean when equal
        return (-self.left[0] + self.right[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
