class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        heap = []
        heap.append((0, 0, 0))

        best = {} # (r, c): time
        best[(0, 0)] = 0
        def explore(t, r,c):
            if r < 0 or c < 0 or r >= len(moveTime) or c >= len(moveTime[0]):
                return
            t = max(t, moveTime[r][c]) + 1
            if t >= best.get((r, c), float('inf')):
                return
            best[(r, c)] = t
            
            heapq.heappush(heap, (t, r, c))
            
            
        while heap:
            t, r, c = heapq.heappop(heap)
           
            if r == len(moveTime) - 1 and c== len(moveTime[0]) - 1:
                return t
            explore(t, r-1, c)
            explore(t, r+1, c)
            explore(t, r, c+1)
            explore(t, r, c-1)
        

