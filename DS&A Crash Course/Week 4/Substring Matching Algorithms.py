from dataclasses import dataclass
import types as t
from collections.abc import Callable
from hf_data_classes import GenericTC, TestCase, Results
from test_cases import perfect_hash_tests
from test_cases import failure_function_tests
from test_cases import correctness_test_cases


def brute_force(pattern: str, text: str) -> list[int]:
    if not pattern or len(pattern) > len(text):
        return []

    matches = list()
    p_i, s_i = 0, 0
    while s_i < len(text):
        # individual char match
        if pattern[p_i] != text[s_i]:
            s_i = (s_i - p_i) + 1  # backtrack (reset), increment
            p_i = 0
        # full pattern match
        elif p_i == len(pattern) - 1:
            matches.append((s_i - p_i))
            s_i = (s_i - p_i) + 1  # backtrack (reset), increment
            p_i = 0
        # increment
        else:
            s_i += 1
            p_i += 1

    return matches


def knuth_morris_pratt(pattern: str, text: str) -> list[int]:  # noqa: shadows name
    if not pattern or len(pattern) > len(text):
        return []

    matches = list()
    fail_fun = _failure_function(pattern)

    i, j = 0, 0  # text index; pattern index
    while i < len(text):
        if text[i] == pattern[j]:  # char match
            i += 1
            j += 1
            if j == len(pattern):  # full pattern match
                matches.append(i - len(pattern))
                j = fail_fun[-1][1]  # lookup for more nearby matches
        else:  # no char match
            if j != 0:  # failure function lookup on pattern mismatch
                j = fail_fun[j - 1][1]
            else:  # (j == 0) indicates first element mismatched
                i += 1

    return matches


def _failure_function(pat: str) -> list[list[str | int]]:
    ''' longest proper prefix which is also a suffix '''  # noqa
    processed = [[c, 0] for c in pat]

    # i is prefix size
    i, j = 0, 1
    while j < len(pat):
        if pat[i] == pat[j]:
            i += 1
            processed[j][1] = i
        else:
            i = 0
        j += 1

    return processed


def rabin_karp(pattern: str, text: str) -> list[int]:  # noqa: shadows name
    if not pattern or len(pattern) > len(text):
        return []

    lookup = _get_alphabet()

    # hash pattern
    pattern_hash = _hash(pattern, lookup)
    # hash text
    text_hash = _hash(text[:len(pattern)], lookup)

    # compare first occurrence
    matches = list()
    if pattern_hash == text_hash:
        matches.append(0)

    # sliding window hash
    i = len(pattern)
    while i < len(text):
        offset = 100 ** (len(pattern) - 1)
        previous = i - len(pattern)
        text_hash -= _hash(text[previous], lookup) * offset
        text_hash = _hash(text[i], lookup) + (text_hash * 100)  # + shift left 2 digits

        if pattern_hash == text_hash:
            matches.append(i - (len(pattern) - 1))

        i += 1

    return matches


def _get_alphabet():
    # remap a-Z to base 52
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # noqa string.ascii_letters
    return {k: i + 1 for i, k in enumerate(alphabet)}


def _hash(inp: str, lookup: dict) -> int:
    ''' perfect hash: 2 digits per char (base 52 in base 10) '''  # noqa
    hash_value = 0
    for i in range(len(inp)):
        # hash_value += lookup[inp[i]] * (100 ** i)
        # inverse preserves order: abc -> 10203
        max_index = len(inp) - 1
        inv_offset = 100 ** (max_index - i)
        hash_value += lookup[inp[i]] * inv_offset

    return hash_value


# naive implementation O(n*m)
# perfect hash fn required for O(n + m)
def rabin_karp_naive(pattern: str, text: str) -> list[int]:  # noqa: shadows name
    if not pattern or len(pattern) > len(text):
        return []

    matches = list()

    # hash pattern
    pattern_hash = 0
    for char in pattern:
        pattern_hash += ord(char)

    # hash text
    text_hash = 0
    n = len(pattern)
    for i in range(n):
        text_hash += ord(text[i])

    # compare first occurrence
    if pattern == text[:len(pattern)]:
        matches.append(0)

    # sliding window hash
    i = len(pattern)
    while i < len(text):
        text_hash += ord(text[i])
        text_hash -= ord(text[i - len(pattern)])

        if pattern_hash == text_hash:
            start = i - (len(pattern) - 1)
            xstop = i + 1  # noqa naming
            if pattern == text[start:xstop]:  # O(n*m)
                matches.append(start)

        i += 1

    return matches


def boyer_moore(pattern: str, text: str) -> list[int]:  # noqa: shadows name
    return []


if __name__ == "__main__":
    all_fns = (
        brute_force,
        knuth_morris_pratt,
        _failure_function,
        rabin_karp,
        _hash,
        rabin_karp_naive,
        boyer_moore,
    )

    class Testing:
        cr_str = 'COACHABLEROCKS'
        cr_sorted = 'AABCCCEHKLOORS'

        def __init__(self):
            pass

        @staticmethod
        def run_failure_function_tests(tests):
            # todo: refactor (implement Results() etc.)
            function = tuple(x for x in all_fns if 'failure' in x.__name__)[0]
            # results = dict()

            print(f'\nTESTING: {function.__name__.upper()}')
            failures = 0
            for ff_test in tests:
                inp = ff_test.input_data
                out = ff_test.expected
                try:
                    assert [i[1] for i in function(inp)] == out
                    print(ff_test, 'PASS')
                except AssertionError:
                    print(ff_test, 'FAIL')
                    failures += 1
            print(f'\n{function.__name__.upper()} FAILED {failures} TESTS!\n')

        @staticmethod
        def run_all_testcases_on_fn(function, tests: list[TestCase]):  # todo: function and return typing
            data = dict()                                              # todo: Callable[str, str] causes error
            fail_counter = 0

            for test in tests:
                out = function(test.pattern, test.text)
                try:
                    assert out == test.match_index
                    data[test] = (True, out)
                except AssertionError:
                    fail_counter += 1
                    data[test] = (False, out)

            return fail_counter, data

        @staticmethod
        def display_results():
            pass

        def time_complexity_tests(self):
            pass

        def run_all(self):
            pass

        @staticmethod
        def run_perfect_hash_test(tests):
            data = list()
            fail_counter = 0
            lookup = _get_alphabet()

            for test in tests:
                datum = Results(test.input_data)
                datum.result = _hash(test.input_data, lookup)
                try:
                    assert datum.result == test.expected
                    datum.passed = True
                except AssertionError:
                    fail_counter += 1
                    datum.passed = False
                data.append(datum)

            return data


    testing = Testing()
    # testing.run_failure_function_tests()
    # testing.run_substring_matching_tests()
    # testing.run_all()

    test_fns = tuple(f for f in all_fns if f.__name__[0] != '_' and 'NAIVE' not in f.__name__)
    test_fns = tuple(f for f in test_fns if "boyer" in f.__name__)
    test_cases = correctness_test_cases

    red, green = 91, 92
    color = lambda color, obj: str(f'\x1b[{str(color)}m' + str(obj) + '\x1b[0m')  # noqa

    summary = dict()
    for test_fn in test_fns:
        test_fn = test_fn
        fn_name = test_fn.__name__.upper()

        results = testing.run_all_testcases_on_fn(test_fn, test_cases)
        summary[fn_name] = results[:]
        fail_count = results[0]
        results = results[1]
        max_len = 4 + max([len(str(x)) for x in results])

        print(f'\nTESTING: {fn_name}')
        for test_case, output in tuple(results.items()):
            result = 'PASS' + str(output[1]) if output[0] else 'FAIL'
            output = color(red, output) if not output[0] else str(output)
            result += output
            print(f"{str(test_case):{max_len}}{output}")
        fail_txt = f"{color(red, 'FAIL ' + str(fail_count))}"
        pass_txt = f"{color(green, f'PASS ' + str(len(results) - fail_count))}"
        print(f"{fn_name:{max_len}}{pass_txt} | {fail_txt}")

    # for i in range(101):
    #     print(i, str(f'\x1b[{str(i)}m' + 'ABCDEF' + '\x1b[0m'))

    # todo: include easily viewable summary

    # ff_data = testing.run_failure_function_tests(failure_function_tests)
    # print(ff_data)

    # hash_fn_data = testing.run_perfect_hash_test(perfect_hash_tests)
    # print(hash_fn_data)

    # for fn, data_tup in summary.items():
    #     print('asdf', fn)
    #     if data_tup[0] > 0:
    #         for data in data_tup[1].items():
    #             if not data[1][0]:
    #                 print(data)


