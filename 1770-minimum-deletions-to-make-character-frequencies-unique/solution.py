class Solution:
    def minDeletions(self, s: str) -> int:
        ctr = Counter(s)
        vals = {}
        for key, val in ctr.items():
            vals[val] = vals.get(val, 0) + 1
        res = 0
        for v in range(len(s), 0, -1):
            cur = vals.get(v, 0)
            if cur > 1:
                res += (cur-1)
                vals[v-1] = vals.get(v-1, 0) + cur - 1
        return res
