###############################################################################
# revised iterative solution
# time: O(n)
# space:
#   O(n) stack
#   O(n) auxiliary


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        lookup = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char in '({[':
                stack.append(char)
            elif len(stack) < 1:
                return False
            elif lookup[char] != stack.pop():
                return False

        if len(stack) > 0:
            return False

        return True


###############################################################################
# live iterative solution
# time: O(n)
# space:
#   O(n) stack
#   O(n) auxiliary

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        conv = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            elif stack and conv[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) > 0:
            return False
        return True