# Initial Approach
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) + int(a))
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) * int(a))
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(math.trunc(int(b) / int(a)))
            else:
                stack.append(int(token))

        return stack[0]

# Using a hash
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda b , a: math.trunc(b / a),
        }

        for token in tokens:
            if token in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[token](b, a))
            else:
                stack.append(int(token))

        return stack[0]
