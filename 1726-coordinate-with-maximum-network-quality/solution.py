class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        res = 0
        sol = (0, 0)
        for x in range(51):
            for y in range(51):
                cur = 0
                for xi, yi, q in towers:
                    dist = round(math.sqrt((xi-x)**2 + (yi-y)**2), 5)
    
                    if dist <= radius:
                        cur += int(float(q) / (1+dist))
          
                        if cur > res:
                            res = cur
                            sol = (x, y)


        return sol

