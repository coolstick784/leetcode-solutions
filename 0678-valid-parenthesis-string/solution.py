class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        extra_popped = 0
        extra = 0
        for ch in s:
            if ch == "(":
                stack.append("(")
            elif stack and ch == ")":
                stack.pop()
            elif not stack and ch == ")":
                if extra:
                    extra -= 1
                elif extra_popped:
                    extra_popped -= 1
                    extra += 1
    
                else:
                    return False
            else:
                if stack:
                    stack.pop()
                    extra_popped += 1
                else:
                    extra += 1

        print("stack", stack)
        if not stack:
            return True
        return False
