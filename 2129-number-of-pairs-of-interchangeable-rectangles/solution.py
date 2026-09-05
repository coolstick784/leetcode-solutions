class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        groups = {}
        for w, h in rectangles:
            groups[w/h] = groups.get(w/h, 0) + 1
        res = 0
        for r in groups:
            res += groups[r] * (groups[r]-1) / 2
        return int(res)
