from typing import List


class Solution:
    # # Timsort implementation in O(n * k log2 k) # #
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

    # # Counting Sort implementation in O(n * k) # #
    # O(n * k) or O(n) time complexity; O(n) auxiliary space complexity
    # where n is the number of words, and k is the average word length
    # O(n * k) if word length, k, is allowed to scale with n, else, O(n)
    # noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedeclaration
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # initialize maps # #
        # for counting sort in O(1)
        cmap = [0] * 26  # replication; list comp. -> [0 for _ in range(26)]
        # for anagram grouping in O(1)
        hmap = dict()

        # iterate over input in O(n)
        for word in strs:
            # # counting sort # #
            # create letter map O(k)
            for let_w in word:
                cmap[ord(let_w) - 97] += 1

            # sorted word formation
            # create a list(word) in O(k)
            sorted_word = list()
            for let_s in cmap:
                sorted_word.append(chr(let_s + 97))
            # cast list to string in O(k)
            sorted_word = ''.join(sorted_word)
            # # end counting sort # #

            # reset letter map O(1)
            cmap = [0] * 26

            # add to hash map in O(1)
            if sorted_word not in hmap:
                hmap[sorted_word] = list()
            hmap[sorted_word].append(word)

        # hash map value retrieval in O(n)
        # cast dict object to list in O(n)
        return list(hmap.values())
