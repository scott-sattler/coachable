###############################################################################
# improved solution
# O(n) time/space

'''

# preserve only valid parenthesis pairs

if open
    add index to stack
if close
    invalidate if stack empty
    pop from stack

invalidate remaining indices from stack

'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)  # O(n) time/space
        stack = list()

        # invalidate excess close
        # create stack of opens
        for i in range(len(s)):
            if s[i] not in '()':
                continue

            if s[i] == '(':
                stack.append(i)
            elif len(stack) > 0:  # s[i] == ')':
                stack.pop()
            else:  # empty stack
                s[i] = ''

        # only invalid opens remain
        # invalidate excess opens
        for i in stack:
            s[i] = ''

        return ''.join(s)


###############################################################################
# first attempt
# O(n) time/space


'''

# preserve only valid parenthesis pairs

)))(a)bb)))))))ccc(((aa

1st pass
disregard close at 0 count
increment count for open
decrement count for close

[(a)bbccc(((aa] + 3

2nd pass
reset count to 0
disregard open at 0
increment count for close
decrement count for open

)))(a)bb)))))))ccc(((aa

[(a)bbccc(((aa] + 3


)))(o)o(a)bb))))ccc(((aa(b)c)d)d
                   ^

[(o)o(a)bbccc(((aa(b)c)d)d] +1
[(o)o(a)bbccc((aa(b)c)d)d]


convert to list
if below 0, turn to string


"((((a)(b(c)((d))"

'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)  # O(n) time/sapce

        n = len(s)
        char = '('
        for each_range in (range(n), range(n - 1, -1, -1)):
            count = 0
            for i in each_range:
                if s[i] not in '()':
                    continue

                if s[i] == char:
                    count += 1
                elif count > 0:
                    count -= 1
                else:  # ')' with count of 0
                    s[i] = ''
            char = ')'

        return ''.join(s)
