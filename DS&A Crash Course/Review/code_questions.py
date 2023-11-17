def quicksort(arr, in_place=True):
    _quicksort(0, len(arr) - 1, arr)
    return None if in_place else arr


def _quicksort(lo, hi, arr):
    if lo >= hi:
        return

    # get pivot
    pivot = _pivot(lo, hi, arr)
    # recurse left
    _quicksort(lo, pivot - 1, arr)
    # recurse right
    _quicksort(pivot + 1, hi, arr)

    return None


# leftmost
def _pivot(lo, hi, arr):
    swap_i = lo + 1
    for i in range(lo + 1, hi + 1):
        if arr[i] < arr[lo]:
            arr[i], arr[swap_i] = arr[swap_i], arr[i]
            swap_i += 1
    arr[swap_i - 1], arr[lo] = arr[lo], arr[swap_i - 1]
    return swap_i - 1


def max_depth(node):
    if not node:
        return 0
    # rr f(n) = max(f(left) + f(right)) + 1
    return max(max_depth(node.left), max_depth(node.right)) + 1


def max_sum_non_adjacent(arr):
    pass


def lca(node):
    pass


def valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not min_val < node.val < max_val:
        return False
    return valid_bst(node.left, min_val, node.val) and valid_bst(node.right, node.val, max_val)


# k = [5, 6, 1, 2, 3, 4]
def rotated_sorted(arr, k):
    return None


def one_apart(str1, str2):
    # try dp and iterative

    # missing character
    # extra character
    return None


tests = [
    # (expected, input)
    (True, {'str1': 'cat', 'str2': 'cats'}),
    (True, {'str1': 'cat', 'str2': 'cut'}),
    (True, {'str1': 'cat', 'str2': 'cats'}),
    (True, {'str1': 'cat', 'str2': 'at'}),
    (False, {'str1': 'cats', 'str2': 'at'}),

    (False, {'str1': 'aaa', 'str2': 'a'}),
    (False, {'str1': 'a', 'str2': 'aaa'}),
    (False, {'str1': 'a', 'str2': 'b'}),

    (False, {'str1': 'ab', 'str2': 'bc'}),
    (False, {'str1': 'bc', 'str2': 'ab'}),
    (True, {'str1': 'aa', 'str2': 'ab'}),
    (True, {'str1': 'ab', 'str2': 'aa'}),

]

for test in tests:
    expected = test[0]
    actual = one_apart(test[1]['str1'], test[1]['str2'])
    print(f"expected: {expected}, actual: {actual}    ||    {test}")



'''
def isOneEditDistance(s: str, t: str) -> bool:
    ns, nt = len(s), len(t)

    # Ensure that s is shorter than t.
    if ns > nt:
        return isOneEditDistance(t, s)

    # The strings are NOT one edit away distance  
    # if the length diff is more than 1.
    if nt - ns > 1:
        return False

    for i in range(ns):
        if s[i] != t[i]:
            # if strings have the same length
            if ns == nt:
                return s[i + 1:] == t[i + 1:]
            # if strings have different lengths
            else:
                return s[i:] == t[i + 1:]
    
    # If there is no diffs on ns distance
    # the strings are one edit away only if
    # t has one more character. 
    return ns + 1 == nt
'''


def count_pairs(target_sum, arr):
    # O(2n)
    # iterate over keys, look for difference key
    # if keys same, take half pairs
    # if keys different, take lower pairs
    # reduce values by pair number
    # add to count

    count = 0

    hashmap = dict()
    for elem in arr:
        if elem not in hashmap:
            hashmap[elem] = 0
        hashmap[elem] += 1

    for key in hashmap:
        diff = target_sum - key
        if diff in hashmap:
            if key == diff:
                pairs = min(hashmap[key], hashmap[diff]) // 2
            else:
                pairs = min(hashmap[key], hashmap[diff])
            hashmap[key] -= pairs
            hashmap[diff] -= pairs
            count += pairs

    return count


# tests = [
#     # (expected, input)
#     (0, {'target': 0, 'arr': [1, 1, 1, 2, 2]}),
#     (0, {'target': 1, 'arr': [1, 1, 1, 2, 2]}),
#     (1, {'target': 2, 'arr': [1, 1, 1, 2, 2]}),
#     (2, {'target': 3, 'arr': [1, 1, 1, 2, 2]}),
#     (1, {'target': 4, 'arr': [1, 1, 1, 2, 2]}),
#     (0, {'target': 5, 'arr': [1, 1, 1, 2, 2]}),
# ]
# for test in tests:
#     expected = test[0]
#     actual = count_pairs(test[1]['target'], test[1]['arr'])
#     print(f"expected: {expected}, actual: {actual}    ||    {test}")