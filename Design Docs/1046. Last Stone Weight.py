from typing import List


class Solution:
    # time O(n log n); space O(1)
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq  # min heap

        # invert value for min heap in O(n)
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # use data structure that can efficiently
        # repeatedly find the maximum value in O(log n)
        heapq.heapify(stones)

        # while we have at least two stones
        # smash and add non-zero results in O(n log n)
        while len(stones) > 1:
            # stone_1 = -heapq.heappop(stones)
            # stone_2 = -heapq.heappop(stones)
            # diff = stone_1 - stone_2
            # if diff > 0:
            #     heapq.heappush(stones, -diff)

            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            # negative_difference <= larger_negative - smaller_negative
            neg_diff = stone_1 - stone_2
            if neg_diff < 0:
                heapq.heappush(stones, neg_diff)

        # return the remaining stone, or zero otherwise
        return -stones[0] if len(stones) > 0 else 0
