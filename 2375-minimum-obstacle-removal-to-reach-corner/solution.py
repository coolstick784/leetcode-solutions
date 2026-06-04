class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        best = {}
        heap = [(0, 0, 0)]
        def explore(cur, nr, nc):
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                return 
            add = 0
            if grid[nr][nc] == 1:
                add = 1
            if cur + add >= best.get((nr, nc), float('inf')):
                return
            best[(nr, nc)] = cur + add
            heapq.heappush(heap, (cur+add, nr, nc))
        
        while heap:
            cost, r, c = heapq.heappop(heap)
   
            if r == len(grid) -1 and c == len(grid[0]) - 1:
                return cost
            explore(cost, r+1, c)
            explore(cost, r-1, c)
            explore(cost, r, c+1)
            explore(cost, r, c-1)
        
