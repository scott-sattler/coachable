from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        # impose order; shorten name
        # (already O(n) space from sort)
        inter = sorted(intervals)

        # from left = 0, right = 1
        # if overlapping: update larger left upper; right++;
        # else: left++; left <-> right; right++;
        left, right = 0, 1
        while right < len(inter):
            if inter[left][1] >= inter[right][0]:
                if inter[right][1] > inter[left][1]:
                    inter[left][1] = inter[right][1]
                right += 1
            else:
                left += 1
                inter[left] = inter[right]  # could swap
                right += 1

        # pop until reaching left pointer
        while len(inter) > left + 1:
            inter.pop()

        return inter




# increment right pointer until no 'overlap'
# [[1,4],[4,5],[5,6],[7,8]]
#    ^     ^
# [[1,5],None,[5,6],[7,8]]
#    ^          ^
# [[1,6],None,None,[7,8]]
#    ^               ^

# increment left pointer, swapping with right
# [[1,6],None,None,[7,8]]
#          ^         ^
# [[1,6],[7,8],None,[7,8]]
#          ^         ^

# pop until reaching left pointer
# [[1,6],[7,8],None]
#          ^
# [[1,6],[7,8]]
#          ^


# detail
# [[1,4],[5,6],[5,6],[7,8]]
#    ^     ^

# [[1,4],[5,6],[5,6],[7,8]]
#          ^^
