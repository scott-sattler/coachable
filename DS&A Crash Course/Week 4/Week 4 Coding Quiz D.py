from __future__ import annotations

'''
Compute all sliding window sums of size k for the input list. 
1 <= k <= length of input list. Return the result as a list.

Example input 1: input_list = [1, 2, 3, 4, 5], k = 3
Example output 1: [6, 9, 12]

Example input 2: input_list = [1, 2, 3, 4, 5], k = 2
Example output 2: [3, 5, 7, 9]
'''


def question8(input_list: list[int], k: int) -> list[int]:
    inp = input_list
    n = len(inp)
    win = [0] * (n - k + 1)

    for i in range(0, len(win)):
        for j in range(i, i + k):
            win[i] += inp[j]

    return win


# from stencil import *

def test_question8_case1():
    assert question8([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]


def test_question8_case2():
    assert question8([1, 2, 3, 4, 5], 2) == [3, 5, 7, 9]


def test_question8_case3():
    assert question8([1, 2, 3, 4, 5], 3) == [6, 9, 12]


def test_question8_case4():
    assert question8([1, 2, 3, 4, 5], 4) == [10, 14]


def test_question8_case5():
    assert question8([1, 2, 3, 4, 5], 5) == [15]
