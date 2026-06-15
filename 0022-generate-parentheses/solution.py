class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solve(left, stack):
            if left < 0 or stack < 0 or (left <= 0 and stack <= 0):
                return []
            
            if left == 0:
                return [")" * stack]
            if left == 1 and stack == 0:
                return ["()"]
            out = []
            if stack:
                for sol in solve(left, stack-1):
                    out.append(")" + sol)
            if left:
                for sol in solve(left-1, stack+1):
                    out.append("(" + sol)
            
            return list(set(out))

        
        return solve(n, 0)
