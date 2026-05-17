# always discard the rightmost when we hit the limit


# arrivals = [1,2,3,3,3,4], w = 3, m = 2
# {1:1} 
# {1:1, 2:1}
# {1:1, 2:1, 3:1}
# {2:1, 3:2}
# {2:1, 3:3} 
# {2:1, 3:2}


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        ctr = {}
        res = 0
        for idx, a in enumerate(arrivals):
            ctr[a] = ctr.get(a, 0) + 1
            if idx >= (w):
                ctr[arrivals[idx-w]] -= 1
            if ctr[a] > m:
                ctr[a] -= 1
                arrivals[idx] = -1
                ctr[-1] = 0
                res += 1
        return res

