# before = [1, 1, 2, 6, 24]
# after = [1, 4, 12, 24, 24] -> [24, 12, 4, 1]
# [23, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1]
        for n in nums:
            before.append(before[-1] * n)
        after = [1]
        for n in nums[::-1]:
            after.append(after[-1] * n)
        after.reverse()
        after = after[1:]
        res = []
        for idx, n in enumerate(nums):
            res.append(before[idx] * after[idx])
        return res 
            
