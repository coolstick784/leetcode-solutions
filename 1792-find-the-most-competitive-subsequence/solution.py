class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        rem = k
        for idx, n in enumerate(nums):
            left = len(nums) - idx 
            while res and n < res[-1] and left > rem:
                res.pop() 
                rem += 1
            if len(res) < k:
                res.append(n)
                rem -= 1
        return res
