import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for idx, n in enumerate(nums):
            left = idx - k + 1
 

            heapq.heappush(heap, (-n, idx))
            while heap[0][1] < left:
                heapq.heappop(heap)
            
            if len(heap) >= k:

                res.append(-heap[0][0])
        return res
            
