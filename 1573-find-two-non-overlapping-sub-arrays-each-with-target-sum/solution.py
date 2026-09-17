class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        pre = [0]
        for n in arr:
            pre.append(pre[-1] + n)
        
        best = {}
        best_past = {}
        for idx, n in enumerate(arr):
            cur = pre[idx]
            goal = cur + target
            if pre[-1] < goal:
                continue
            end_idx = bisect.bisect(pre, goal) - 1
            s = pre[end_idx] - cur
            dist = end_idx - idx
           
            if s == target:
                best[idx] = dist
        for idx in range(len(arr)-1, -1, -1):
            best_past[idx] = min(best.get(idx, float('inf')), best_past.get(idx+1, float('inf')))
        res = float('inf')

        for idx in range(len(arr)):
            if idx not in best:
                continue
            res = min(res, best[idx] + best_past.get(idx+best[idx], float('inf')))
        

        if res == float('inf'):
            return -1
        return res
