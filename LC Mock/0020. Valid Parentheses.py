###############################################################################
# variation on iterative solution
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
            if char in lookup.values():
                stack.append(char)
            elif len(stack) < 1:
                return False
            elif lookup[char] != stack.pop():
                return False

        return len(stack) == 0


###############################################################################
# toy recursive solution
# time: O(n)
# space:
#   O(n) stack
#   O(n) call stack
#   O(n) auxiliary

class Solution:
    lookup = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    def isValid(self, s: str) -> bool:
        outer_stack = list()
        return self._isValid(0, outer_stack, s)

    def _isValid(self, i, stack, s):
        if i >= len(s):
            if stack:
                return False
            return True

        if s[i] in '({[':
            stack.append(s[i])
        elif not stack:
            return False
        # pop stack and copare to current char
        elif stack.pop() != self.lookup[s[i]]:
            return False

        return self._isValid(i + 1, stack, s)


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