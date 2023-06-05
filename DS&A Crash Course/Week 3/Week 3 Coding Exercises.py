from __future__ import annotations

'''
Return the list of numbers as a string separated by space using recursion
'''


# more performant (perf + clarity ~?= 0); records data within itself via implicit data structure
# O(2n) + O(n^2) -> O(n^2) time (n calls; n .join); O(2n) -> O(n) aux space (n call stack; n implicit structure)
# First Attempt
def recurse_1(lst: list[int | str]) -> str:
    if isinstance(lst[0], str):
        return ' '.join(lst)

    lst.append(str(lst.pop(0)))  # issue: pop() vs (pop(0) O(.5n(n+1)) -> O(n^2))

    return recurse(lst)


# Second Atteempt
# clean; poor performance
def recurse_2(lst: list[int]) -> str:
    if len(lst) == 1:
        return str(lst[0])

    return recurse(lst[0:1]) + ' ' + recurse(lst[1:])


# Third Attempt: implicit data structure
# O(n) time; O(1) aux space
def recurse(lst: list[int | str]) -> str:
    # base case
    if isinstance(lst[0], str):
        lst.pop()
        return ' '.join(lst)

    # create implicit data structure
    if not isinstance(lst[-2], str):
        lst[-1] = str(lst[-1])
        lst.append(-2)

    lst[lst[-1]] = str(lst[lst[-1]])
    lst[-1] -= 1

    return recurse(lst)


# Fourth Attempt
def recurse_4(lst: list[int | str]) -> str:
    # keep return data in outermost fn call
    pass


'''
2. Calculate the factorial of N iteratively and recursively
'''


def fact_iter(n: int) -> int:
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


def fact_recursive(n: int) -> int:
    if n < 2:
        return 1
    return n * fact_recursive(n - 1)


'''
3. Use binary search to find the index of a list that a certain number exists at. 
Return -1 if number does not exist. Assume that the list is sorted.
'''


def find_index(lst: list[int], val: int) -> int:
    lo = 0
    hi = len(lst)

    while hi - lo > 1:
        indx = lo + (hi - lo) // 2

        if lst[indx] == val:
            return indx

        if lst[indx] > val:
            hi = indx
        else:  # go right
            lo = indx

    # todo: refactor/debug for inputs of size 1, 2

    return -1




'''
4. Use binary search to find the index of a list that is the biggest number less than or equal to the given value. 
Return -1 if such a number does not exist. Assume that the list is sorted.
'''


def find_closest(lst: list[int], val: int) -> int:
    pass


# from stencil import *

def test_recurse_1():
    # assert recurse([1, 2, 3]) == "1 2 3 "
    assert recurse([1, 2, 3]) == "1 2 3"


def test_fact_iter_1():
    assert fact_iter(5) == 120


def test_fact_iter_2():
    assert fact_iter(10) == 3628800


def test_fact_recursive_1():
    assert fact_recursive(5) == 120


def test_fact_recursive_2():
    assert fact_recursive(10) == 3628800


def test_find_index_1():
    assert find_index([1, 5, 10, 20, 100], 5) == 1


def test_find_index_2():
    assert find_index([1, 5, 10, 20, 100], 15) == -1


def test_find_closest_1():
    assert find_closest([1, 5, 10, 20, 100], 9) == 1


def test_find_closest_2():
    assert find_closest([1, 5, 10, 20, 100], 21) == 3


def test_find_closest_3():
    assert find_closest([1, 5, 10, 20, 100], 0) == -1
