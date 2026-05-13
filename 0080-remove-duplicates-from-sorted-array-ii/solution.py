# shift all cells to the right if we're more than 2
# if the current val is < the prev val, we're done


# [0, 0, 1, 1, 1, 1, 2, 3, 3] 2 -> 3 -> 4
#[0,0,1,1,1,2,3,3,1] 4-> 4
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_idx = 2
        if len(nums) <= 2:
            return len(nums)
        

        num_removed = 0
        start = len(nums)
        while cur_idx < (start-num_removed):
       
            val = nums[cur_idx]
            prev1 = nums[cur_idx-1]
            prev2 = nums[cur_idx-2]
            if val < prev1 or val < prev2:
                break
            if val == prev1 and val == prev2:
                del nums[cur_idx]
                num_removed += 1
            else:
                cur_idx += 1
     

        return start - num_removed
