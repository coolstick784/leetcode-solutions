from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)

        # counts[i] holds prefix counts up to i (inclusive), as a 26-length list
        counts = [[0]*26 for _ in range(n)]
        for i, ch in enumerate(s):
            ci = ord(ch) - ord('a')
            if i > 0:
                counts[i] = counts[i-1].copy()  # copy 26 ints (cheap and predictable)
            counts[i][ci] += 1

        res = []
        for l, r, k in queries:
            num_odd = 0

            # compute odds by subtracting prefix counts
            for c in range(26):
                right = counts[r][c]
                left = counts[l-1][c] if l > 0 else 0
                if (right - left) & 1:   # parity check
                    num_odd += 1

            res.append((num_odd // 2) <= k)

        return res

