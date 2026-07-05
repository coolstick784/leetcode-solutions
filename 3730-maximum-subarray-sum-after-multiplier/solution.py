import math
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)

        if max(nums) <= 0:
            return math.ceil(max(nums) / k)
        left = 0
        right = 0
        cur = 0
        best = 0
        while right < len(nums):
            cur += nums[right] * k
            if cur <= 0:
                left = right + 1
                cur = 0
            else:
                best = max(best, cur)
            
            right += 1
        best_using = {}
        best_using_ending = {}
        best_not_using = {}
        for idx, n in enumerate(nums):
            best_using_before = best_using.get(idx-1, 0)
            best_using_ending_before = best_using_ending.get(idx-1, 0)
            best_not_using_before = best_not_using.get(idx-1, 0)
            
            best_using[idx] = max(best_using_before+n, best_using_ending_before+n, 0)
            if n > 0:
                add = n //k
            else:
                add = math.ceil(n/k)
            best_using_ending[idx] = max(best_using_ending_before + add, best_not_using_before+add, 0)
            best_not_using[idx] = max(0, best_not_using_before + n)
     
            best = max(best, best_using[idx], best_using_ending[idx], best_not_using[idx])
        return best
            
        


