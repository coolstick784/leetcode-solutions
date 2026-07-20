class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        @lru_cache(None)
        def solve(x, y):
            nonlocal sx
            nonlocal sy
            
            if x == sx and y == sy:
                return True
            if x < sx or y < sy:
                return False
            if y > x:
                x, y = y, x
                sx, sy = sy, sx

            # go down until MAX(x is just above y, sx)
            mult = max(min((x-y) // y, (x-sx) // y), 1)
            return solve(x-y*mult, y)
        
  
        
        return solve(tx, ty)
