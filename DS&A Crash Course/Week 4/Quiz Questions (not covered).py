from __future__ import annotations

'''
Given a list, create a prefix sum list. 
Example input: [1, 2, 3]
Example output: [1, 3, 6]
'''


def question6(input_list: list[int]) -> list[int]:
    # should mention/cover prefix sum list in curriculum or provide definition
    for i in range(1, len(input_list)):
        input_list[i] += input_list[i - 1]
    return input_list


'''
Given a list, return a list where the element at index i is the product 
of all other elements in the original list except for the element at index i. 
Do this without using the division operator. 

Example input: [1, 2, 3, 4]
Example output: [24, 12, 8, 6]

Hint: Build up left and right prefix product lists. 
For the example input above, your left prefix product list should look like:
[1, 1, 2, 6]

And your right prefix product list should look like: 
[24, 12, 4, 1]
'''


def question7(input_list: list[int]) -> list[int]:
    n = len(input_list)
    left = input_list[:]
    for i in range(1, n):
        left[i] *= left[i - 1]
    print(left)
    right = input_list[:]
    for i in range(n - 2, -1, -1):
        right[i] *= right[i + 1]
    print(right)
    for i in range(n):
        l_el = left[i - 1] if i > 0 else 1
        r_el = right[i + 1] if i < (n - 1) else 1
        input_list[i] = l_el * r_el
    return input_list


# from stencil import *

def test_question6_case1():
    assert question6([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]


def test_question6_case2():
    assert question6([1, -1, 1, -1, 1]) == [1, 0, 1, 0, 1]


def test_question7_case1():
    assert question7([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_question7_case2():
    assert question7([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_question7_case3():
    assert question7([-1, 1, -1, 1, -1]) == [1, -1, 1, -1, 1]


def test_question7_case4():
    assert question7([3, 5]) == [5, 3]
