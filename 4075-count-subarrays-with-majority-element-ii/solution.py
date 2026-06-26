class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        nums = [1 if n == target else -1 for n in nums]
        cur = 0
        pre = [0]
        for n in nums:
            cur += n
            pre.append(cur)
        ctr = {0: 1}
        res = 0
        prev = 0
        for idx, p in enumerate(pre):
            if idx == 0:
                continue
            if p > pre[idx-1]:
                sol = prev + ctr.get(p-1, 0)
            else:
                sol = prev - ctr.get(p, 0)

            res += sol
            prev = sol
            ctr[p] = ctr.get(p, 0) + 1
        return res
