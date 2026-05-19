
# "226"
# solve(0) = solve(1) + solve(2) = 2 + 1 = 3
# solve(1) = solve(2) + solve(3) = 1 + 1 = 2
# solve(2) = solve(3) = 1
# solve(3) = 1


class Solution:
    def numDecodings(self, s: str) -> int:
        # 1. dict with number to letter

        # 2. we'll want a lru cached function with the number of ways to interpret
        # if it's empty, return 1
        # if it's possible to interpret the first char, add 1 * the ways to interpret the rest
        # if it's possible to intrepret the frist 2 chars, add 1 * the ways to interpret the rest

        @lru_cache(None)
        def solve(idx):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0

            out = solve(idx+1)
            if idx < len(s) - 1 and int(s[idx] + s[idx+1]) < 27:
                out += solve(idx+2)
            return out


        return solve(0)
