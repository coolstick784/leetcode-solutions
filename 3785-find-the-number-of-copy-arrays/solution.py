class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        @lru_cache(None)
        def solve(idx):
            mn = bounds[idx][0]
            mx = bounds[idx][1]
            if idx < len(original) - 1:
                diff = original[idx+1] - original[idx]
                nxt = solve(idx+1)

                mn = max(mn, nxt[0] - diff)
                mx = min(mx, nxt[1] - diff)
            
            if mn > mx:
                return (float('inf'), -float('inf'))
            return (mn, mx)




        res = solve(0)
        if res[0] == float('inf'):
            return 0
        return res[1] - res[0] + 1
