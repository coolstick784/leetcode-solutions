class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = int(len(nums)*(len(nums)-1)/2)
        ctr = {}
        for idx, n in enumerate(nums):
            res -= (ctr.get(n-idx, 0))
            ctr[n-idx] = ctr.get(n-idx, 0) + 1
        return res

        
