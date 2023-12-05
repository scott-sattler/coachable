from typing import List


class Solution:
    # noinspection PyPep8Naming, PyMethodMayBeStatic
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = {0: 1}  # prefix sum

        sum_ = 0
        for num in nums:
            sum_ += num

            # count target matches
            if sum_ - k in prefix:
                count += prefix[sum_ - k]

            # hash running total
            if sum_ not in prefix:
                prefix[sum_] = 0
            prefix[sum_] += 1

        return count
