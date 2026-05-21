# 3, 2, 1
# 3, 2
# 3, 5
# 5, 6


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            while len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
