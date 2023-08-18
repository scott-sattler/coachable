import types  # todo


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

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # noqa ascii_letters
    lookup = {k: i + 1 for i, k in enumerate(letters)}  # noqa naming

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
    ''' perfect hash '''  # noqa
    ''' 2 digits per char (base 52) '''
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


if __name__ == "__main__":
    class Testing:
        cr_str = 'COACHABLEROCKS'
        cr_sorted = 'AABCCCEHKLOORS'

        failure_function_tests = [
            ('', []),
            ('abc', [0, 0, 0]),
            ('aba', [0, 0, 1]),
            ('ab', [0, 0]),
            ('ababab', [0, 0, 1, 2, 3, 4]),
            ('abcabc', [0, 0, 0, 1, 2, 3]),
            ('aabaababb', [0, 1, 0, 1, 2, 3, 4, 0, 0]),

        ]

        test_cases = [
            # todo: better time complexity test(s)
            # pattern, text, leftmost match index
            # basic naive tests
            ('abc', 'ab', []),
            ('abc', 'a', []),
            ('abc', '', []),
            ('a', '', []),
            ('z', '', []),

            ('abc', 'abc', [0]),
            ('abc', 'zabc', [1]),
            ('abc', 'abcd', [0]),
            ('dabc', 'abc', []),
            ('abc', 'aabcc', [1]),
            ('aaabc', 'abc', []),

            ('abc', 'abcbc', [0]),
            ('abc', 'abcabc', [0, 3]),
            ('aaa', 'aaaaaa', [0, 1, 2, 3]),
            ('baaac', 'aaaaaa', []),
            ('aaa', 'baaaaaac', [1, 2, 3, 4]),

            # kmp specific tests
            ('aabcaa', 'aabcabaabcaa', [6]),
            ('aaabc', 'aaaaabcaaabc', [2, 7]),
            ('aaabc', 'aaaaabcaaaabc', [2, 8]),
            ('abcabcg', 'aaabcabcabcxabcabcg', [12]),
            ('a', 'a', [0]),
            ('a', 'aaaaa', [0, 1, 2, 3, 4]),
            ('aaaa', 'aaaaaaa', [0, 1, 2, 3]),

            ('onions', 'onionionspl', [3]),

            # ('a' * 1_000 + 'd', 'a' * 1_000_000 + 'd', [999_000]),


        ]

        functions = [
            knuth_morris_pratt,
            rabin_karp,
            boyer_moore,

            _hash,
            _failure_function,
            brute_force,
        ]

        def __init__(self):
            pass

        def run_failure_function_tests(self):
            functions = self.functions
            failure_function_tests = self.failure_function_tests

            results = list()

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
            functions = self.functions
            test_cases = self.test_cases

            exclusion = lambda obj: isinstance(obj, types.FunctionType) and obj.__name__[0] != '_'  # noqa: lambda fn
            test_fns = {name: obj for name, obj in globals().copy().items() if exclusion(obj)}
            summary = dict()

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

        def run_all(self):
            self.run_failure_function_tests()
            self.run_substring_matching_tests()

    testing = Testing()
    # testing.run_failure_function_tests()
    # testing.run_substring_matching_tests()
    testing.run_all()
