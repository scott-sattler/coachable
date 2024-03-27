'''

prefix tree
time: O(n * k)
where
    n is the number of input operations
    k is the average word length

space: O(m * k)
where
    m is the number of words
    k is the average word length


w/ wild card:
space: O(m * k)
    stack O(maximum depth)
    same (or less than) order of nodes (m * k)
time: O(n * k * m)
OR
time: O(n * a ^ s)
where
    a is the alphabet size
    s is the number of stars

degenerate input:
'.....................z'


normal traversal
    if wild card
    search for any child
    within every child, does at least one match the search input


'prefix + wild card (*) + long string + unique character


.. sdfsdfadaf
^
at most, alphabet size

 ^
 at most, alphabet size



normal traversal
    if wild card
    search for any child
    within every child, does at least one match the search input


p = self.root
for c in word:
    if not c in p:
        p[c] = {}
    p = p[c]


for every word with a wild card
search for entire alphabet variation on wild card

alphabet: abc
input: a.c
search: aac
        abc
        acc
constrained by: nodes avaliable



w * r d
      ^
[d, r, a, d, r, b]

    w

a   b ... o  ... z

[w, b, r, d]


base case(s):
    no child matchs
    end of word

recursive case(s):
    fn(ptr/ref/trie level, i + 1)

'''


class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            if not c in p:
                p[c] = {}
            p = p[c]
        p['is_word'] = True

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)

    def _search(self, word: str, i: int, ref: dict) -> bool:
        if i >= len(word):
            if 'is_word' in ref:
                return True
            return False

        valid_chars = list()
        if word[i] in ref:
            valid_chars.append(word[i])
        elif word[i] == '.':
            valid_chars = [k for k in ref.keys() if k != 'is_word']

        if not ref or not valid_chars:
            return False

        for char in valid_chars:
            if self._search(word, i + 1, ref[char]):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
