# for each index, we want the number of ways we can split ending at that index multiplied by the number after it

# if it is a 1, we want the sum of ways we can do 
#e.g. for [0,1,0,0,1, 0], for the 2nd 1, we'll do (ending at 3) + (ending at 2) + (ending at 1)
# ending at last 0 is just equal to ending at last 1

#[0, 1, 0, 0, 1]
# sum ending = [0, 1, 2, 3, 6]
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        cur = 0
        idx = 0
        prev_one = -1
        sum_ending = []
        while idx < len(nums):
            if nums[idx] == 1:
                if prev_one == -1:
                    cur = 1
                elif prev_one != 0:
                    cur = sum_ending[-1] - sum_ending[prev_one-1]
                else:
                    cur = sum_ending[-1]
                if sum_ending:
                    sum_ending.append(cur + sum_ending[-1])
                else:
                    sum_ending = [cur]
                prev_one = idx
            else:
                if prev_one == -1:
                    cur = 0
                elif prev_one != 0:
                    cur = sum_ending[prev_one] - sum_ending[prev_one - 1]
                else:
                    cur = sum_ending[prev_one]
                if sum_ending:
                    sum_ending.append(cur + sum_ending[-1])
                else:
                    sum_ending = [cur]
            idx += 1
        
        return cur % (10**9+7)
        
