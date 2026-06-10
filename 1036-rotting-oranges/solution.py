from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        
        num_fresh = 0
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                if el == 2:
                    q.append((r,c, 0))
                elif el == 1:
                    num_fresh += 1
        def explore(cr, cc, cur):
            nonlocal num_fresh
            if cr < 0 or cc < 0 or cr >= len(grid) or cc >= len(grid[0]) or grid[cr][cc] != 1:
                return 
            grid[cr][cc] = 2
            q.append((cr, cc, cur+1))
            num_fresh -= 1
        t = 0
        while q:
           
            r, c, t= q.popleft()
          
            explore(r-1, c, t)
            explore(r+1, c, t)
            explore(r, c-1, t)
            explore(r, c+1, t)



        if num_fresh:
            return -1
        return t
