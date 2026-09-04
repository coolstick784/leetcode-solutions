class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        from_start = 0
        from_end = 0
        from_middle = 0
        ends = 0
        cur = 0
        best = []
        for idx, n in enumerate(nums):
            cur += n
            from_start = max(from_start, cur)
            best.append(from_start)
        cur = 0
        for idx in range(len(nums)-1, -1, -1):
            n = nums[idx]
            cur += n
            from_end = max(from_end, cur)
            if idx > 0:
                ends = max(ends, best[idx-1] + from_end)


        cur = 0
        for idx, n in enumerate(nums):
            cur += n
            cur = max(cur, 0)
            from_middle = max(from_middle, cur)



        return max(ends, from_middle)
