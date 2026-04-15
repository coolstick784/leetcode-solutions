# 1. sort the array
# we'll have a set of sums for all numbers < x
# then we'll have a set of sums for all numbers capped at x
# then, we'll see if there's a match that adds to k

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        
        nums.sort()
        sums = set([0])
        new_sums = sums.copy()
        left_idx = -1
        res = []
        for x in range(1, len(nums)+1):
            
            while left_idx < len(nums)-1 and nums[left_idx+1] < x:
                left_idx += 1
                left = nums[left_idx]
                
                added = set()
                for su in sums:
                    if su + left <= k:
                        added.add(su + left)
                sums |= added
                

            capped_num = len(nums) -left_idx - 1
            found = False
            cur = 0
            for _ in range(capped_num + 1):
                if k - cur in sums:
                    found = True
                    res.append(True)
                    break
                cur += x
                if cur > k:
                    break
            if not found:
                res.append(False)
            

        return res
