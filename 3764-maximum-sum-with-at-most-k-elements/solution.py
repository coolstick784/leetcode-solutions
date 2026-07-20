import heapq
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        ctr ={}
        for r, row in enumerate(grid):
            for c, el in enumerate(row):
                heapq.heappush(heap, (-el, r))
        res = 0
        total = 0 
        if k == 0:
            return 0
        while heap:
            val, r = heapq.heappop(heap)
            val = -val
            if ctr.get(r, 0) < limits[r]:
                ctr[r] = ctr.get(r, 0) + 1
                res += val
                total += 1
            if total == k:
                return res
        return res
