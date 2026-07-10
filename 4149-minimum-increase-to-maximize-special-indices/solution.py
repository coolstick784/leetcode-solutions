# 1, 2, 3
# 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5, 6
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2, 5, 7, 9
# 2, 4, 6, 8
# 3, 5, 7, 9
# 2, 4, 7, 9

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = 0
        mx = math.ceil(len(nums) /2) - 1
        for idx, n in enumerate(nums):
            if idx == 0 or idx == len(nums) - 1:
                continue
            left = len(nums) - idx
            num_before = idx
            cost = max(0, max(nums[idx-1], nums[idx+1]) - n + 1)
            if left % 2 == 0 and num_before % 2 == 0:
                dp[idx] = min(dp.get(idx-2, 0), dp.get(idx-3, 0)) + cost
            elif left % 2 == 1 and num_before % 2 == 1:
                dp[idx] = dp.get(idx-2, 0) + cost
            elif left % 2 == 1 and num_before % 2 == 0:
                dp[idx] = float('inf')
            elif left % 2 == 0 and num_before % 2 == 1:
                dp[idx] = dp.get(idx-2, 0) + cost
        print("dp", dp)
        if len(nums) % 2 == 1:
            return dp[len(nums) - 2]
        return min(dp[len(nums)-2], dp[len(nums)-3])

