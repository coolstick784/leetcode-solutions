class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [x**2 for x in range(1, math.ceil(math.sqrt(n)) + 1)]
        @lru_cache(None)
        def solve(num):

            for square in squares:
                if square > num:
                    return False
                if not solve(num-square):
                    return True
            return False
        return solve(n)

