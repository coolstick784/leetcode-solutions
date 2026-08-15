class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        l = len(requests)
        num_combos = 1 << l
        res = 0
        for c in range(num_combos):
            excess = [0 for _ in range(n)]
            total_excess = 0
            for idx, (start, end) in enumerate(requests):
                if not (c & (1 << idx)):
                    continue
                if start == end:
                    continue
                excess[start] += 1
                excess[end] -= 1
                if excess[start] == 1:
                    total_excess += 1
                elif excess[start] == 0:
                    total_excess -= 1
                if excess[end] == -1:
                    total_excess += 1
                elif excess[end] == 0:
                    total_excess -= 1
            if total_excess == 0:
            
                res = max(res, c.bit_count())
        return res

