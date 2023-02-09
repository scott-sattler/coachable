"""
844. Backspace String Compare
Easy

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
backspace character.

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
    # second attempt: followup O(1) auxiliary
    # time complexity:
    # space complexity (auxiliary):
    def backspaceCompare(self, s: str, t: str) -> bool:  # noqa: naming convention
        raise NotImplemented

    # first attempt:
    # time complexity: O(2s + 2t) -> O(s + t)
    # space complexity (auxiliary): O(2s + 2t) -> O(s + t) auxiliary
    def first_attempt_backspaceCompare(self, s: str, t: str) -> bool:  # noqa: naming convention
        stack_s = list()
        stack_t = list()

        # construct backspaced strings (stacks)
        for char in s:
            if char != "#":
                stack_s.append(char)
            elif len(stack_s) > 0:
                stack_s.pop()

        for char in t:
            if char != "#":
                stack_t.append(char)
            elif len(stack_t) > 0:
                stack_t.pop()

        return True if stack_s == stack_t else False


test_cases = [
    # # included
    # [
    #     "ab#c",
    #     "ad#c",
    #     True
    # ],
    [
        "ab##",
        "c#d#",
        True
    ],
    [
        "a#c",
        "b",
        False
    ],

    # additional
    [
        "a",
        "b",
        False
    ],
    [
        "a#c######",
        "b#",
        True
    ],

    # failed
    [
        "bxj##tw",
        "bxj###tw",
        False
    ],
    [
        "ab##",
        "c#d#",
        True
    ],

]

print("(s, t), ans, Solution().backspaceCompare(s, t)")
for s, t, ans in test_cases:
    print((s, t), ans, Solution().backspaceCompare(s, t))
