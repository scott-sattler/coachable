class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def isHappy(self, n: int) -> bool:
        # return sum of each digit squared
        def _happy(k) -> int:
            sum_ = 0
            while k > 0:
                sum_ += (k % 10) ** 2
                k //= 10
            return sum_

        # # visited set
        # visited = set()
        # while n not in visited:
        #     visited.add(n)
        #     n = _happy(n)
        # fast = n

        # Floyd's Cycle Detection
        slow = n
        fast = _happy(n)
        while slow != fast:
            slow = _happy(slow)
            fast = _happy(_happy(fast))

        return fast == 1
