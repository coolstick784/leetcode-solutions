class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        start_2 = nums[1:]
        for idx, n in enumerate(start_2):
            if idx == 2:
                dp[idx] = dp[0] + n
            elif idx < 2:
                dp[idx] = n
            else:
                dp[idx] = max(
                    dp[idx-2] + n,
                    dp[idx-3] + n
                )
        
        s2_max = max(dp[-1], dp[-2])
        end_2 = nums[:-1]
        for idx, n in enumerate(end_2):
            if idx == 2:
                dp[idx] = dp[0] + n
            elif idx < 2:
                dp[idx] = n
            else:
                dp[idx] = max(
                    dp[idx-2] + n,
                    dp[idx-3] + n
                )
        
        
        e2_max = max(dp[-2], dp[-3])
        return max(s2_max, e2_max)
