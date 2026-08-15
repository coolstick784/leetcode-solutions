import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for idx, n in enumerate(nums):
            heapq.heappush(heap, -n)
        res = 0
        for _ in range(k):
            val = -heapq.heappop(heap)
            res += val 
            heapq.heappush(heap, -math.ceil(val/3))
        return res
