class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ctr = Counter(nums)
        idx = 0
        cur = ctr[0]
        
        while cur > 0:
            nums[idx] = 0
            idx += 1
            cur -= 1
        cur = ctr[1]
        
        while cur > 0:
            nums[idx] = 1
            idx += 1
            cur -= 1
        cur = ctr[2]
        
        while cur > 0:
            nums[idx] = 2
            idx += 1
            cur -= 1
