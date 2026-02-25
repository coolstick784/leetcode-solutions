class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        res = []
        goal = len(nums) // 3
        for c in ctr:
            if ctr[c] > goal:
                res.append(c)
        return res
