class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        heaps = {}
        for r, row in enumerate(nums):
            heaps[r] = []
            for c, el in enumerate(row):
                heapq.heappush(heaps[r], -el)
        n_cols = len(nums[0])
        res = 0
        for _ in range(n_cols):
            cur_max = 0
            for h in heaps:
                if not heaps[h]:
                    continue
                cur_max = max(cur_max, -heapq.heappop(heaps[h]))
            
            res += cur_max
        return res
