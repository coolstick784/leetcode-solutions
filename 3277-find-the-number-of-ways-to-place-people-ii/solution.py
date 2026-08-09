# for each point, get every other point where 1. x2 >= x1, 2. y2 <= y1, 3. there are no points where (x1 <= x3 <= x2) and (y1 >= y3 >= y2)
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], -x[1]))
        res = 0
        for idx, (x, y) in enumerate(points):
            mn_y = -float('inf')
 
            for idx2, (x2, y2) in enumerate(points[idx+1:]):
      
                if y2 > y:
                    continue
                if y2 > mn_y:
                    print("x", x, "y", y, "x2", x2, "y2", y2)
                    mn_y = y2
                    res += 1
        return res

