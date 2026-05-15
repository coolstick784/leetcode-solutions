# 1 -> [1, 2] 2-> [2, 3] 3 -> [3, 4]

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @lru_cache(None)
        def solve(row, glass):
            if row == 0 and glass == 0:
                return poured
            if glass == 0:
                return max(0, (solve(row-1, glass)-1)/2)
            if glass == row:
                return max(0, (solve(row-1, glass-1)-1)/2)
            return max(0, (solve(row-1, glass)-1)/2) + max(0, (solve(row-1, glass-1)-1)/2)
            
        

        return min(1, solve(query_row, query_glass))
