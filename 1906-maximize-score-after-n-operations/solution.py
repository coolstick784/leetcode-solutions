class Solution:
    def maxScore(self, nums: List[int]) -> int:
        


        @lru_cache(None)
        def solve(n, cur):
            if not cur:
                return 0
            out = 0
            cur = list(cur)
            
            for idx, n1 in enumerate(cur):
                for idx2, n2 in enumerate(cur[idx+1:]):
                    new = cur.copy()
                
                    g = gcd(min(n1, n2), max(n1, n2))
                    new.remove(n1)
                    new.remove(n2)
                    out = max(out, n*g + solve(n+1, tuple(sorted(new))))
            return out

            
            

        ns = tuple(sorted(nums))
        return solve(1, ns)
