import heapq
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        heap = [(0, 0, 0, 0, 1)] # cost, first cell, second cell
        best = {(0, 0, 0, 1): 0}

        def explore(cur, r1, c1, r2, c2, move = False):
            if r1 >= len(grid) or c1 >= len(grid[0]) or r2 >= len(grid) or c2 >= len(grid[0]) or r1 < 0 or c1 < 0 or c2 < 0 or r2 < 0:
                return
            if grid[r1][c1] == 1 or grid[r2][c2] == 1 or (move and grid[r1+1][c1+1] == 1):
                return
            if best.get((r1, c1, r2, c2), float('inf')) <= cur:
                return
            best[(r1, c1, r2, c2)] = cur
            heapq.heappush(heap, (cur, r1, c1,r2,c2))
    
        while heap:
    
            cost, r1, c1, r2, c2 = heapq.heappop(heap)
           
            if r1 == len(grid) - 1 and c1 == len(grid[0]) - 2 and r2 == len(grid) - 1 and c2 == len(grid[0]) - 1:
                return cost
            explore(cost+1, r1, c1+1, r2, c2+1)
            explore(cost+1, r1+1, c1, r2+1, c2)
            if c2 == c1 + 1:
                explore(cost+1, r1, c1, r1+1, c1, True)
            else:
                explore(cost+1, r1, c1, r1, c1+1, True)
        return -1
