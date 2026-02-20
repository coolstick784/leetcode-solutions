class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for idx, n in enumerate(nums):
            if idx >= 3:
                dp[idx] = max(
                    dp[idx-2] + n,
                    dp[idx-3] + n
                )
            elif idx == 2:
                dp[idx] = dp[0] + n
            else:
                dp[idx] = n
        if len(nums) == 1:
            return nums[0]
        return max(dp[-1], dp[-2])
        
