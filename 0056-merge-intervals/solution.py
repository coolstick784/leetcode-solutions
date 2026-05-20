# 1. sort intervals by start then end 
#2. for each start, get the current end
# then, while the current end is >= the next start, merge the current end with the next end (whichever is greater stays)
# keep going until the next start is > the current end, then add the current itnerval to our intervals
# rinse and repeat until we've done all intervals


# [[1,3],[2,6],[8,10],[15,18]]
# [1, 3] ps = 1, pe = 3
# [2, 6] ps = 1 pe = 6
# [8, 10] [1, 6] ps=8 pe = 10
# [1, 6] [8, 10] [15, 18]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        prev_start = -1
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                if prev_end != -1:
                    res.append([prev_start, prev_end])
                prev_start = start
                prev_end = end
            else:
                prev_end = max(end, prev_end)
        
        res.append([prev_start, prev_end])
        return res
