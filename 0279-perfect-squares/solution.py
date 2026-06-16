squares = [n**2 for n in range(1, 10**2+1)]
@lru_cache(None)
def solve(val):
    if val == 0:
        return 0
    out = float('inf')
    for sq in squares:
        if sq > val:
            break
        out = min(out, 1 + solve(val - sq))
    return out


class Solution:
    def numSquares(self, n: int) -> int:
        return solve(n)
