class Solution(object):
    def search(self, nums, target, idx = 0):
        mid = len(nums) // 2

        
        if target == nums[mid]:
            return idx+mid
        elif len(nums) == 1:
            return -1
        elif target > nums[mid]:
            return self.search(nums[mid:], target, idx+mid)
        else:
            return self.search(nums[:mid], target, idx)
        
