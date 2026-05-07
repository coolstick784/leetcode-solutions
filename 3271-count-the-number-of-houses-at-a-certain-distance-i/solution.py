# we can either travel directly, to x -> y -> directly, or to y -> x -> directly

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = {}
        for h1 in range(1, n+1):
            for h2 in range(h1, n+1):
                direct = abs(h2-h1)
                through_x = abs(x-h1) + 1 + abs(y-h2)
                through_y = abs(y-h1) + 1 + abs(x-h2)
                val = min([direct, through_y, through_x])
                res[val] = res.get(val, 0) + 2


        out = []
        for k in range(1, n+1):
            out.append(res.get(k, 0))

        return out
