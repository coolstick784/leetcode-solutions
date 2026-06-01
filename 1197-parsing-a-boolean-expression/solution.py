class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        rev_stack = deque()
        mp = {}
        for idx, ch in enumerate(expression):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                mp[stack.pop()] = idx

        def do_op(op, arr):
      
            if op == "|":
                return [sum(arr) > 0]
            if op == "&":
                return [sum(arr) == len(arr)]
            if op == "!":
                return [not arr[0]]

        @lru_cache(None)
        def solve(start, end):
            
            cur = []
            op = None
            print("start", start, "end", end)
            if start > end:
                return []
            print("start", start, "end", end, "ch", expression[start])
            if expression[start] in ['t', 'f']:
                if expression[start] == 't':
                    return [1] + solve(start+1, end)
                return [0] + solve(start+1, end)
            if expression[start] in ['!', '&', '|']:
                op = expression[start]
                first = start+1
                last = mp[first]
                return do_op(op, solve(first, last)) + solve(last+1, end)
            return solve(start+1, end)



        return solve(0, len(expression) - 1)[0] == 1
