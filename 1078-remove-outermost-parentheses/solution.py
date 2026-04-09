# we can create a stack
# if there is a () in a row, add that
# otherwise, add the open parentheses to a stack
# if it's an open parenthesis, and there already exists a stack, we want to add it and also add it to the stack
# if it's an open parenthesis, and there doesn't exist a stack, and the next char is not a closed parenthesis, then we want to add it to the stack but not our resolution
# if it's closed, and len(stack) > 1, add it and pop the stack
# if it's 1, just pop the stack
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        idx = 0
        res = ""
        stack = []
        while idx < len(s):


            if s[idx] == "(":
                if not stack:
                    stack.append("(")
                else:
                    stack.append("(")
                    res += "("
            else:
                stack.pop()
                if stack:
                    res += ")"
            idx += 1
        return res
        
