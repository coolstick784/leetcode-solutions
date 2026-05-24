class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        heap = []
        for n, ct in ctr.items():   
            heapq.heappush(heap, (ct, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for ct, n in heap]
