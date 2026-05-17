# move to the right
# if the number is > the current max, we first subtract the excess by the difference
# if there is still a difference, we need to know how many numbers are before it, that emans all of them are the max
# we increment each diff // n (and add that to our max), then change diff % n elements, adding our max by 1, and our excess is n + 1 - (diff % n)


# [3, 7, 1, 6] 0, 3
# [5, 5, 1, 6] 0, 5
# [5, 5, 1, 6] 4, 5
# [5, 5, 2, 5, 9] 3, 5
# [5, 5, 5, 5, 6]
# 

# [10, 1]

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        excess = 0
        cur_max = nums[0]
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            if n > cur_max:
                diff = n - cur_max
                if excess >= diff:
                    
                    excess -= diff
                    diff = 0
                else:
                    diff = diff - excess
                    excess = 0
                change_diff = diff // (idx+1)
                cur_max += change_diff
                if diff and diff % (idx+1) != 0:
                    cur_max += 1
                    excess = idx+1-(diff % (idx+1))
            else:
                excess += (cur_max - n)

        return cur_max
        
