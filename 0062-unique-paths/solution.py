class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def search(row, col):
            if row == m-1 and col == n-1:
                return 1
            if row >=m or col >= n:
                return 0
           

            return  search(row+1, col) +  search(row, col+1)
        return search(0, 0)
        
