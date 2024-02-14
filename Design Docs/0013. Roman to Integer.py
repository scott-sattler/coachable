class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def romanToInt(self, s: str) -> int:
        val_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            curr = val_map[s[i]]
            # bounds check; subtract if increasing
            if i + 1 < len(s) and val_map[s[i + 1]] > curr:
                curr *= -1
            total += curr
        return total

    # def romanToInt(self, s: str) -> int:
    #     val_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     total = 0
    #     for i in range(len(s)):
    #         curr = val_map[s[i]]
    #         # bounds check
    #         if i + 1 < len(s):
    #             # subtract if increasing
    #             if val_map[s[i + 1]] > curr:
    #                 curr *= -1
    #         total += curr
    #     return total

    # def romanToInt(self, s: str) -> int:
    #     val_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     total = 0
    #     for i in range(len(s) - 1):
    #         curr = val_map[s[i]]
    #         # subtract if increasing
    #         if val_map[s[i + 1]] > curr:
    #             curr *= -1
    #         total += curr
    #     else:
    #         total += val_map[s[-1]]
    #     return total
