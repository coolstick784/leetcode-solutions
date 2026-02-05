class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        if rungs[0] <= dist:
            res = 0
        elif rungs[0] % dist == 0:
            res = rungs[0] // dist - 1
        else:
            res = rungs[0] // dist 
        for idx, n in enumerate(rungs[:-1]):

            diff = rungs[idx+1] - n
            if diff > dist:
                if diff % dist == 0:
                    res += diff // dist - 1
                else:
                    res += diff // dist 
 

        return res
        
