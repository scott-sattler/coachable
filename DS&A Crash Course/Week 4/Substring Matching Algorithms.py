

def knuth_morris_pratt(pattern: str, text: str) -> list[int]:  # noqa: shadows name
    return [0]


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
        text_hash = _hash(text[i], lookup) + (text_hash * 100)  # shift left 2 digits

        if pattern_hash == text_hash:
            matches.append(i - (len(pattern) - 1))

        i += 1

    return matches


def _hash(inp: str, lookup: dict) -> int:
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
    cr_str = 'COACHABLEROCKS'
    cr_sorted = 'AABCCCEHKLOORS'

    functions = [
        knuth_morris_pratt,
        rabin_karp,
        boyer_moore,

    ]

    test_cases = [
        # pattern, text, leftmost match index
        # basic naive tests
        ('abc', 'ab', []),
        ('abc', 'a', []),
        ('abc', '', []),
        ('a', '', []),
        ('z', '', []),

        ('abc', 'abc', [0]),
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
        ('abcabcg', 'aaabcabcabcxabcabcg', [12]),


    ]

    test_fns = {name: obj for name, obj in globals().copy().items() if callable(obj) and name[0] != '_'}
    summary = dict()

    selector = functions[1].__name__  # specify fn here
    test_fns = {selector: test_fns[selector]}

    for fn_name, each_fn in list(test_fns.items())[:]:  # specify fn here
        failed = 0
        print(f'\nTESTING: {fn_name.upper()}')
        for each_test in test_cases[:]:  # specify test cases here
            pattern = each_test[0]
            text = each_test[1]
            try:
                assert each_fn(pattern, text) == each_test[2]
                print(each_test, 'PASS')
            except AssertionError:
                print(each_test, 'FAIL')
                print(each_fn(pattern, text))
                # assert brute_force(each_test[0], each_test[1]) == each_test[2]  # for easy debugging
                failed += 1

        tc, p = len(test_cases), (len(test_cases) - failed)
        algo, info = f'{fn_name.upper()}', f'PASSED {p:{3}} of {tc}\nFAILED {failed:{3}} of {tc}'
        print('\n', algo, '\n', info, sep='')
        summary[algo] = info

    print('\n\nSUMMARY')
    for k, v in summary.items():
        print(k, v, sep='\n')
