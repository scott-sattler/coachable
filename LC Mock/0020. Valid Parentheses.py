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