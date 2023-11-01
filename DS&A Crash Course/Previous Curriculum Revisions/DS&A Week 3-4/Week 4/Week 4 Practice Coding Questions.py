from __future__ import annotations

'''
Reverse a string without the built in function to do so
'''


# time complexity: O(n)
# space complexity: O(n)
def reverse_str(s: str) -> str:
    s_reversed = ''
    for i in range(len(s) - 1, -1, -1):
        s_reversed += s[i]
    return s_reversed  # or return s[::-1]


'''
Find the most frequent substring of length n in a string. If there’s a tie, return the alphabetically smallest.
'''


# time/space: O(n)/O(n)
def most_freq_substring(s: str, n: int) -> str:
    frequency_map = dict()
    max_l_k = [0, '']
    for i in range(len(s) - n + 1):
        next_substring = s[i:i + n]
        if next_substring in frequency_map:
            frequency_map[next_substring] += 1
        else:
            frequency_map[next_substring] = 1

        curr_sub_count = frequency_map[next_substring]
        max_len = max_l_k[0]
        if curr_sub_count >= max_len:
            new_max = [curr_sub_count, next_substring]
            # ties broken alpha
            if curr_sub_count == max_len:
                max_l_k = sorted([new_max, max_l_k], key=lambda x: x[1])[0]
            else:
                max_l_k = new_max

    return max_l_k[1]


'''
What is the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''


def smallest_subsequence(s: str, n: int) -> str:
    # instructions != test cases
    # return ''.join(sorted(list(s))[0:n])
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            while len(stack) > 0 and stack[-1] > char:
                stack.pop()
            stack.append(char)

    return ''.join(stack[0:n])


'''
Sort N sorted lists
Example
Input: [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
Output: [0, 1, 2, 4, 5, 8, 8, 9, 10]
'''


# time/space O(k)/O(k) where k is total elements
def sort_n_lists(lst: list[list[int]]) -> list[int]:
    lst_sorted = []
    while lst:
        max = float('-inf')
        index = 0
        for i, each_lst in enumerate(lst):
            if each_lst[-1] > max:
                max = each_lst[-1]
                index = i
        else:
            next_num = lst[index].pop()
            lst_sorted.append(next_num)
            if len(lst[index]) == 0:
                del lst[index]
    return lst_sorted[::-1]


''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''


def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(lst, key=lambda x: (x[0], -x[1]))


# from stencil import *

def test_reverse_str_1():
    assert reverse_str("abcd") == "dcba"


def test_reverse_str_2():
    assert reverse_str("abbd") == "dbba"


def test_most_freq_substring_1():
    assert most_freq_substring("abaa", 2) == "aa"


def test_most_freq_substring_2():
    assert most_freq_substring("eabcdeab", 3) == "eab"


def test_smallest_subsequence_1():
    assert smallest_subsequence("agbf", 2) == "ab"


def test_smallest_subsequence_2():
    assert smallest_subsequence("batman", 3) == "aan"


def test_sort_n_lists_1():
    assert sort_n_lists([[1, 5, 8], [0, 2, 10], [4, 8, 9]]) == [0, 1, 2, 4, 5, 8, 8, 9, 10]


def test_sort_n_lists_2():
    assert sort_n_lists([[1, 3], [2, 4]]) == [1, 2, 3, 4]


def test_sort_n_lists_3():
    assert sort_n_lists([[1, 3], [4, 6]]) == [1, 3, 4, 6]


def test_sort_n_lists_4():
    assert sort_n_lists([[4, 6], [1, 3]]) == [1, 3, 4, 6]


def test_sort_n_lists_5():
    assert sort_n_lists([[1, 3, 5]]) == [1, 3, 5]


def test_sort_tuples_1():
    assert sort_tuples([(1, 1), (2, 2), (2, 1), (1, 2)]) == [(1, 2), (1, 1), (2, 2), (2, 1)]


def test_sort_tuples_2():
    assert sort_tuples([(2, 10), (1, 10), (3, 10)]) == [(1, 10), (2, 10), (3, 10)]


def test_sort_tuples_3():
    assert sort_tuples([(10, 2), (10, 1), (10, 3)]) == [(10, 3), (10, 2), (10, 1)]


# tests

test_reverse_str_1()
test_reverse_str_2()
test_most_freq_substring_1()
test_most_freq_substring_2()
test_smallest_subsequence_1()
test_smallest_subsequence_2()
test_sort_n_lists_1()
test_sort_n_lists_2()
test_sort_n_lists_3()
test_sort_n_lists_4()
test_sort_n_lists_5()
test_sort_tuples_1()
test_sort_tuples_2()
test_sort_tuples_3()
