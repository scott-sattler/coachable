# import quicksort
cr_str = "COACHABLEROCKS"
cr_list = list(cr_str)


def insertion_sort(collection: list, debug=False):
    ''' swap implementation '''  # noqa
    cr = collection
    if debug: print(''.join(cr))  # noqa
    n = len(cr)
    for i in range(n):
        j = i
        while j > 0 and cr[j] < cr[j - 1]:
            cr[j], cr[j - 1] = cr[j - 1], cr[j]
            if debug: print(''.join(cr))  # noqa
            j -= 1
    return ''.join(cr)


def selection_sort(collection: list, debug=False):
    ''' swap implementation '''  # noqa
    cr = collection
    if debug: print(''.join(cr))  # noqa
    n = len(cr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if cr[j] < cr[min_index]:
                min_index = j
        if i != min_index:
            cr[i], cr[min_index] = cr[min_index], cr[i]
            if debug: print(''.join(cr))  # noqa
    return ''.join(cr)


def quicksort(collection: list, debug=False):
    ''' leftmost pivot '''  # noqa
    cr = collection
    if debug: print(''.join(cr))  # noqa
    n = len(cr)
    _quicksort(cr, 0, n - 1, debug)
    return ''.join(cr)


def _quicksort(arr, lo, hi, debug):
    if lo >= hi:
        return

    pivot = partition(arr, lo, hi)

    if debug:  print(''.join(arr))  # noqa

    _quicksort(arr, lo, pivot - 1, debug)
    _quicksort(arr, pivot + 1, hi, debug)


def partition(arr, lo, hi) -> int:
    next_swap = lo + 1

    for i in range(lo + 1, hi + 1):
        if arr[i] < arr[lo]:
            arr[i], arr[next_swap] = arr[next_swap], arr[i]
            next_swap += 1

    swap = next_swap - 1
    arr[lo], arr[swap] = arr[swap], arr[lo]

    return swap


# assert insertion_sort(cr_list[:]) == 'AABCCCEHKLOORS'
# assert selection_sort(cr_list[:]) == 'AABCCCEHKLOORS'
assert quicksort(cr_list[:]) == 'AABCCCEHKLOORS'

# insertion_sort(cr_list[:], True)
# selection_sort(cr_list[:], True)
quicksort(cr_list[:], True)
