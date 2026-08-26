class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        res = []
        for n in sorted(ctr.keys()):
            if ctr[n] == 1 and n-1 not in ctr and n+1 not in ctr:
                res.append(n)
        return res
