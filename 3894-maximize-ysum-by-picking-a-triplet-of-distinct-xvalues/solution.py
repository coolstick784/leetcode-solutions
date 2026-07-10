class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        taken = set()
        y = [(n, idx) for idx, n in enumerate(y)]
        y.sort(reverse=True)
        res = 0
        y_idx = 0
        while y_idx < len(y) and len(taken) < 3:
            x_val = x[y[y_idx][1]]
            if x_val not in taken:
                taken.add(x_val)
                res += y[y_idx][0]
            y_idx += 1
        if len(taken) == 3:
            return res
        return -1
