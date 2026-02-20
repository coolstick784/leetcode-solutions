class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        rotten = {} # (2, 1): 2
        fresh = {} # (2, 1): 1
        for r in range(num_rows):
            for c in range(num_cols):
                cur_el = grid[r][c]
                if cur_el == 1:
                    fresh[(r, c)] = 1
                elif cur_el == 2:
                    rotten[(r, c)] = 2
        res = 0
        while rotten:
            new = {}



            for r, c in rotten:
                
                if fresh.get((r-1, c), 0) == 1:
                    new[(r-1, c)] = 2
                    fresh[(r-1, c)] = 0

                if fresh.get((r+1, c), 0) == 1:
                    new[(r+1, c)] = 2
                    fresh[(r+1, c)] = 0
                if fresh.get((r, c+1), 0) == 1:

                    new[(r, c+1)] = 2
       
                    fresh[(r, c+1)] = 0
                if fresh.get((r, c-1), 0) == 1:
                    
                    new[(r, c-1)] = 2
                    fresh[(r, c-1)] = 0
            res += 1

            rotten = new.copy()
        res -= 1
        res = max(0, res)
        if fresh and max(fresh.values()) == 1:
            return -1
        
        return res
        
