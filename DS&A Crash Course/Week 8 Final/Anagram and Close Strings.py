from __future__ import annotations
from typing import *

'''
Determine if these 2 strings are anagrams in O(n) runtime

You can assume that a,b are strings with only letters.
You should ignore capitalizations.

For example,
check_anagram("inTegRal", "Triangle") -> True
'''


def check_anagram(a: str, b: str) -> bool:
    # can add len check

    a = a.lower()
    b = b.lower()

    a_map = dict()
    for char in a:
        if char not in a_map:
            a_map[char] = 0
        a_map[char] += 1

    for char in b:
        if char not in a_map:
            return False
        a_map[char] -= 1

    for val in a_map.values():
        if val != 0:
            return False

    return True


'''
Given 2 strings determine how many full and partial matches they have.

a = BEARS
b = BEAST
-> (3,1)

3 full matches because BEA
1 partial match since S is in the remaining part of the string but incorrect index.

a = BANANA
b = ORANGE
-> (0, 2)

0 full matches and 2 partial matches for AN.

Return as a tuple (full matches, partial matches)
'''


def close_strings(a: str, b: str) -> tuple:
    full = 0
    part = 0

    a_map = dict()
    for char in a:
        if char not in a_map:
            a_map[char] = 0
        a_map[char] += 1

    n = len(b)
    for i in range(n):
        if b[i] == a[i]:
            full += 1
            continue

        if b[i] in a_map and a_map[b[i]] > 0:
            a_map[b[i]] -= 1
            part += 1

    return full, part


print(check_anagram("inTegRal", "Triangle"))

a = 'BEARS'
b = 'BEAST'
print(close_strings(a, b))
a = 'BANANA'
b = 'ORANGE'
print(close_strings(a, b))
