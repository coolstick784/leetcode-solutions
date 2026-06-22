import heapq
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = float('inf')
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            res = min(res, n - nums[idx-1])
        return res
