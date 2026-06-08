class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        res = 1
        prev_start = ranges[0][0]
        prev_end = ranges[0][1]
        for start, end in ranges:
            if start > prev_end:
                res *= 2
                res = res % (10**9+7)
                prev_start = start
                prev_end = end
            else:
                prev_end = max(prev_end, end)
        
        res *= 2
        res = res % (10**9+7)
        return res
