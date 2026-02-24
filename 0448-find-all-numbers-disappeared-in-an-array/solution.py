class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set([n for n in range(1, len(nums)+1 )])
        for n in nums:
            if n in res:
                res.remove(n)
        return list(res)
        
