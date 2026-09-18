MOD = 10**9 + 7
class Solution:
    def countWinningSequences(self, s: str) -> int:
        @lru_cache(None)
        def get_score(a, b):
            if a == b:
                return 0
            if b == 'E' and a == 'F':
                return -1
            if b == 'F' and a == 'W':
                return -1
            if b == 'W' and a == 'E':
                return -1
            return 1
        @lru_cache(None)
        def solve(idx, prev, score):
            #print(idx, prev, score)
            if idx == len(s) and score > 0:
                return 1
            elif idx == len(s):
                return 0
            rem = len(s) - idx 
            if score - rem > 0:
                return 2**rem
            if score + rem <= 0:
                return 0
            res = 0
            for p in ['F', 'W', 'E']:
                if p == prev:
                    continue
                res += solve(idx+1, p, score + get_score(s[idx], p)) % MOD
            return res
        return solve(0, None, 0) % MOD
