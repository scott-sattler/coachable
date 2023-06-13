from __future__ import annotations


# additional constraints:
#   indexing constrained to only positive values

class StringBuilder:
    # Optional argument for a string and a capacity (optional).
    # Otherwise defaults to an empty string and has no limit on characters.
    def __init__(self, string="", capacity=None):
        self.str_list: list = [''] * capacity if capacity is not None else
        self.char_len: int = 0
        self.capacity: None | int = capacity

        self.append(string)

        if (self.capacity is not None) and (len(string) < self.capacity):
            n = capacity - len(string)
            for i in range(n):
                self.str_list.append('')

    # Returns the string that is built.
    def __str__(self) -> str:
        return ''.join(self.str_list)

    # Appends s to the array in O(len(s)) at the end.
    # Should raise an exception if over capacity.
    def append(self, s: str) -> None:
        if (self.capacity is not None) and (len(s) + self.char_len <= self.capacity):
            k = max(self.char_len - 1, 0)
            for i, char in enumerate(s):
                self.str_list[i + k] = s[i]
                self.char_len += 1
        else:
            raise Exception(f'Resulting string would exceed string capacity of {self.capacity}.')

    # Returns the length of the string.
    def size(self) -> int:
        return self.char_len

    # Returns the character at location index.
    def char_at(self, index: int) -> str:
        # index is within string size
        if -1 < index < self.char_len:
            return self.str_list[index]

        raise IndexError

    # Deletes characters between start (inclusive) and end (exclusive).
    # Should raise an exception if start, end are out of bounds.
    def delete(self, start: int, end: int | None = None) -> None:
        if end is None:
            end = self.char_len
        if self._boundary_check(start, end):
            self.str_list = self.str_list[:max(start - 1, 0)] + self.str_list[end:]
            self.char_len -= (end - start)
            for null in range(end - start):
                self.str_list.append('')
        else:
            raise Exception("Boundary error.")

    # Returns a substring from indices start (inclusive) to end (inclusive).
    # Should raise an exception if start, end are out of bounds.
    def substring(self, start: int, end=None) -> str:
        if self._boundary_check(start, end):
            return self.str_list[start:end + 1]
        else:
            raise Exception("Boundary error.")

    # Reverses the current string
    def reverse(self) -> str:
        return self.str_list[:self.char_len:-1] + self.str_list[self.char_len:]

    # Replaces all occurrences of “old” with “new”
    def replace(self, old: str, new: str) -> None:
        for i in range(self.char_len):
            if self.str_list[i] == old:
                self.str_list[i] = new
                self.char_len += (len(new) - len(old))
        # addresses bad input
        str_list_copy = self.str_list.__str__()
        self.delete(0)
        self.append(str_list_copy)

    # check and convert boundary
    def _boundary_check(self, start: int, end: int) -> bool:

        lower = -1 < start < end
        upper = start < end <= self.char_len

        return lower and upper

    # Extends capacity
    def extend(self, new_capacity):
        # todo: account for None data type
        # if new_capacity > self.capacity:
        #   self.capacity = new_capacity
        # else:
        #   raise Exception('New capacity must be greater than the existing capacity.')
        raise NotImplementedError


# string = StringBuilder("Hello World", 20)
# string.delete(0, 6)
# print(string.str_list)
# out = str(string)
# print(out)


string = StringBuilder("abc", 10)
string.replace("a", "dc")
print(str(string) == "dcbc")

#
# # from __future__ import annotations  # noqa
#
# import unittest  # noqa
# # from string_builder import StringBuilder
#
#
# class TestStringBuilder(unittest.TestCase):
#
#     def test_string_builder_simple(self):
#         string = StringBuilder()
#         self.assertEqual(str(string), "")
#
#         string = StringBuilder("Hello World")
#         self.assertEqual(str(string), "Hello World")
#
#         with self.assertRaises(Exception):
#             string = StringBuilder("Hello World", 5)
#
#         self.assertEqual(string.size(), 11)
#         self.assertEqual(string.char_at(2), 'l')
#
#         self.assertEqual(string.substring(0, 5), 'Hello')
#         self.assertEqual(string.substring(6), 'World')
#
#         string.append(". This is my first program")
#         self.assertEqual(string.size(), 37)
#         self.assertEqual(string.char_at(36), 'm')
#
#         with self.assertRaises(Exception):
#             string.substring(100)
#         with self.assertRaises(Exception):
#             string.substring(1, 0)
#         with self.assertRaises(Exception):
#             string.substring(-1)
#         with self.assertRaises(Exception):
#             string.substring(0, 38)
#
#     def test_string_builder_replace(self):
#         string = StringBuilder("abc", 10)
#         string.replace("a", "dc")
#         self.assertEqual(str(string), "dcbc")
#
#         string = StringBuilder("aaa", 11)
#         string.replace("a", "aa")
#         self.assertEqual(str(string), "aaaaaa")
#
#         with self.assertRaises(Exception):
#             string.replace("a", "aa")
#
#     def test_string_builder_reverse(self):
#         string = StringBuilder("Hello World", 20)
#         self.assertEqual(str(string.reverse()), "dlroW olleH")
#         self.assertEqual(str(string), "dlroW olleH")
#         self.assertEqual(string.char_at(1), 'l')
#         self.assertEqual(string.size(), 11)
#
#     def test_string_builder_delete(self):
#         string = StringBuilder("Hello World", 20)
#         with self.assertRaises(Exception):
#             string.delete(-1)
#         with self.assertRaises(Exception):
#             string.delete(11)
#         with self.assertRaises(Exception):
#             string.delete(2, 0)
#         with self.assertRaises(Exception):
#             string.delete(0, 12)
#         string.delete(0, 6)
#         self.assertEqual(string.size(), 5)
#         self.assertEqual(str(string), "World")
#
#     def test_append_performance(self):
#         string = StringBuilder("", 10000)
#         for i in range(10000):
#             string.append("a")
#         self.assertEqual(string.size(), 10000)
#
