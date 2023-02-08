"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false


Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.

"""


class Solution:
    # second attempt: previously solved
    # time complexity: O(n)
    # space complexity (auxiliary): O(n) (O(n))
    def isValid(self, s: str) -> bool:  # noqa: naming convention
        stack = list()
        lookup = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) < 1 or stack.pop() != lookup[char]:
                    return False

        return True if len(stack) == 0 else False


input_strs = [
    "(){}[]",   # T
    "({[)}]",   # F
    "]",        # F
    "}{",       # F
    "((()))",   # T
    "(()[)]",   # F


]

for each in input_strs:
    print(each, Solution().isValid(each))
