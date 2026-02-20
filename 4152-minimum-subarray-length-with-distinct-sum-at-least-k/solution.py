class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0
        res = 2**31-1
        ctr = {nums[0]:1}
        cur_sum = nums[0]
        while left < len(nums) and right < len(nums):

            if cur_sum >= k:

                res = min(res, right-left+1)
                left += 1
                ctr[nums[left-1]] = ctr.get(nums[left-1], 1) - 1
                if ctr[nums[left-1]] == 0:
                    cur_sum -= nums[left-1]
            else:
                right += 1
                if right < len(nums):
                    ctr[nums[right]] = ctr.get(nums[right], 0) + 1
                if right < len(nums) and ctr[nums[right]] == 1:
                    cur_sum += nums[right]
        if res == 2**31-1:
            return -1
        return res

        
