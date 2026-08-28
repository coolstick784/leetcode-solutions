class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        all_points = set([tuple(point) for point in points])
        
        res = float('inf')
        for x, y in points:
            for x2, y2 in all_points:
                if x2 == x or y2 == y:
                    continue
                
                if (x2, y) in all_points and (x, y2) in all_points:
                  
                    res = min(res, (abs(x2-x) * abs(y2-y)))
        if res == float('inf'):
            return 0
        return res
                
