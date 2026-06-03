# for each cell, ask what number we need (min) to access it
# then, just count

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        mn = [[float('inf') for _ in grid[0]] for _ in grid] 
        heap = [(grid[0][0] + 1,0, 0) ] # min, row, col
        mx = max(queries)
        mn[0][0] = grid[0][0] + 1
        def explore(cost, r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            cur_cost = max(cost, grid[r][c]+1)
            if cur_cost >= mn[r][c]:
                return  
            
            mn[r][c] = cur_cost
            heapq.heappush(heap, (cur_cost, r, c))
        while heap:
            cost, cr, cc = heapq.heappop(heap)
            explore(cost, cr+1, cc)
            explore(cost, cr-1, cc)
            explore(cost, cr, cc+1)
            explore(cost, cr, cc-1)
        
        mn_costs = {}
        for r, row in enumerate(mn):
            for c, el in enumerate(row):
                mn_costs[el] = mn_costs.get(el, 0) + 1

        dp = {}
        cur = 0
        for n in range(mx+1):
            dp[n] = dp.get(n-1, 0) + mn_costs.get(n, 0)
        res = []
        for q in queries:
            res.append(dp.get(q, 0))
        return res


