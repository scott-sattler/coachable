from __future__ import annotations

import unittest


class StringBuilder:
    # Optional argument for a string and a capacity (optional).
    # Otherwise defaults to an empty string and has no limit on characters.
    def __init__(self, string="", capacity=None):
        if capacity is None:
            capacity = float('inf')
        if capacity < len(string):
            raise Exception()

        self.c_string = [i for i in string]
        self.capacity = capacity

    # Returns the string that is built.
    def __str__(self) -> str:
        return ''.join(self.c_string)

    # Appends s to the array in O(len(s)) at the end.
    # Should raise an exception if over capacity.
    def append(self, s: str) -> None:
        if len(self.c_string) + len(s) <= self.capacity:
            self.c_string += list(s)

    # Returns the length of the string.
    def size(self) -> int:
        return len(self.c_string)

    # Returns the character at location index.
    def char_at(self, index: int) -> str:
        return self.c_string[index]

    # Deletes characters between start (inclusive) and end (exclusive).
    # Should raise an exception if start, end are out of bounds.
    def delete(self, start: int, end=None) -> None:
        # self.c_string = self.c_string[: start - 1] + self.c_string[end + 1:]
        if self.bounds_test(start, end):
            del self.c_string[start:end]

    # Returns a substring from indices start to end.
    # Should raise an exception if start, end are out of bounds.
    def substring(self, start: int, end=None) -> str:
        # mirroring Python behavior
        # specification was not provided
        if end is None:
            end = len(self.c_string)

        if self.bounds_test(start, end):
            return ''.join(self.c_string[start:end])

    # Reverses the current string
    def reverse(self) -> str:
        self.c_string = self.c_string[::-1]
        return ''.join(self.c_string)

    # Replaces all occurrences of “old” with “new”
    def replace(self, old: str, new: str):
        sentinel = False
        for i in range(len(self.c_string)):
            if self.c_string[i] == old:
                self.c_string[i] = new
                sentinel = True
        if not sentinel:
            raise Exception()
        # self.c_string = [i if i != old else new for i in self.c_string]  fails on not found

    def bounds_test(self, start, stop) -> bool:
        if not isinstance(start, int) or not isinstance(stop, int):
            raise Exception()

        # inequality always returns bool -> bool > int
        # can override for expected behavior in x > y > z
        # https://stackoverflow.com/a/12675160
        if 0 > start or start > len(self.c_string):
            raise Exception()
        if 0 > stop or stop > len(self.c_string):
            raise Exception()
        if start > stop:
            raise Exception()

        return True


# from string_builder import StringBuilder
class TestStringBuilder(unittest.TestCase):

    def test_string_builder_simple(self):
        string = StringBuilder()
        self.assertEqual(str(string), "")

        string = StringBuilder("Hello World")
        self.assertEqual(str(string), "Hello World")

        with self.assertRaises(Exception):
            string = StringBuilder("Hello World", 5)

        self.assertEqual(string.size(), 11)
        self.assertEqual(string.char_at(2), 'l')

        self.assertEqual(string.substring(0, 5), 'Hello')
        self.assertEqual(string.substring(6), 'World')

        string.append(". This is my first program")
        self.assertEqual(string.size(), 37)
        self.assertEqual(string.char_at(36), 'm')

        with self.assertRaises(Exception):
            string.substring(100)
        with self.assertRaises(Exception):
            string.substring(1, 0)
        with self.assertRaises(Exception):
            string.substring(-1)
        with self.assertRaises(Exception):
            string.substring(0, 38)

    def test_string_builder_replace(self):
        string = StringBuilder("abc", 10)
        string.replace("a", "dc")
        self.assertEqual(str(string), "dcbc")

        string = StringBuilder("aaa", 11)
        string.replace("a", "aa")
        self.assertEqual(str(string), "aaaaaa")

        with self.assertRaises(Exception):
            string.replace("a", "aa")

    def test_string_builder_reverse(self):
        string = StringBuilder("Hello World", 20)
        self.assertEqual(str(string.reverse()), "dlroW olleH")
        self.assertEqual(str(string), "dlroW olleH")
        self.assertEqual(string.char_at(1), 'l')
        self.assertEqual(string.size(), 11)

    def test_string_builder_delete(self):
        string = StringBuilder("Hello World", 20)
        with self.assertRaises(Exception):
            string.delete(-1)
        with self.assertRaises(Exception):
            string.delete(11)
        with self.assertRaises(Exception):
            string.delete(2, 0)
        with self.assertRaises(Exception):
            string.delete(0, 12)
        string.delete(0, 6)
        self.assertEqual(string.size(), 5)
        self.assertEqual(str(string), "World")

    def test_append_performance(self):
        string = StringBuilder("", 10000)
        for i in range(10000):
            string.append("a")
        self.assertEqual(string.size(), 10000)

