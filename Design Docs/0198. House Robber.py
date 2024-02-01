from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        two_back = 0
        for val in nums:
            new_max = max(prev_max, two_back + val)
            two_back = prev_max
            prev_max = new_max
        return prev_max
