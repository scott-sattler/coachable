"""
844. Backspace String Compare
Easy

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".


Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?

"""


class Solution:
    # first attempt:
    # time complexity:
    # space complexity (auxiliary):
    def backspaceCompare(self, s: str, t: str) -> bool:  # noqa: naming convention
        pass


test_cases = [
    [
        "a",
        "b"
    ],  # False
    [
        "ab#c",
        "ad#c"
    ],  # True
    [
        "ab##",
        "c#d#"
    ],  # True
    [
        "a#c",
        "b"
    ],  # False

]

for s, t in test_cases:
    print((s, t), Solution().backspaceCompare(s, t))
