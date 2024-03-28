'''
time:
n + n + n * log2 n

[x1, ,x1, ,x1, ,x2, ,x2]

O(n)

bucket sort
choose buck, exhaust bucket
must first choose largest bucket (edge case)

invalid if twice maximum count
is ever larger than length s


aaaabb
aababa
size 6

aaabb
ababa
size 5

2*(count - 1)

aaaabbb
size 7

aaa
2

[a, ... , a]

x, a ... a, x

3 1
5 2
6 3

aaab
4

aa
2

'''


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) < 2:
            return s

        # bucket sort O(n)
        bucket = dict()
        for c in s:
            if not c in bucket:
                bucket[c] = 0
            bucket[c] += 1

        # validate and store max c O(n)
        max_c = c
        for c in bucket:
            if bucket[c] > bucket[max_c]:
                max_c = c
        if 2 * (bucket[max_c] - 1) >= len(s):
            return ""

        # create valid arrangement O(2n)
        valid = [None] * len(s)
        i = 0
        # place largest count (edge case)
        while bucket[max_c] > 0:
            valid[i] = max_c
            bucket[max_c] -= 1
            i += 2
        # place remaining in any order
        for c in bucket:
            while bucket[c] > 0:
                if i >= len(s):
                    i = 1

                valid[i] = c

                bucket[c] -= 1
                i += 2

        return ''.join(valid)  # O(n)
