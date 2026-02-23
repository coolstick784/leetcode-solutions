class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[None for _ in range(n)] for _ in range(n)]


        for r in range(n):
            for c in range(n):
                poss = 8
                if (r-1) < 0 or (c+2) > n - 1:
                    poss -= 1
                if (r+1) > n - 1 or (c+2) > n - 1:
                    poss -= 1
                if (r-2) < 0 or (c+1) > n - 1:
                    poss -= 1
                if (r+2) > n - 1 or (c+1) > n - 1:
                    poss -= 1
                if (r+2) > n-1 or (c-1) < 0:
                    poss -= 1
                if (r-2) < 0 or (c-1) < 0:
                    poss -= 1
                if (r-1) < 0 or (c-2) < 0:
                    poss -= 1
                if (r+1) > n - 1 or (c-2) < 0:
                    poss -= 1       
                dp[r][c] = poss/8
            
        @lru_cache(None)
        def getProbabilites(cur_k, cur_pos):
            r = cur_pos[0]
            c = cur_pos[1]
            if cur_k == 0:
                return 1
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if cur_k == 1:
                return dp[r][c]
            return (getProbabilites(cur_k-1, (r-1, c+2)) * 0.125 + 
            getProbabilites(cur_k-1, (r-1, c-2)) * 0.125 + 
            getProbabilites(cur_k-1, (r+1, c+2)) * 0.125 + 
            getProbabilites(cur_k-1, (r+1, c-2)) * 0.125 + 
            getProbabilites(cur_k-1, (r-2, c-1)) * 0.125 + 
            getProbabilites(cur_k-1, (r-2, c+1)) * 0.125 + 
            getProbabilites(cur_k-1, (r+2, c-1)) * 0.125 + 
            getProbabilites(cur_k-1, (r+2, c+1)) * 0.125)
        return getProbabilites(k, (row, column))

        
