###############################################################################
# live solution
# O(n) time/space

'''

# todo: consider 2 pointers emulating stack

[-5, -10, /, /, /, /, -8]
       ^
                           ^

[-5, -10, /, /, /, -8]
          ^
                    ^

[-5, -10, /, /, /, -8, -2, 5, 4]
                              ^
                              ^

# empty stack
    # append
# non-empty stack
    # topmost negative
        # append
    # topmost positive
        # incoming positive
            # append
        # incoming negative
            # larger
                # pop
            # equal
                # pop
                # next
            # less than
                # next

'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()

        i = 0
        while i < len(asteroids):
            nxt = asteroids[i]
            # empty stack
            if len(stack) < 1:  # not stack
                stack.append(nxt)
            # negative topmost
            elif stack[-1] < 0:
                stack.append(nxt)
            # positive topmost
            elif nxt > 0:  # incoming positive
                stack.append(nxt)
            # positive topmost
            elif nxt < 0:  # incoming negative
                top = stack[-1]
                if -nxt >= top:
                    stack.pop()
                if -nxt > top:
                    continue
            i += 1

        return stack
