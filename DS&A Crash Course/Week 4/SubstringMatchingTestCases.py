from hf_data_classes import GenericTC, TestCase, Results


perfect_hash_tests: list[GenericTC] = [
    GenericTC('a', 1),
    GenericTC('b', 2),
    GenericTC('z', 26),
    GenericTC('A', 27),
    GenericTC('Y', 51),
    GenericTC('Z', 52),
    GenericTC('abc', 10203),
    GenericTC('cba', 30201),
    GenericTC('aaa', 10101),
    GenericTC('baaab', 201010102),
]

failure_function_tests: list[GenericTC] = [
    GenericTC('', []),
    GenericTC('abc', [0, 0, 0]),
    GenericTC('aba', [0, 0, 1]),
    GenericTC('ab', [0, 0]),
    GenericTC('ababab', [0, 0, 1, 2, 3, 4]),
    GenericTC('abcabc', [0, 0, 0, 1, 2, 3]),
    GenericTC('aabaababb', [0, 1, 0, 1, 2, 3, 4, 0, 0]),

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

    # knuth-morris-pratt specific tests
    TestCase('aabcaa', 'aabcabaabcaa', [6]),
    TestCase('aaabc', 'aaaaabcaaabc', [2, 7]),
    TestCase('aaabc', 'aaaaabcaaaabc', [2, 8]),
    TestCase('abcabcg', 'aaabcabcabcxabcabcg', [12]),

    TestCase('onions', 'onionionspl', [3]),

    # rabin-karp specific tests
    TestCase('j', 'a', []),
    TestCase('i', 'a', []),
    TestCase('k', 'a', []),

    # boyer-moore specific tests
    TestCase('b', 'aaaaab', [5]),
    TestCase('b', 'aaaaaba', [5]),
    TestCase('b', 'aaaaabaa', [5]),
    TestCase('baa', 'aaa', []),
    TestCase('baa', 'aaaaaaaaa', []),
    TestCase('abc', 'dddddddddddd', []),
    TestCase('abc', 'cacccbabc', [6]),

    # duplicate
    TestCase('abc', 'abcbc', [0]),
    TestCase('abc', 'abcabc', [0, 3]),
    TestCase('baaac', 'aaaaaa', []),

]

time_complexity_test_cases: list[TestCase] = [
    # todo: better time complexity test(s)
    TestCase('a' * 1_000 + 'd', 'a' * 1_000_000 + 'd', [999_000]),

]