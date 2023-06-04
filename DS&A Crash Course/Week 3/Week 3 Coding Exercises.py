from __future__ import annotations

'''
Return the list of numbers as a string separated by space using recursion
'''


# more performant (perf + clarity ~?= 0); records data within itself via implicit data structure
# O(2n) + O(n^2) -> O(n^2) time (n calls; n .join); O(2n) -> O(n) aux space (n call stack; n implicit structure)
# First Attempt
# not able to easily resolve pop() vs pop(0)
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


# Third Attempt
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
def recurse(lst: list[int | str]) -> str:
    # keep return data in outermost fn call
    pass


x = recurse([1, 2, 3, 4, 5])
print(repr(x))

'''
2. Calculate the factorial of N iteratively and recursively
'''


def fact_iter(n: int) -> int:
    pass


def fact_recursive(n: int) -> int:
    pass


'''
3. Use binary search to find the index of a list that a certain number exists at. 
Return -1 if number does not exist. Assume that the list is sorted.
'''


def find_index(lst: list[int], val: int) -> int:
    pass


'''
4. Use binary search to find the index of a list that is the biggest number less than or equal to the given value. 
Return -1 if such a number does not exist. Assume that the list is sorted.
'''


def find_closest(lst: list[int], val: int) -> int:
    pass
