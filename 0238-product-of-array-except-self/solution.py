# we want 2 lists, the multiplication of everything to the left of it and the multiplication of everyuthing to the right
# mutltiply those 2 to get our answer
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        res = []
        for idx, n in enumerate(nums):
            
            res.append(cur)
            cur *= n
        cur = 1
        for idx in range(len(nums)-1, -1, -1):
            res[idx] = cur * res[idx]
            cur *= nums[idx]

        return res
        
