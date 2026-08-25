class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        longest = []
        cur = 0
        for idx, n in enumerate(nums):
            if idx == 0 or n != nums[idx-1] + 1:
                cur = 1
            else:
                cur += 1
            longest.append(cur)
        
        res = []
        for idx, n in enumerate(nums[:len(nums)-k+1]):
            if longest[idx+k-1] >= k:
                res.append(nums[idx+k-1])
            else:
                res.append(-1)
        return res
