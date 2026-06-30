
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for idx, ch in enumerate(s):
            if not stack:
                stack.append(ch)
            elif ord(ch) == ord(stack[-1]) + 1 or (ch == 'a' and stack[-1] == 'z') or ord(ch) == ord(stack[-1]) -1 or (ch == 'z' and stack[-1] == 'a'):
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

