'''

2 1 + 3 *
^
vals = 2 1
oper = +

(2 + 1) * 3


3 2 6 4 5 - - - -

edge cases:


'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = list()

        for token in tokens:
            if token not in '+-*/':
                vals.append(int(token))
                continue

            right_val = vals.pop()
            left_val = vals.pop()

            if token == "+":
                result = left_val + right_val
            if token == "-":
                result = left_val - right_val
            if token == "*":
                result = left_val * right_val
            if token == "/":
                result = int(left_val / right_val)

            vals.append(result)

        return vals[0]
