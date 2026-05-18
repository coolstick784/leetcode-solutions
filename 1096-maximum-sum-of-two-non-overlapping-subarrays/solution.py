#  nums = [0,6,5,2], firstLen = 1, secondLen = 2
# start from 1, 2

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    
        def maxStart(start_idx, l):
            res = 0
            left = start_idx
            right = start_idx
            cur = 0
            while right < len(nums):
                cur += nums[right]
                if (right-left+1) > l:
                    cur -= nums[left]
                    left += 1
                if (right-left+1) == l:
                    res = max(res, cur)
                right += 1
            return res
        
        def maxEnd(end_idx, l):
            res = 0
            left = 0
            right = 0
            cur = 0
            while right < end_idx+1:
                cur += nums[right]
                if (right-left+1) > l:
                    cur -= nums[left]
                    left += 1
                if (right-left+1) == l:
                    res = max(res, cur)
                right += 1
            return res
        
        res = 0
        
        for start in range(firstLen, len(nums) -secondLen+1):
            res = max(res, maxStart(start, secondLen) + maxEnd(start-1, firstLen))
        for start in range(secondLen, len(nums) -firstLen+1):
            res = max(res, maxStart(start, firstLen) + maxEnd(start-1, secondLen))
        return res
