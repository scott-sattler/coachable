'''

11
11

100

carry

strings are immutable
-> use a list

b_sum = list()

iterate right to left on both
when 2 or both 1: place 0, carry 1


concurrently iterate over both strings

transpose either binary
then iterate over one, changing existing as necessary

deque: append left
list: O(n + m) for reverse

11
11

001


101
1

011
1

110

from collections import deque
b_sum = deque()
b_sum.appendleft()

list.reverse()


solution:
O(n + m) time
O(max(n, m)) space

100000000000000000000000
100000000000000000000000

'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = list()

        # add binary numbers O(n + m) time
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i > -1 or j > -1 or carry:
            bin_a = 0
            if i >= 0:
                bin_a = int(a[i])

            bin_b = 0
            if j >= 0:
                bin_b = int(b[j])

            total = bin_a + bin_b + carry
            carry = total // 2
            bin_sum.append(str(total % 2))

            i -= 1
            j -= 1

        # reverse list O(n + m) time
        i = 0
        j = len(bin_sum) - 1
        while i < j:
            bin_sum[i], bin_sum[j] = bin_sum[j], bin_sum[i]
            i += 1
            j -= 1

        return ''.join(bin_sum)
