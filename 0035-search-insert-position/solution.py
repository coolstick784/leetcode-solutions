class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1
        if target < nums[left]:
            return 0
        if target > nums[right]:
            return len(nums)
        while left < right - 1:
            

            med = (right + left) // 2
     
          
            if nums[med] == target:
                return med
            elif nums[med] > target:

                right = med
            else:

                left = med
        if nums[left] == target:
            return left
        return right
