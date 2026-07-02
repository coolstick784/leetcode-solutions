import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        best = {}
        heap = [(health-grid[0][0], 0, 0)]
        if health-grid[0][0] <= 0:
            return False
        def explore(cur, r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 
            if grid[r][c] == 1:
                cur -= 1
            if cur <= 0:
                return
            if cur <= best.get((r, c), -float('inf')):
                return
            best[(r, c)] = cur
            heapq.heappush(heap, (cur, r, c))
            
        while heap:
            cur, r, c = heapq.heappop(heap)
            if r == len(grid) -1 and c == len(grid[0]) - 1:
                return True
            explore(cur, r+1, c)
            explore(cur, r-1, c)
            explore(cur, r, c+1)
            explore(cur, r, c-1)
        return False
