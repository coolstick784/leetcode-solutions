# can do x->y, z->x, z->y, y->x, y->z
# cannot do x->z, z->b
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @lru_cache(None)
        def solve(s1, s2, s3, prev):
            out = 0
            if s1 < 0 or s2 < 0 or s3 < 0:
                return -1
            if prev != 2 and prev != 3:
                out = max(out, 1 + solve(s1, s2-1, s3, 2))
            if prev != 1:
                out = max(out, 1 + solve(s1-1, s2, s3, 1))
                out = max(out, 1 + solve(s1, s2, s3-1, 3))
                
            return out
        return solve(x, y, z, 0) * 2
