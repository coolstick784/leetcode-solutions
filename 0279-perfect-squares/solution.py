squares = []
for n in range(1, 101):
    squares.append(n*n)

@lru_cache(None)
def solve(num):
    if num == 0:
        return 0
    if num < 0:
        return float('inf')
    res = float('inf')
    for i in squares:
        if i > num:
            break
        res = min(res, 1+solve(num-i))
    return res


class Solution:
    def numSquares(self, n: int) -> int:
        return solve(n)
