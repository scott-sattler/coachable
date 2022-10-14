
# not comprehensive
DEFAULT_TEST = [
    [5, 2, 4, 6, 1, 3],
    [1],
    [2],
    [],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1],

    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1],
]


class Sort:

    @staticmethod
    def insertion_sort(arr: list) -> list:
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j > -1 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr

    @staticmethod
    def selection_sort(arr: list) -> list:

        n = len(arr)
        for i in range(0, n):

            min_index = i
            j = i + 1
            while j < n:
                if arr[j] < arr[min_index]:
                    min_index = j
                j += 1

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


class Test(Sort):
    def test_all(self, test_array: list[list], verbose: bool = True):
        for each_item in dir(Sort):
            if not each_item.startswith("__"):
                fn = getattr(Sort, each_item)
                self.test(test_array, fn, not verbose)

    def test(self, test_cases: list[list] | list, sorting_algo: callable, only_fail: bool = False):
        # make single test compatible with multi-test
        if not isinstance(test_cases[0], list):
            test_cases = [test_cases]

        fails = []
        test_count = 0
        for each_test in test_cases:
            tested_input = each_test
            output = sorting_algo(tested_input)
            expected_out = sorted(tested_input)

            try:
                test_count += 1
                assert output == expected_out
                result = "PASS"
            except AssertionError:
                result = "FAIL"
                fails.append(tested_input)

            if not only_fail or result == "FAIL":
                print(f"{result}:\t\t{tested_input}")
                print(f"expected:\t{expected_out:}")
                print(f"received:\t{output:}")
                print()

        print(f"{sorting_algo.__name__}: RAN {test_count} | PASSED {test_count-len(fails)} | FAILED {len(fails)}: {fails}")


# Test().test(DEFAULT_TEST, Sort().insertion_sort, only_fail=True)
# Test().test(DEFAULT_TEST, Sort().insertion_sort, only_fail=False)
# Test().test(DEFAULT_TEST, Sort().selection_sort, only_fail=False)
Test().test_all(DEFAULT_TEST, verbose=False)



