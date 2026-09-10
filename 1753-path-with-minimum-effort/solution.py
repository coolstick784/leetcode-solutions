class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        best = {}
        heap = [(0, 0, 0)] # (cost, r, c)
        rg = len(heights) - 1
        cg = len(heights[0]) - 1
        best[(0, 0)] = 0
        def explore(cur, cr, cc, prev):
            if cr < 0 or cc < 0 or cr >= len(heights) or cc >= len(heights[0]):
                return 
            p = max(cur, abs(heights[cr][cc] - prev))
            if p >= best.get((cr, cc), float('inf')):
                return 
            best[(cr, cc)] = p
            heapq.heappush(heap, (p, cr, cc))
        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == rg and c == cg:
                return cost
            el = heights[r][c]
            explore(cost, r-1, c, el)
            explore(cost, r, c-1, el)
            explore(cost, r+1, c, el)
            explore(cost, r, c+1, el)
