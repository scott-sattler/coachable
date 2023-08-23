

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


def knuth_morris_pratt(pattern: str, text: str) -> list[int]:
    if not pattern or len(pattern) > len(text):
        return []

    matches = list()
    fail_fn = _failure_function(pattern)

    i, j = 0, 0  # text index; pattern index
    while i < len(text):
        if text[i] == pattern[j]:  # char match
            i += 1
            j += 1
            if j == len(pattern):  # full pattern match
                matches.append(i - len(pattern))
                j = fail_fn[-1][1]  # lookup for more nearby matches
        else:  # no char match
            if j != 0:  # failure function lookup on pattern mismatch
                j = fail_fn[j - 1][1]
            else:  # (j == 0) indicates first element mismatched
                i += 1

    return matches


# partial match table
def _failure_function(pattern: str) -> list[list[str | int]]:
    ''' longest proper prefix which is also a suffix '''  # noqa
    processed = [[c, 0] for c in pattern]

    # i is prefix size
    i, j = 0, 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            processed[j][1] = i
        else:
            i = 0
        j += 1

    return processed


def rabin_karp(pattern: str, text: str) -> list[int]:
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
    # remap a-Z to base 52 (in base 10)
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
def rabin_karp_naive(pattern: str, text: str) -> list[int]:
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


# implementation limited to bad character rule
# only O(n + m) if no match occurs (e.g. ('aa...', 'aaaa...') -> [0, 1, 2...])
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm#Performance
def boyer_moore(pattern: str, text: str) -> list[int]:
    if not pattern or len(pattern) > len(text):
        return []

    patl = len(pattern)
    matches = list()
    table = _bad_char_table(pattern)

    txt_i = len(pattern) - 1
    while txt_i < len(text):
        txt_j = txt_i
        pat_i = len(pattern) - 1
        while pat_i > -1 and text[txt_j] == pattern[pat_i]:
            txt_j -= 1
            pat_i -= 1

        if pat_i < 0:  # match
            matches.append(txt_j + 1)

            # check bounds and shift by lookup for next text char
            txt_i += 1
            txt_i += table[text[txt_i]] - 1 if txt_i < len(text) else txt_i
        else:
            # if rightmost occurrence to left of mismatch
            # shift table to that occurrence, else shift 1
            shift = table[text[txt_j]]
            txt_i += shift if patl - pat_i < shift else 1

    return matches


# bad character/shift table
# p763: delta_1 is "the difference between [the pattern length] and
# the position of the rightmost occurrence of char in [pattern]"
def _bad_char_table(pattern: str, alphabet: list[str] = None) -> dict[str, int]:
    # implicit data structures (i.e. table[ord(char)] <- val) disfavored
    alphabet = list(_get_alphabet().keys()) if not alphabet else alphabet

    table = {k: len(pattern) for k in alphabet}
    for i, c in enumerate(pattern):
        table[c] = max(1, len(pattern) - i - 1)
    return table




all_fns = (
    brute_force,
    knuth_morris_pratt,
    _failure_function,
    rabin_karp,
    _hash,
    rabin_karp_naive,
    boyer_moore,
    _bad_char_table,

)