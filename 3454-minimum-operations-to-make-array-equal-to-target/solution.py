class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = 0
        diff_left = 0
        diff_right = 0
        while left <= right:
            if nums[left] <= target[left] and nums[left] + max(diff_left, 0) >= target[left]:

                diff_left = target[left] - nums[left]
            elif nums[left] < target[left] and nums[left] + diff_left < target[left]:
                res += target[left] - (nums[left] + max(diff_left, 0))
                diff_left = target[left] - nums[left]
                

            elif nums[left] > target[left] and nums[left] + diff_left <= target[left]:
                diff_left = target[left] - nums[left]
            else:
                res += nums[left] + min(diff_left, 0) - target[left]
                diff_left = target[left] - nums[left]
                

            # nums[left] = target[left]
            # if nums[right] <= target[right] and nums[right] + max(diff_right, 0) >= target[right]:
            #     diff_right = target[right] - nums[right]
            # elif nums[right] < target[right] and nums[right] + diff_right < target[right]:
            #     res += target[right] - (nums[right] + max(diff_right, 0))
            #     diff_right = target[right] - nums[right]
                
            # elif nums[right] > target[right] and nums[right] + diff_right <= target[right]:
            #     diff_right = target[right] - nums[right]
            # else:
            #     res += nums[right] + min(diff_right, 0) - target[right]
            #     diff_right = target[right] - nums[right]
                
            # nums[right] = target[right]

            #print("left", left, "right", right, "res", res)

            left +=1
      
            
        
        return res
