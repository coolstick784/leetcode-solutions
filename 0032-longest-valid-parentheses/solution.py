class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        past_sol = []
        res = 0
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif stack:
                prev = stack.pop()
                val = idx - prev + 1
                
                while past_sol and past_sol[-1][0] >= prev - 1:
                    if past_sol[-1][0] == prev -1:
                        prev, prev_val = past_sol.pop()
                        val += prev_val
                    else:
                        past_sol.pop()
                past_sol.append((idx, val))
                res = max(res, val)
        return res
