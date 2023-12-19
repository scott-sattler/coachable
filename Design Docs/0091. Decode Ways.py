class Solution:
    # top down dp
    # noinspection SpellCheckingInspection
    def numDecodings(self, s: str) -> int:
        memo = dict()
        return self._dp(s, memo, 0)

    def _dp(self, s: str, memo: dict, i: int) -> int:
        # valid mapping found
        if i >= len(s):
            return 1

        if i in memo:
            return memo[i]

        count = 0

        # if digit is not 0
        if s[i] != '0':
            count += self._dp(s, memo, i + 1)

        # if in-bounds and valid value
        if i + 1 < len(s) and 27 > int(s[i:i + 2]) > 9:
            count += self._dp(s, memo, i + 2)

        memo[i] = count
        return count
