import itertools
import math

values = [46, 34, 42, 23, 52, 33]
# values = list(map(lambda x: x % 10, values))
# print(list(values))

all_permutations: list = list(itertools.permutations(values))
# print(all_permutations)

hash_list = [[i, None] for i in range(9)]
# print(hash_list)

target_result = [46, 34, 42, 23, 52, 33]

# helper fns
log_10 = lambda x: x % 10  # noqa
format_print = lambda x: ' '.join([str(i) for i in x])  # noqa

# tests
# all_permutations = [[46, 34, 42, 23, 52, 33, 46, 46, 46, 46]]  # no fail; full; wrap
# all_permutations = [[46, 34, 42, 23, 52, 33, 46, 46, 46, 46, 46]]  # fail too large


def insert_value(value, hashmap):
    index = log_10(value)
    if hashmap[index][1] is not None:
        tries = 0
        while tries < len(hashmap):
            if hashmap[index][1] is not None:
                tries += 1
                index = log_10(index + 1)
            else:
                hashmap[index][1] = value
                break
        else:
            if tries == len(hashmap):
                print(value, "fails in", hashmap)
                raise SystemExit("insertion failed: hashmap full")
    else:
        hashmap[index][1] = value


tests_ran = 0
failed = 0
for each_permutation in all_permutations:
    tests_ran += 1
    print("testing:", ' '.join([str(i) for i in each_permutation]))
    current_solution = [[i, None] for i in range(10)]
    for each_value in each_permutation:
        insert_value(each_value, current_solution)

    # next line tests valid solution checker
    # current_solution = [[0, 46], [1, None], [2, 34], [3, None], [4, 42], [5, 23], [6, 52], [7, None], [8, 33]]
    result = [i[1] for i in current_solution if i[1] is not None]
    if result == target_result:
        print("Solution found!", format_print(result))
        break
    else:
        failed += 1
        print("failed: ", format_print(result))
else:
    n = len(values)
    print(f"Possible Tests: {math.factorial(n)} | Tests Ran: {tests_ran} | Tests Failed: {failed}")
