class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        prev = {}
        res = 0
        for idx, t in enumerate(tasks):
            p = prev.get(t, -float('inf'))
            res = max(p + space+1, res + 1)
            prev[t] = res


        return res
