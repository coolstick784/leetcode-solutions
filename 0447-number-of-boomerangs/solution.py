# for each point, get the distance to every other point
# each point will have its own dictionary with lengths, and the number of points for each lenth 
# if a specific length has more than one point in it, e.g. (a, b, c) ac, ab, bc, ba, cb, ca so it's that number factorial

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            return math.sqrt((x1-x2)**2 + (y2-y1)**2)
        lengths_dict = {}
        for idx, p1 in enumerate(points):
            x, y = p1
            lengths_dict[(x, y)] = {}
            for idx2, p2 in enumerate(points):
                x2, y2 = p2
                cur_dist = dist((x, y), (x2, y2))
                lengths_dict[(x, y)][cur_dist] = lengths_dict[(x, y)].get(cur_dist, 0) + 1

        

        res = 0
        for x, y in points:
            for l in lengths_dict[(x, y)]:
                if lengths_dict[(x, y)][l] > 1:
                    res += lengths_dict[(x, y)][l] * (lengths_dict[(x, y)][l] -1)
        return res
