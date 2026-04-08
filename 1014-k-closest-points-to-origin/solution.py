class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist = []
        for x, y in points:
            dist.append((-1*(x**2+y**2), [x, y]))

        for dist, point in dist:
     
            if len(heap) < k:
                heapq.heappush(heap, (dist, point))
            else:
                heapq.heappush(heap, (dist, point))
          
                heapq.heappop(heap)
     
        res = []
        for dist, point in heap:
            res.append(point)
        return res
