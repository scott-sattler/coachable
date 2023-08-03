from __future__ import annotations
import string

'''
Question 11. Write a function that takes in a string,
and returns the same string, but with 
1. trailing whitespaces at the beginning and end of string removed and
2. each group of consecutive whitespaces changed to a single dash '-'
'''


def question11(input_string: str) -> str:
    # no time to clean up
    processed = []
    inp = input_string
    n = len(inp)
    i = 0
    while i < n:
        if inp[i] == ' ':
            while i < n and inp[i] == ' ':
                i += 1
            processed.append('-')
            continue
        processed.append(inp[i])
        i += 1

    if processed[0] == '-':
        processed.pop(0)
    if processed[-1] == '-':
        processed.pop()

    return ''.join(processed)


'''
Question 12. Write a function that takes in a string,
and returns the same string, but with every other letter capitalized,
starting with the character at index 1.
Your algorithm must run in O(n), where n is the length of the input string.
'''


def question12(input_string: str) -> str:
    inp = input_string
    n = len(inp)
    processed = []

    for i in range(n):
        if i % 2 == 0:
            processed.append(inp[i])
            continue

        processed.append(inp[i].capitalize())

    return ''.join(processed)


'''
Question 13. Write in a function that takes in a list of strings,
and counts the frequency of all the words, case-insensitive. 
Return the result as a dictionary where the keys are the 
lowercased words, and the values are the frequencies of those words. 
Return it as a normal dictionary, not defaultdict.
'''


def question13(input_strings: list[str]) -> dict[str, int]:
    freq_map = dict()
    for word_str in input_strings:
        for word in word_str.split():
            if word.lower() in freq_map:
                freq_map[word.lower()] += 1
            else:
                freq_map[word.lower()] = 1
    return freq_map


# from stencil import *

def test_question11_case1():
    assert question11('hello there  everyone') == 'hello-there-everyone'


def test_question11_case2():
    assert question11('  trailing whitespace ') == 'trailing-whitespace'


def test_question12_case1():
    assert question12('coachable') == 'cOaChAbLe'


def test_question13_case1():
    assert question13(['hello hi all', 'hello again']) == {'hello': 2, 'hi': 1, 'all': 1, 'again': 1}


def test_question13_case2():
    assert question13(['hello hI all', 'HELLO again']) == {'hello': 2, 'hi': 1, 'all': 1, 'again': 1}
