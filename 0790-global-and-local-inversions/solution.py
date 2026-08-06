# if n > nums[idx+1], nums[idx+2] must be n + 2, nums[idx+1] must be n - 1, and 
# n must be < n

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for idx, n in enumerate(nums[:-1]):
            if n > nums[idx+1]:

                if nums[idx+1] != n - 1:
                    return False
                if idx > 0 and nums[idx-1] >= n:
                    return False
        return True

