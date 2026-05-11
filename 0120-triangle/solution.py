class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def min_sum(row, idx):

            if row >= len(triangle):
                return 0
            if idx < 0 or idx >= len(triangle[row]):
                return float('inf')
            val = triangle[row][idx]
            return min(val + min_sum(row+1, idx), val+min_sum(row+1, idx+1))
        return min_sum(0, 0)
