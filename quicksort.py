
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
