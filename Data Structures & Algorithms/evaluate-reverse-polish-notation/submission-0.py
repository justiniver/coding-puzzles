import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ('+', '-', '*', '/')

        i = 0
        stack = []
        while i < len(tokens):
            while i < len(tokens) and not (tokens[i] in ops):
                stack.append(int(tokens[i]))
                i += 1
            while i < len(tokens) and tokens[i] in ops:
                op = tokens[i]
                i += 1
                n = stack.pop()
                n2 = stack.pop()
                if op == '+':
                    n2 += n
                if op == '-':
                    n2 -= n
                if op == '*':
                    n2 *= n
                if op == '/':
                    n2 = math.trunc(n2 / n)
                stack.append(n2)    
        
        return stack[0]
        