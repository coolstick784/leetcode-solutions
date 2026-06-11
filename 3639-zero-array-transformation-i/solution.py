class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        sums = [0 for _ in nums]
        for start, end in queries:
            sums[start] += 1
            if end < len(sums) - 1:
                sums[end+1] -= 1
        cur = 0

        for idx, n in enumerate(nums):
            cur += sums[idx]
            if cur < n:
                return False
        return True
