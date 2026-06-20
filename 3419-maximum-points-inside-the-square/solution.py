class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        mn = 0
        mx = 0
        for idx, (x, y) in enumerate(points):
            mx = max(mx, abs(x), abs(y)) 
            points[idx] = (abs(x), abs(y))
        mx += 1
    
        res = 0
        while mn < mx:
            med = (mn + mx) //2
           
            tags = set()
            poss = True 
            ct = len(points)
            for idx, (x, y) in enumerate(points):
                if x > med or y > med:
                    ct -= 1
                    continue
                tag = s[idx]
                if tag in tags:
                    poss = False
                    break
                else:
                    tags.add(tag)
            if not poss:
                mx = med
            else:
                res = max(res, ct)
                mn = med + 1


        return res
