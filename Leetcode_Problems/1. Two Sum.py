"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""


class Solution:
    # brute force
    # time-complexity: O(n2)
    # space-complexity: O(1)
    def twoSum(self, nums: list[int], target: int) -> list[int]:  # noqa: naming convention
        n = len(nums) - 1
        for i in range(n):
            for j in range(n - i):
                j += i + 1
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

    # time-complexity: O(2n -> n)?
    # space-complexity: O(1)
    def twoSum(self, nums: list[int], target: int) -> list[int]:  # noqa: naming convention
        n = len(nums)
        hash_table = {}
        for i in range(n):
            key = nums[i]
            value = hash_table.get(key)
            if value is None:
                hash_table[key] = i
            elif nums[value] + key == target:
                return [i, hash_table[key]]
        for i in range(n):
            a = nums[i]
            b = target - a
            j = hash_table.get(b)
            if j is not None and i != j:
                return [i, j]


test_0 = [[2, 7, 11, 15], 9]
test_1 = [[2, 5, 5, 11], 10]
test_2 = [[-1, -2, -3, -4, -5], -8]

print(Solution().twoSum(test_0[0], test_0[1]))
print(Solution().twoSum(test_1[0], test_1[1]))
print(Solution().twoSum(test_2[0], test_2[1]))
