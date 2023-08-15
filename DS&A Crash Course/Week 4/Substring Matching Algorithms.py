

def knuth_morris_pratt(pattern: str, text: str) -> list[int]:
    return [0]


def rabin_karp(pattern: str, text: str) -> list[int]:
    return [0]


def boyer_moore(pattern: str, text: str) -> list[int]:
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

    test_fns = {name: obj for name, obj in globals().copy().items() if callable(obj)}
    summary = dict()
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
