
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        explored = set()
        to_explore = deque([(x, 0), (x, y), (0, y)])
        # We can pour x into y until y fills up or x is empty, y into x until x fills up or y is empty, completely fill up x, or completely fill up y
        # can also empty x or y
        while to_explore:
            poss = to_explore.popleft()

            
            if poss[0] == target or poss[1] == target or poss[0] + poss[1] == target:
                return True
            pours = [
                (poss[0]-(y-poss[1]), y), 
            (0, poss[1] + poss[0]), 
            (x, poss[1] - (x-poss[0])),
            (poss[1] + poss[0], 0),
            (x, poss[1]),
            (poss[0], y),
            (0, poss[1]),
            (poss[0], 0)
            ]
            
            explored.add(poss)
            for p in pours:
                if p not in explored and p[0] <= x and p[1] <= y and p[0] >= 0 and p[1] >= 0:
                    to_explore.append(p)
            
        return False

        
