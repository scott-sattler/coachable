from dataclasses import dataclass
import types as t


def brute_force(pattern: str, text: str) -> list[int]:
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
    if len(pattern) > len(text):
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
    if len(pattern) > len(text):
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
    if len(pattern) == 0:
        return []

    if len(pattern) > len(text):
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
    return [0]


all_fns = (
    brute_force,
    knuth_morris_pratt,
    _failure_function,
    rabin_karp,
    _hash,
    rabin_karp_naive,
    boyer_moore,
)

all_matching_fns = (
    brute_force,
    knuth_morris_pratt,
    rabin_karp,
    rabin_karp_naive,
    boyer_moore,
)

primary_matching_fns = (
    brute_force,
    knuth_morris_pratt,
    rabin_karp,
    boyer_moore,
)

if __name__ == "__main__":
    @dataclass
    class TestCase:
        pattern: str
        text: str
        match_index: list[int]
        test_passed: bool | None = None

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
            # TestCase('', 'a', []),
            # TestCase('', 'z', []),
            # TestCase('', 'baz', []),
            # TestCase('', 'bacdefz', []),
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
            TestCase('aa', 'abaaaaaaca', [1, 2, 3, 4, 5]),
            TestCase('aaa', 'aabaaaaaacaa', [1, 2, 3, 4]),
            TestCase('aaaa', 'aaabaaaaaacaaa', [1, 2, 3]),
            TestCase('aaaaa', 'aaaabaaaaaacaaaa', [1, 2]),
            TestCase('aaaaaa', 'aaaaabaaaaaacaaaaa', [1]),

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

        def __init__(self, all_functions: tuple[t.FunctionType]):
            super().__init__()
            self.all_functions = all_functions
            self.primary_fns = (i for i in self.all_functions if i.__name__ != '_' and 'naive' not in i.__name__)
            print(self.primary_fns)

        def run_failure_function_tests(self):
            functions = self.functions
            failure_function_tests = self.failure_function_tests

            results = dict()

            ffun = functions[-2]
            print(f'\nTESTING: {ffun.__name__.upper()}')
            failures = 0
            for ff_test in failure_function_tests:
                inp = ff_test[0]
                out = ff_test[1]
                try:
                    assert [i[1] for i in ffun(inp)] == out
                    print(ff_test, 'PASS')
                except AssertionError:
                    print(ff_test, 'FAIL')
                    failures += 1
            print(f'\n{ffun.__name__.upper()} FAILED {failures} TESTS!\n')

        def run_substring_matching_tests(self):
            raise DeprecationWarning
            functions = self.functions
            test_cases = self.test_cases

            exclusion = lambda obj: isinstance(obj, types.FunctionType) and obj.__name__[0] != '_'  # noqa: lambda fn
            test_fns = {name: obj for name, obj in globals().copy().items() if exclusion(obj)}

            # selector = functions[0].__name__                   # specify single fn here [kmp, rk, bm, ff, bf]
            # test_fns = {selector: test_fns[selector]}

            for fn_name, each_fn in list(test_fns.items())[:]:  # specify fns here
                failed = 0
                print(f'\nTESTING: {fn_name.upper()}')
                for each_test in test_cases[:]:                 # specify test cases here
                    pattern = each_test[0]
                    text = each_test[1]
                    try:
                        assert each_fn(pattern, text) == each_test[2]
                        print(each_test, 'PASS')
                    except AssertionError:
                        print(each_test, 'FAIL')
                        print(each_fn(pattern, text))
                        failed += 1

                tc, p = len(test_cases), (len(test_cases) - failed)
                algo, info = f'{fn_name.upper()}', f'PASSED {p:{3}} of {tc}\nFAILED {failed:{3}} of {tc}'
                print('\n', algo, '\n', info, sep='')
                summary[algo] = info

            print('\n\nSUMMARY')
            for k, v in summary.items():
                print(k, v, sep='\n')

        @staticmethod
        def run_all_class_testcases_on_fn(function: t.FunctionType, tests: list[TestCase]) -> dict:
            data = dict()
            fail_count = 0

            for test in tests:
                try:
                    assert function(test.pattern, test.text) == test.match_index
                    test.test_passed = True
                except AssertionError:
                    fail_count += 1
                    test.test_passed = False
                finally:
                    data[test] = test.test_passed

            return data

        def run_tests_of_class_testcase(self):
            pass

        def time_complexity_tests(self):
            pass

        def run_all(self):
            pass


    testing = Testing(all_fns)
    # testing.run_failure_function_tests()
    # testing.run_substring_matching_tests()
    testing.run_all()

    # test_fns = all_matching_fns
    test_fns = primary_matching_fns


    test_cases = testing.correctness_test_cases

    for test_fn in test_fns:
        print(f'\nTESTING: {test_fn.__name__.upper()}')
        results = testing.run_all_class_testcases_on_fn(test_fn, test_cases)
        # print(results)
        for k, v in results.items():
            print(k, v)
            if not v:
                break

    # tc, p = len(test_cases), (len(test_cases) - failed)
    # algo, info = f'{fn_name.upper()}', f'PASSED {p:{3}} of {tc}\nFAILED {failed:{3}} of {tc}'
    # print('\n', algo, '\n', info, sep='')
    # summary[algo] = info
    #
    # print('\n\nSUMMARY')
    # for k, v in summary.items():
    #     print(k, v, sep='\n')