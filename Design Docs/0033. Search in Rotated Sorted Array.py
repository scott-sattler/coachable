from typing import List

# 1 2 3 4 5 6  array
# 4 5 6 1 2 3  rotated array
#       ^

# 4 5 1 2 3

# O(n) -> O(log n)


class Solution:
    # (1) find index of rotation
    # (2) find the value (or absence)

    # noinspection PyMethodMayBeStatic
    def search(self, nums: List[int], target: int) -> int:
        # (1) find index of rotation
        lo = 0
        hi = len(nums) - 1
        mid = lo + (hi - lo) // 2
        # repeatedly look in decreasing
        # direction of bisected array
        while lo + 1 < hi:
            # left decreasing
            if nums[lo] > nums[mid]:
                hi = mid
            else:  # right decreasing
                lo = mid
            mid = lo + (hi - lo) // 2

        rot_index = hi

        # (2) find the value (or absence)
        # reset values
        lo = 0
        hi = len(nums) - 1

        # find subarray to binary search into
        # note that subarrays are increasing
        if target < nums[0]:
            lo = rot_index
        else:
            hi = rot_index

        # binary search subarray
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            # if value less than mid, look left
            if target < nums[mid]:
                hi = mid - 1
            # if value greater than mid, look right
            else:  # target > nums[mid]
                lo = mid + 1

        # since lo == hi at this point, return lo or hi
        # if this index is equal to target
        return lo if nums[lo] == target else -1
