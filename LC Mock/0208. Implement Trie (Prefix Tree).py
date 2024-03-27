###############################################################################
# live solution:
#   hash map implementation
# time: O(n*k)
#   where
#   n is the number of input operations
#   k is average word length
# space: O(m*k)
#   where
#   m is the number of words

'''

dictionary {letter: children}
where
children <- {letter: children}

example:
abc -> {a: {b: {is_word: True, c: None}}}


O(n*k) time
where
n is the number of input operations
k is average word length

O(m*k) space
where
m is the number of words


solution:

.insert()
# for every letter in word
    # create node if dne
    # traverse down a level
# indicate word completion

.search()
# for each letter
    # if node dne
        # return false
    # traverse down trie
# return true if sentinel present

.startsWith()
# for each letter
    # if node dne
        # return false
    # traverse down trie
# return true

'''


class Trie:
    '''
    {letter: children}
    where is_word is in children dict
    '''

    def __init__(self):
        self.root = dict()

    def _traverse(self, word) -> bool | dict:
        p = self.root
        for c in word:
            if not c in p:
                return False
            p = p[c]
        return p

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if not c in p:
                p[c] = dict()
            p = p[c]
        p['is_word'] = True

    def search(self, word: str) -> bool:
        p = self._traverse(word)
        return p and 'is_word' in p

    def startsWith(self, prefix: str) -> bool:
        p = self._traverse(prefix)
        return type(p) is dict


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


###############################################################################
# live solution:
#   array implementation
# time: O(n*k)
#   where
#   n is the number of input operations
#   k is average word length
# space: O(k*a)
#   where
#   a is the alphabet size

'''
trie
    t
    r
      i
      e

tree
    t
    r
  e   i
  e   e

tree
    t
    r
 a  e  i
 c  e  e
 e

insert:
    O(k), where k is the lengh of the word being inserted
    either dictionary or list
    each letter is represented by a node in the three
    last letter contains bool
search():
    traverse tree
    if successful, return True, otherwise False
startsWith():
    same as search, except no True bool required


root = {'t': {'a' ... 'r': {...}}}

root = {'t': first_level}}
first_level = {'a': null, ..., 'r': {second_level}}  (may or may not include empty)
second_level = {'a': this_a_dict, 'e': this_e_dict, 'i': this_i_dict}
this_a_dict = ...


   a
 b   c
... ...

[None] * 26

      a
[ , null, null]
 |
[None,  ,  ]
      |   |


array solution:

O(n*k) time
where
n is the number of input operations
k is average word length

O(k*a) space
where
a is the alphabet size

dictionary:
O(k) space


'''


class Trie:
    """
    bool-list of bool-lists
    bool index: 0
    """

    def _to_index(self, char):
        ascii_offset = 96  # 97 - 1 for bool
        return ord(char) - ascii_offset

    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        pointer = self.root
        i = 0
        while i < len(word):
            char = word[i]
            next_index = self._to_index(char)
            if not pointer[next_index]:
                pointer[next_index] = [None] * 27
                pointer[next_index][0] = False
            pointer = pointer[next_index]
            i += 1
        pointer[0] = True

    def search(self, word: str) -> bool:
        pointer = self.root
        i = 0
        while i < len(word):
            char = word[i]
            next_index = self._to_index(char)
            if not pointer[next_index]:
                return False
            pointer = pointer[next_index]
            i += 1
        return pointer[0]

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        i = 0
        while i < len(prefix):
            char = prefix[i]
            next_index = self._to_index(char)
            if not pointer[next_index]:
                return False
            pointer = pointer[next_index]
            i += 1
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
