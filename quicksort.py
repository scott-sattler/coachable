
# quicksort (in place)
# leftmost pivot implementation
def quicksort_leftmost(arr: list) -> None:
    # calls helper method _quicksort
    _quicksort_leftmost(arr, 0, len(arr) - 1)


def _quicksort_leftmost(arr: list, low: int, high: int) -> None:
    # recursion -> base case
    # reduced data set -> left/right subarrays

    # base case
    # pivot
    # left/right recurse

    # base case
    if low >= high:
        return
    # pivot index
    pivot_index = partition_leftmost(arr, low, high)
    # recurse left
    _quicksort_leftmost(arr, low, pivot_index - 1)
    # recurse right
    _quicksort_leftmost(arr, pivot_index + 1, high)


def partition_leftmost(arr: list,  low: int, high: int) -> int:
    # returns index of pivot element

    # pivot is low (leftmost)
    # swap index
    # from left to right swaps

    # swap index
    next_swap_index = low + 1

    # iterate over low<->high swapping
    for i in range(low + 1, high + 1):
        if arr[i] < arr[low]:
            arr[i], arr[next_swap_index] = arr[next_swap_index], arr[i]
            next_swap_index += 1

    # swap pivot to correct position
    arr[next_swap_index - 1], arr[low] = arr[low], arr[next_swap_index - 1]

    # return index of pivot element
    return next_swap_index - 1


unsorted_leftmost = [3, 4, 2, 1, 5, 6, 2, 7, 8, 8, 3, 11, 100, 0, -3, -10, 9]
quicksort_leftmost(unsorted_leftmost)
print(unsorted_leftmost)


# without reference
# important principal:
# the pivot's final location can be obtained by moving all elements lower/higher
# to the left/right of the pivot
def quicksort_rightmost(arr):
    # right to left (high is pivot)
    _quicksort_rightmost(arr, 0, len(arr) - 1)


def _quicksort_rightmost(arr, low, high):
    # pivot
    # recurse left/right
    # base case
    if low >= high:  # this is when no swaps found? and/or other cases?
        return

    pivot = partition_rightmost(arr, low, high)

    # recurse left
    _quicksort_rightmost(arr, low, pivot - 1)

    # recurse right
    _quicksort_rightmost(arr, pivot + 1, high)


def partition_rightmost(arr, low, high):
    par_val = arr[high]
    next_swap_index = high - 1

    # swap out of place (high/low) elements
    for i in range(high - 1, low - 1, -1):
        if arr[i] > par_val:  # when out of place
            arr[i], arr[next_swap_index] = arr[next_swap_index], arr[i]  # swap
            next_swap_index -= 1  # decrement
    # put pivot into place
    arr[high], arr[next_swap_index + 1] = arr[next_swap_index + 1], arr[high]
    return next_swap_index + 1


unsorted_rightmost = [3, 4, 2, 1, 5, 6, 2, 7, 8, 8, 3, 11, 100, 0, -3, -10, 9]
quicksort_rightmost(unsorted_rightmost)
print(unsorted_rightmost)


# leftmost partition
def quicksort(arr):
    _quicksort_helper(arr, 0, len(arr) - 1)


def _quicksort_helper(arr, low, high):
    if low >= high:
        return

    pivot_index = partition(arr, low, high)
    # lower
    _quicksort_helper(arr, low, pivot_index -1)
    # upper
    _quicksort_helper(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    low_swap = low + 1

    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            arr[i], arr[low_swap] = arr[low_swap], arr[i]
            low_swap += 1
    arr[low], arr[low_swap - 1] = arr[low_swap - 1], arr[low]
    return low_swap - 1


unsorted = [3, 4, 2, 1, 5, 6, 2, 7, 8, 8, 3, 11, 100, 0, -3, -10, 9]
quicksort(unsorted)
print(unsorted)


# median of 3 (mo3) partition
def quicksort_mo3(arr):
    return _quicksort_mo3(0, len(arr) - 1, arr)


def _quicksort_mo3(lo, hi, arr):
    if lo >= hi:
        return

    # find pivot
    mo3_pivot = _mo3_pivot(lo, hi, arr)
    # recurse left
    _quicksort_mo3(lo, mo3_pivot - 1, arr)
    # recurse right
    _quicksort_mo3(mo3_pivot + 1, hi, arr)


def _mo3_pivot(lo, hi, arr):
    mid = lo + (hi - lo) // 2

    # correctly order lo, mid, hi
    # todo: reconsider/refactor
    if arr[lo] > arr[mid]:
        _swap(lo, mid, arr)
    if arr[mid] > arr[hi]:
        _swap(mid, hi, arr)
    if arr[lo] > arr[mid]:
        _swap(lo, mid, arr)

    if (hi + 1) - (lo + 1) < 4:
        return mid

    # swap mid with leftmost
    _swap(lo, mid, arr)
    # then perform leftmost
    piv = lo
    for i in range(lo, hi + 1):
        if arr[i] < arr[lo]:
            _swap(i, piv + 1, arr)
            piv += 1
    _swap(piv, lo, arr)
    return piv


def _swap(ind_1, ind_2, arr):
    arr[ind_1], arr[ind_2] = arr[ind_2], arr[ind_1]


# unsorted = [3, 4, 2, 1, 5, 6, 2, 7, 8, 8, 3, 11, 100, 0, -3, -10, 9]
unsorted = [3, 4, 8, 9, 5, 6, 2, 7, 2, 8, 3, 11, 100, 0, -3, -10, 1]
quicksort_mo3(unsorted)
print(unsorted)
