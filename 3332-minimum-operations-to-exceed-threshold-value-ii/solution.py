class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for n in nums:
            heapq.heappush(heap, n)
        while heap[0] < k:
            res += 1
            mn1 = heapq.heappop(heap)
            mn2 = heapq.heappop(heap)
            heapq.heappush(heap, min(mn1, mn2) * 2 + max(mn1, mn2))

        return res
