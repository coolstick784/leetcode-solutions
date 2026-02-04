from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()

            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:  # "/"
                stack.append(int(a / b))  # truncates toward 0

        return stack[-1]

