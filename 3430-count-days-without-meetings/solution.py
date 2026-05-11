class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = 0

        prev_end = 0
        for start, end in meetings:
            if start > prev_end:
                res += (start-prev_end-1)
            prev_end = max(prev_end, end)
        if days > prev_end:
            res += (days-prev_end)

        return res

