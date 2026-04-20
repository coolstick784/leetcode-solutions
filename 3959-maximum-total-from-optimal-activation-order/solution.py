# can't you just choose the highest 1 witha  limit of 1, highest 2 with a limit of 2, and so on?

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        limit_dict = {}
        for idx, val in enumerate(value):
            cur_limit = limit[idx]
            limit_dict.setdefault(cur_limit, []).append(val)
        for l in limit_dict:
            limit_dict[l].sort()
            limit_dict[l].reverse()
        nums = list(set(limit))
        nums.sort()
        res = 0
        for n in nums:
            res += sum(limit_dict[n][:n])
        return res
