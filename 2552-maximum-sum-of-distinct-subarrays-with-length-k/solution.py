from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        cur_sum = 0
        best = 0

        for right, x in enumerate(nums):
            cur_sum += x
            count[x] = count.get(x, 0) + 1

            # make all elements unique
            while count[x] > 1:
                y = nums[left]
                count[y] -= 1
                cur_sum -= y
                left += 1

            # keep window size at most k
            while right - left + 1 > k:
                y = nums[left]
                count[y] -= 1
                cur_sum -= y
                left += 1

            # if size is exactly k, it's unique by construction
            if right - left + 1 == k:
                best = max(best, cur_sum)

        return best

