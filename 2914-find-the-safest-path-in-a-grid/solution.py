import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def closest(r, c):
            
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return float('inf')
            if grid[r][c] == 1:
                return 0


            return min(closest(r+1, c)+1, closest(r, c+1)+1)


        close = {}
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                close[(r, c)] = closest(r, c)
                close[(r,c)]= min(close[(r,c)], close.get((r-1,c), float('inf'))+1, close.get((r, c-1), float('inf'))+1)
        

        best = {} # (r, c) -> safe
        def explore(r, c, safe):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            safe = min(safe, close[(r, c)])
            if safe <= best.get((r, c), -float('inf')):
                return 
            best[(r, c)] = safe
            heapq.heappush(heap, (-safe, r, c))
        heap = [(-close[(0, 0)], 0, 0)]
        while heap:
            s, cr, cc = heapq.heappop(heap)
            
            s = -s
         
            if cr == len(grid) - 1 and cc == len(grid[0]) - 1:
                return s
            explore(cr+1, cc, s)
            explore(cr-1, cc, s)
            explore(cr, cc+1, s)
            explore(cr, cc-1, s)

