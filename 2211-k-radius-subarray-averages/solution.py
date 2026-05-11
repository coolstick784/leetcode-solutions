class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        cur = sum(nums[:2*k])
        
        for idx in range(len(nums)-2*k):
        
            cur += nums[idx+2*k]
            res[idx+k] = int(cur / (2*k+1))
            cur -= nums[idx]

        return res

