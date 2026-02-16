class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for n in nums:
            ctr[n] = ctr.get(n, 0) + 1
        print(ctr)
        at_each = {}
        for c in ctr:

            at_each.setdefault(ctr[c], []).append(c)


        res = []
        start = len(nums)
        out_len = 0
        while out_len != k:
            
            res.extend(at_each.get(start, []))
            if at_each.get(start, []) != []:
                out_len += len(at_each[start])
            start -= 1
        return res
