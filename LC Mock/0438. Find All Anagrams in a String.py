'''

hash maps
arrays
prime factors
bit - manipulation

"abc"
"cbaebabacd"
       ^
         ^
0, 6

sliding window/two pointers O(n + m)?
verification: alphabet_size * n


"abc"
"cbaebabacd"

   a
aaaa


abc
zzzabcabcabcabcabc

30_000


abc

01 00 00
00 02 00
00 00 03

010203


aaaaaa
aaaaaaaaaaaaaaaaaaa


time: O(n * a)
where
    a is the size of the alphabet
space: O(n + m)

'''


class Solution:

    def _compare(self, map1, map2) -> bool:
        if len(map1) != len(map2):
            return False
        for k in map1:
            if not k in map2:
                return False
            if map1[k] != map2[k]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = list()
        if len(s) < len(p):
            return anagrams

        # create freq map of p
        pmap = dict()
        for c in p:
            if not c in pmap:
                pmap[c] = 0
            pmap[c] += 1

        # craete freq map of first
        # p characters in s
        smap = dict()
        for c in s[:len(p)]:
            if not c in smap:
                smap[c] = 0
            smap[c] += 1

        # sliding window
        i = 0
        j = len(p) - 1
        while True:
            # compare freq maps
            if self._compare(pmap, smap):
                anagrams.append(i)

            # increment window
            i += 1
            if smap[s[i - 1]] == 1:
                del smap[s[i - 1]]
            else:
                smap[s[i - 1]] -= 1

            j += 1
            if j == len(s):
                break
            if not s[j] in smap:
                smap[s[j]] = 0
            smap[s[j]] += 1

        return anagrams
