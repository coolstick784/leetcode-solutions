# have a parallel array, subs
# so e.g. we have to remove 2 from 1, add -2 to nums[0] and 2 to nums[0+k]
# [2,2,3,1,1,0]
# [0,0,0,0,0,0]
# cur = -2, [0,0,0,2,0,0]
# cur=-3, [0,0,0,2,1,0]
# cur = -3, [0,0,0,2,1,0]
#cur=-1, [0,0,0,2,1,0]



class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        subs = [0 for _ in nums]
        cur = 0
        for idx, n in enumerate(nums):
            cur += subs[idx]
            n += cur
            if n < 0:
                return False
            if idx+k < len(nums):
                subs[idx+k] += n
            elif idx+k > len(nums) and n > 0:
                return False
            cur -= n
        return True

        
