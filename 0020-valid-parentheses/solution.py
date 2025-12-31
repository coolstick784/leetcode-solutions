class Solution:
    def isValid(self, s: str) -> bool:
        matching_dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        stack = []
        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                matching_opening = matching_dict[ch]
                if len(stack) >= 1 and matching_opening == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
