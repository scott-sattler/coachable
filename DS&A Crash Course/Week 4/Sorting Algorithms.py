cr_str = "COACHABLEROCKS"
cr_list = list(cr_str)


def insertion_sort(collection: list, debug=False) -> str:
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


def selection_sort(collection: list, debug=False) -> str:
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


def quicksort(collection: list, three_way=False, debug=False) -> str:
    ''' leftmost pivot '''  # noqa
    cr = collection
    if debug: print(''.join(cr))  # noqa
    n = len(cr)
    _quicksort(cr, 0, n - 1, three_way, debug)
    return ''.join(cr)


def _quicksort(arr, lo, hi, three_way, debug):
    if lo >= hi:
        return

    pivot = partition(arr, lo, hi, three_way)

    _quicksort(arr, lo, pivot - 1, debug, three_way)
    _quicksort(arr, pivot + 1, hi, debug, three_way)

    if debug:  print(''.join(arr))  # noqa


def partition(arr, lo, hi, three_way) -> int:
    next_swap = lo + 1

    for i in range(lo + 1, hi + 1):
        if three_way:
            if arr[i] <= arr[lo]:
                arr[i], arr[next_swap] = arr[next_swap], arr[i]
                next_swap += 1
        else:
            if arr[i] < arr[lo]:
                arr[i], arr[next_swap] = arr[next_swap], arr[i]
                next_swap += 1

    swap = next_swap - 1
    arr[lo], arr[swap] = arr[swap], arr[lo]

    return swap


def mergesort_td(collection: list, debug=False) -> str:
    ''' uses ascii minval of 0 '''  # noqa
    cr = collection
    if debug: print(''.join(cr))  # noqa
    return ''.join(_mergesort_td(cr, debug))


def _mergesort_td(arr, debug):
    if len(arr) < 2:
        return arr

    mid_p = len(arr) // 2

    left = _mergesort_td(arr[:mid_p], debug)
    right = _mergesort_td(arr[mid_p:], debug)

    merged = list()
    while left or right:
        left_el = chr(0)
        if len(left) > 0:
            left_el = left[-1]

        right_el = chr(0)
        if len(right) > 0:
            right_el = right[-1]

        if left_el > right_el:
            merged.append(left_el)
            left.pop()
        else:
            merged.append(right_el)
            right.pop()

    if debug:  print(''.join(merged[::-1]))  # noqa

    return merged[::-1]


def mergesort_bu():
    pass


# assert insertion_sort(cr_list[:]) == 'AABCCCEHKLOORS'
# assert selection_sort(cr_list[:]) == 'AABCCCEHKLOORS'
# assert quicksort(cr_list[:]) == 'AABCCCEHKLOORS'
# assert quicksort(cr_list[:], True) == 'AABCCCEHKLOORS'
# assert mergesort_td(cr_list[:], True) == 'AABCCCEHKLOORS'

# insertion_sort(cr_list[:], True)
# selection_sort(cr_list[:], True)
# quicksort(cr_list[:], three_way=False, debug=True)
# quicksort(cr_list[:], three_way=True, debug=True)
mergesort_td(cr_list[:], True)
