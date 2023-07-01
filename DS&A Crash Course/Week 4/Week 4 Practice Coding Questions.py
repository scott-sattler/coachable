from __future__ import annotations

'''
Reverse a string without the built in function to do so
'''


def reverse_str(s: str) -> str:
    return s[::-1]


'''
Find the most frequent substring of length n in a string.
If there’s a tie, return the alphabetically smallest.
'''


def most_freq_substring(s: str, n: int) -> str:
    freq_map = dict()
    for i in range(n, len(s) + 1):
        substr = s[i - n:i]
        if substr in freq_map:
            freq_map[substr] += 1
        else:
            freq_map[substr] = 0

    return sorted(freq_map.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]


'''
What is the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”.
Time complexity does not need to be optimal.
'''


def smallest_subsequence(s: str, n: int) -> str:
    a_ss = list()  # all subsequences
    _helper_fn(s, n, 0, list(), a_ss)
    a_ss.sort()
    return a_ss[0]


def _helper_fn(text, sub_len, i, sub_str: list, a_ss):
    if i == len(text):
        if len(sub_str) == sub_len:
            a_ss.append(''.join(sub_str))
        return tuple()

    # include
    include = sub_str[:]
    include.append(text[i])
    i += 1

    # include, exclude
    return _helper_fn(text, sub_len, i, include, a_ss), _helper_fn(text, sub_len, i, sub_str, a_ss)


'''
Merge N sorted lists.

Do not just append them all and use .sort()
Think of the merge technique used in mergesort.

Example
Input: [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
Output: [0, 1, 2, 4, 5, 8, 8, 9, 10]
'''


def merge_n_lists(n_lists: list[list[int]]) -> list[int]:
    # min heap of tuple(value, list_index) tuples

    # naive
    # while at least one list has elements:
    # find smallest element
    # append to sorted list

    n_lists_sorted = list()
    while len(n_lists) > 0:
        min_element = float('inf')
        min_index = None
        for i, each_list in enumerate(n_lists):
            if each_list[0] < min_element:
                min_element = each_list[0]
                min_index = i

        # all sorts of bad
        n_lists[min_index].pop(0)
        if len(n_lists[min_index]) < 1:
            del n_lists[min_index]

        n_lists_sorted.append(min_element)

    return n_lists_sorted


''' 
Given a list of coordinates, sort them by increasing order for X values, 
then decreasing order for Y values.
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''


def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(lst, key=lambda xy: (xy[0], -xy[1]))


# from stencil import *

def test_reverse_str_1():
    assert reverse_str("abcd") == "dcba"


def test_reverse_str_2():
    assert reverse_str("abbd") == "dbba"


def test_most_freq_substring_1():
    assert most_freq_substring("abaa", 2) == "aa"


def test_most_freq_substring_2():
    assert most_freq_substring("eabcdeab", 3) == "eab"


# def test_smallest_subsequence_1():
#     assert smallest_subsequence("agbf", 2) == "ab"


def test_smallest_subsequence_2():
    assert smallest_subsequence("batman", 3) == "aan"


def test_smallest_subsequence_3():
    assert smallest_subsequence("zzzab", 3) == "zab"


#
#
# def test_merge_n_lists_1():
#     assert merge_n_lists([[1, 5, 8], [0, 2, 10], [4, 8, 9]]) == [0, 1, 2, 4, 5, 8, 8, 9, 10]
#
#
# def test_merge_n_lists_2():
#     assert merge_n_lists([[1, 3], [2, 4]]) == [1, 2, 3, 4]
#
#
# def test_merge_n_lists_3():
#     assert merge_n_lists([[1, 3], [4, 6]]) == [1, 3, 4, 6]
#
#
# def test_merge_n_lists_4():
#     assert merge_n_lists([[4, 6], [1, 3]]) == [1, 3, 4, 6]
#
#
# def test_merge_n_lists_5():
#     assert merge_n_lists([[1, 3, 5]]) == [1, 3, 5]


def test_sort_tuples_1():
    assert sort_tuples([(1, 1), (2, 2), (2, 1), (1, 2)]) == [(1, 2), (1, 1), (2, 2), (2, 1)]


def test_sort_tuples_2():
    assert sort_tuples([(2, 10), (1, 10), (3, 10)]) == [(1, 10), (2, 10), (3, 10)]


def test_sort_tuples_3():
    assert sort_tuples([(10, 2), (10, 1), (10, 3)]) == [(10, 3), (10, 2), (10, 1)]


def test_smallest_subsequence_3():
    assert smallest_subsequence("zzzaab", 3) == "aab"
