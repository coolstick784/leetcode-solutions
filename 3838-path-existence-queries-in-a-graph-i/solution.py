class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        latestPossible = [idx for idx, num in enumerate(nums)]
        
        for idx in range(len(nums) -2, -1, -1):
            if nums[idx] + maxDiff >= nums[idx+1]:
                latestPossible[idx] = latestPossible[idx+1]
        res = []
        for q in queries:
            start, end = sorted(q)
            res.append(latestPossible[start] >= end)
        return res
            



        
