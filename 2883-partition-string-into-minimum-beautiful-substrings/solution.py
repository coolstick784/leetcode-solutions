class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # what does a binary representation of a power of 5 entail?
        pow_bin = ['1', '101', '11001', '1111101', '1001110001', '110000110101', '11110100001001']
        # since s is small, we can do a brute force
        # try starting with each string.  if the current substring starts with that binary, return the solve of everything past that binary + 1
        # if it doesn't, return 1000
        # if our final res = 1000, return -1

        @lru_cache(None)
        def solve(sub, cur):
            ans = []
            if sub == '':
                return cur
            for p in pow_bin:
                cur_len = len(p)
                if sub.startswith(p):
                    ans.append(solve(sub[cur_len:], 1+cur))
                else:
                    ans.append(1000)
            return min(ans)

        res = solve(s, 0)

        if res == 1000:
            return -1
        return res
