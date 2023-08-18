from dataclasses import dataclass
import types as t
from collections.abc import Callable


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

    # remap a-Z to base 52
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # noqa string.ascii_letters
    lookup = {k: i + 1 for i, k in enumerate(letters)}  # noqa shadows name

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

def _hash(inp: str, lookup: dict) -> int:  # noqa: shadows name
    ''' perfect hash: 2 digits per char (base 52) '''  # noqa
    hash_value = 0
    for i in range(len(inp)):
        # inv_i preserves order: abc -> 102030
        inv_i = (len(inp) - 1) - i
        base = 10 * (100 ** inv_i)
        hash_value += (lookup[inp[i]] * base)

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

    @dataclass
    class TestCase:
        pattern: str
        text: str
        match_index: list[int]

        def __repr__(self):
            return f"({self.pattern}, {self.text}, {self.match_index})"

        def __hash__(self):
            return hash(self.__repr__())


    class Testing:
        cr_str = 'COACHABLEROCKS'
        cr_sorted = 'AABCCCEHKLOORS'

        perfect_hash_tests: list[tuple[str | int]] = [
            ('a', 1),
            ('b', 2),

            ('z', 26),
            ('A', 27),

            ('Y', 51),
            ('Z', 52),

            ('abc', 10203),
            ('cba', 30201),
        ]

        failure_function_tests: list[tuple[str | list[int]]] = [
            ('', []),
            ('abc', [0, 0, 0]),
            ('aba', [0, 0, 1]),
            ('ab', [0, 0]),
            ('ababab', [0, 0, 1, 2, 3, 4]),
            ('abcabc', [0, 0, 0, 1, 2, 3]),
            ('aabaababb', [0, 1, 0, 1, 2, 3, 4, 0, 0]),

        ]

        correctness_test_cases: list[TestCase] = [
            # basic/naive tests
            TestCase('a', 'a', [0]),
            TestCase('a', 'aaaaa', [0, 1, 2, 3, 4]),
            TestCase('aaaa', 'aaaaaaa', [0, 1, 2, 3]),

            # bad input tests
            TestCase('', 'a', []),
            TestCase('', 'z', []),
            TestCase('', 'baz', []),
            TestCase('', 'bacdefz', []),
            TestCase('a', '', []),
            TestCase('z', '', []),
            TestCase('abc', '', []),
            TestCase('abc', 'a', []),
            TestCase('abc', 'ab', []),
            TestCase('dabc', 'abc', []),
            TestCase('aaabc', 'abc', []),
            TestCase('abcz', 'abc', []),

            # no match tests
            TestCase('baaac', 'aaaaaa', []),
            TestCase('baaac', 'baaaaa', []),
            TestCase('baaac', 'baaaac', []),

            TestCase('abc', 'abc', [0]),
            TestCase('abc', 'zabc', [1]),
            TestCase('abc', 'abcd', [0]),
            TestCase('abc', 'aabcc', [1]),

            TestCase('abc', 'abcbc', [0]),
            TestCase('abc', 'abcabc', [0, 3]),
            TestCase('aaa', 'aaaaaa', [0, 1, 2, 3]),
            TestCase('a', 'baaaaaac', [1, 2, 3, 4, 5, 6]),
            TestCase('aa', 'abaaaaaaca', [2, 3, 4, 5, 6]),
            TestCase('aaa', 'aabaaaaaacaa', [3, 4, 5, 6]),
            TestCase('aaaa', 'aaabaaaaaacaaa', [4, 5, 6]),
            TestCase('aaaaa', 'aaaabaaaaaacaaaa', [5, 6]),
            TestCase('aaaaaa', 'aaaaabaaaaaacaaaaa', [6]),

            # kmp specific tests
            TestCase('aabcaa', 'aabcabaabcaa', [6]),
            TestCase('aaabc', 'aaaaabcaaabc', [2, 7]),
            TestCase('aaabc', 'aaaaabcaaaabc', [2, 8]),
            TestCase('abcabcg', 'aaabcabcabcxabcabcg', [12]),

            TestCase('onions', 'onionionspl', [3]),


        ]

        time_complexity_test_cases: list[TestCase] = [
            # todo: better time complexity test(s)
            TestCase('a' * 1_000 + 'd', 'a' * 1_000_000 + 'd', [999_000]),


        ]

        # def __init__(self, all_functions: tuple[t.FunctionType]):
        #     super().__init__()
        #     self.all_functions = all_functions
        #     self.primary_fns = (i for i in self.all_functions if i.__name__ != '_' and 'naive' not in i.__name__)
        #     print(self.primary_fns)

        def run_failure_function_tests(self):
            # todo: fix after refactor
            function = tuple(x for x in all_fns if 'failure' in x.__name__)[0]
            failure_function_tests = self.failure_function_tests

            # results = dict()

            print(f'\nTESTING: {function.__name__.upper()}')
            failures = 0
            for ff_test in failure_function_tests:
                inp = ff_test[0]
                out = ff_test[1]
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


    testing = Testing()
    # testing.run_failure_function_tests()
    # testing.run_substring_matching_tests()
    # testing.run_all()

    test_fns = tuple(f for f in all_fns if f.__name__[0] != '_' and 'NAIVE' not in f.__name__)
    test_cases = testing.correctness_test_cases

    red, green = 91, 92
    color = lambda color, obj: str(f'\x1b[{str(color)}m' + str(obj) + '\x1b[0m')  # noqa

    print('fffffffffffffffffff', test_fns)
    for test_fn in test_fns:
        test_fn = test_fn
        fn_name = test_fn.__name__.upper()

        results = testing.run_all_testcases_on_fn(test_fn, test_cases)
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

    # testing.run_failure_function_tests()
