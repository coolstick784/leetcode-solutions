class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        s = sorted(nums)
        idxs = {}
        for idx, n in enumerate(nums):
            idxs.setdefault(n, []).append(idx)

        res = [0 for _ in nums]
        cur_idxs = []
        cur_ns = []
        for idx, n in enumerate(s):
            if idx == 0 or n > (limit + s[idx-1]):
                cur_idxs.sort()
                for p, i in enumerate(cur_idxs):
                    res[i] = cur_ns[p]
                cur_idxs = []
                cur_ns = []
            cur_idxs.append(idxs[n].pop())
            cur_ns.append(n)
        cur_idxs.sort()
        for p, i in enumerate(cur_idxs):
            res[i] = cur_ns[p]
        return res
