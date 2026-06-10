class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        #print(round(64**(1/3), 2))
        def solve(n, cur):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if cur == 1:
                return n + 1
            return solve(
                math.floor(
                    round(n**(1/cur), 12)
                    ), 1
            )
        return solve(r, k) - solve(l-1, k)
