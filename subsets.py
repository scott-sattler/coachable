
# def subsets(n):
#     if n == 0:
#         return 1
#     index, size = 0, 0
#     return _subsets(index, size, n - 1) + _subsets(index, size + 1, n - 1)
#
#
# def _subsets(index, size, n):
#     if index == n:
#         return 1
#     # print(size)
#     return _subsets(index + 1, size + 1, n) + _subsets(index + 1, size, n)
#
# for i in range(4):
#     print(subsets(i))
#
#
# def subsets(n):
#     if n == 0:
#         return 1, []
#     index = 0
#     subsets = []
#     # return _subsets(1, [], n - 1, subsets) + _subsets(1, [0], n - 1, subsets)
#     _subsets(1, [0], n, subsets) + _subsets(1, [], n, subsets)
#     return len(subsets), subsets
#
#
# def _subsets(index, par_set, n, subsets):
#     if index == n:
#         subsets.append(par_set)
#         print(par_set)
#         return 1
#     return _subsets(index + 1, par_set + [index], n, subsets) + _subsets(index + 1, par_set, n, subsets)
#
#
# for i in range(7):
#     print(subsets(i))
#
# print(subsets(3))

# []
# [] [1]
# [] [1] [2] [1 2]


# nonconsecutive recursive
# proper notation
# while this tracks the sets themselves, cardinality does not require the sets themselves
def nc_subsets(n):
    if n < 1:
        return n, 1, {}
    subsets = []
    _subsets(3, [1], n, subsets) + _subsets(2, [], n, subsets)
    count = len(subsets)
    subsets = ''.join(['{' if i == '[' else '}' if i == ']' else i for i in str(subsets)])  # otherwise use frozensets
    return n, count, subsets


def _subsets(index, par_set, n, subsets):
    if index > n:
        subsets.append(par_set)
        return 1
    return _subsets(index + 2, par_set + [index], n, subsets) + _subsets(index + 1, par_set, n, subsets)


# nonconsecutive iterative
# list notation (no proper notation)
def iter_sets(n):
    elements = [i for i in range(1, n + 1)]
    sets = []
    agenda = [[]]  # seed
    while agenda:
        next_elem = agenda.pop(0)
        if next_elem not in sets:
            sets.append(next_elem)  # not included
        for elem in elements:  # included
            next_set = next_elem + [elem]
            if len(next_elem) < 1 or elem > next_elem[-1] + 1:
                sets.append(next_set)
                agenda.append(next_set)
    return n, len(sets), sets  # list notation tho


print(iter_sets(6))

# for i in range(7):
#     print(subsets(i))

print(nc_subsets(6))
# print(nc_subsets(0))
