# for each height 1=100, we want a list of lengths that are >= that height
# then, when we get a point, we just have to bisect the list and get the index 
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        heights = [[] for _ in range(101)]
        for h in range(1, 101):
            for l, hei in rectangles:
                if hei >= h:
                    heights[h].append(l)
            heights[h].sort()
            
        # [1, 2, 2]
        res = []
        for x, y in points:
            if heights[y]:
                l = len(heights[y])
                res.append(
                    l - bisect.bisect_left(heights[y], x)
                    )
            else:
                res.append(0)
        return res
