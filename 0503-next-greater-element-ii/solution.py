class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums += nums
        out = []
        for idx, n in enumerate(nums):
            if idx >= l:
                continue
            cur_idx = idx + 1
            
            while cur_idx < len(nums):
                cur = nums[cur_idx]
                if cur > n:
                    cur_idx = len(nums)
                    out.append(cur)
                cur_idx += 1
            if cur_idx == len(nums):
                out.append(-1)
        
        return out
