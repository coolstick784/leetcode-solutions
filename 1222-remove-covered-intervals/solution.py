class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for idx, (start, end) in enumerate(intervals):
            intervals[idx] = [start, -end]
        intervals.sort()
        for idx, (start, end) in enumerate(intervals):
            intervals[idx] = [start, -end]
        res = len(intervals)
        mx = -1
        for start, end in intervals:
            if end <= mx:
                res -= 1
            mx = max(mx, end)
        return res
