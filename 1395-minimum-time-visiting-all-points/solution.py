class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        
        def get_min_dist(p1, p2):
            p1_x = p1[0]
            p1_y = p1[1]
            p2_x = p2[0]
            p2_y = p2[1]
            dist_x = abs(p1_x-p2_x)
            dist_y = abs(p1_y-p2_y)
            diff = abs(dist_x - dist_y)
            mult = min(dist_x, dist_y)
            return mult + diff
        
        for idx, p in enumerate(points[:-1]):
            res += get_min_dist(p, points[idx+1])
        return res
