# for each n between min and max, inclusive
# we want to keep track of our cost, left, and right
# as we move forward, our cost is (cost previous) + (num previous)
# while cost > k, move left 1
# while right + 1 equals n, move right 1
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        nums.sort()
        cost = 0
        left = 0
        right = -1
        res = 1
        for n in range(min_val, max_val + 1):
            cost += right - left+1
            while cost > k:
                cost -= (n-nums[left])
                left += 1
            while right+1 < len(nums) and nums[right+1] == n:
                right += 1

            res = max(res, (right-left+1))

        return res
