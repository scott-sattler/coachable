from typing import List


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    # O(n * k log2 k) time; O(n) auxiliary space
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group via hash map
        hmap = dict()

        # iterate over input
        for string in strs:
            # produce unique hash ID
            # list(str) -> sort(list) -> str(list) -> hash(str)
            # in O(3k log2 k) -> O(k log2 k)
            # note: str -> list -> str O(2k)
            anagram_id = ''.join(sorted(string))
            if anagram_id not in hmap:
                hmap[anagram_id] = list()
            hmap[anagram_id].append(string)

        # return list of anagrams grouped in lists
        return list(hmap.values())
