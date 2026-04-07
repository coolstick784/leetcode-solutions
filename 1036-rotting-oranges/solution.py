class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start with each rotten orange
        # then, for each rotten orange, we want a new list of rotten oranges that were not rotten previously
        # for those oranges, they are set with minute 1
        # then for those oranges, that's minute two, and we keep going until there are no more fresh oranges to rot
        
        rotten = set()
        rot_from = set()
        new_rot_from = set()
        fresh = set()
        
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 2:
                    rotten.add((r, c))
                if el == 1:
                    fresh.add((r, c))
                    
        if not rotten and not fresh:
            return 0
     
                    
        def rot(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in rotten or grid[row][col] != 1:
                return
            grid[row][col] == 2
            new_rot_from.add((row, col))
            
            
        rot_from = rotten.copy()
        
        minutes = -1
        while rot_from:
      
            for r, c in rot_from:
                rot(r-1, c)
                rot(r+1, c)
                rot(r, c-1)
                rot(r, c+1)
            rotten = rotten.union(new_rot_from)
            rot_from = new_rot_from.copy()
            new_rot_from = set()
           
            minutes += 1
       
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 1 and (r, c) not in rotten:
                    return -1
        return minutes
