class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ctr = len(grid[0])
        res = 0
        
        while ctr > 0:
            cur_maxes = [0 for _ in range(len(grid))]
            for idx, r in enumerate(grid):
                cur_max = max(r)
                cur_maxes.append(cur_max)
                grid[idx].remove(cur_max)
            res += max(cur_maxes)
            ctr -= 1
        return res
            
            
        
