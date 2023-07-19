
cr_str = "COACHABLEROCKS"
cr_list = list(cr_str)


def insertion_sort(collection: list):
    ''' swap implementation '''  # noqa
    cr = collection
    n = len(cr)
    for i in range(n):
        j = i
        while j > 0 and cr[j] < cr[j - 1]:
            cr[j], cr[j - 1] = cr[j - 1], cr[j]
            j -= 1
    return ''.join(cr)


def selection_sort(collection: list):
    ''' swap implementation '''  # noqa
    cr = collection
    n = len(cr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if cr[j] < cr[min_index]:
                min_index = j
        if i != min_index:
            cr[i], cr[min_index] = cr[min_index], cr[i]
    return ''.join(cr)




assert insertion_sort(cr_list) == 'AABCCCEHKLOORS'
assert selection_sort(cr_list) == 'AABCCCEHKLOORS'


