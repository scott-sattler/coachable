from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def maxArea(self, height: List[int]) -> int:
        # two pointer solution:
        # starting with the pointers in positions that
        # can produce the largest possible area (0, n-1),
        # we have found the maximum area of the shorter
        # height. we therefore repeatedly increment,
        # inward, the shorter of the two pointers.

        # initialize pointers and max store
        p1 = 0
        p2 = len(height) - 1
        max_area = float('-inf')

        # iterate until p1 and p2 collide
        while p1 < p2:
            width = p2 - p1
            lower_height = height[p1]
            # bound by the lesser height of p1
            if height[p1] < height[p2]:
                p1 += 1
            # bound by p2
            elif height[p1] > height[p2]:
                lower_height = height[p2]
                p2 -= 1
            # maximum of both p1 and p2 found
            else:  # height[p1] == height[p2]
                p1 += 1
                p2 -= 1
            # update if new area is larger
            max_area = max(max_area, lower_height * width)

        return max_area
