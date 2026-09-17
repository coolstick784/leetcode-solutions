import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        n = 0
        for idx, a in enumerate(apples):
            d = days[idx]
            heapq.heappush(heap, (idx + d, a))
            while heap and (heap[0][0] <= idx or heap[0][1] <= 0):
                heapq.heappop(heap)
            if heap:
                d, a = heapq.heappop(heap)
                n += 1
                heapq.heappush(heap, (d, a-1))
                

        cur = len(days)
        while heap:
            d, a = heapq.heappop(heap)
            if d <= cur or a <= 0:
                continue
            n += 1
            cur += 1
            heapq.heappush(heap, (d, a-1))
        
        return n
