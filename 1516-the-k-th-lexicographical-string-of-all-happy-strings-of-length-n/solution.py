class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        n_poss = 3 * 2**(n-1)
        if n_poss < k:
            return ""
        
        def solve(num):
            if num == 1:
                return ['a', 'b', 'c']
            res = []
            for sol in solve(num-1):
                if sol[-1] == 'a':
                    res.append(sol + 'b')
                    res.append(sol + 'c')
                elif sol[-1] == 'b':
                    res.append(sol + 'a')
                    res.append(sol + 'c')
                else:
                    res.append(sol + 'a')
                    res.append(sol + 'b')
            return res
        return solve(n)[k-1]
