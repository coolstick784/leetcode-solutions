class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        idxs = {}
        for idx, n in enumerate(nums):
            idxs.setdefault(n, []).append(idx)

        def findMin(cur):
            out = -float('inf')
            for i, idx in enumerate(cur[:-1]):
                dist = cur[i+1] - idx
                out = max(out, dist //2)
            
            dist = cur[0] + (len(nums) - cur[-1])
            out = max(out, dist//2)
            return out        

        res = float('inf')
        for n, l in idxs.items():
            
            res = min(res, findMin(l))

        return res

