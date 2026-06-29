from typing import List
from functools import lru_cache
import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        INF = float('inf')

        @lru_cache(None)
        def solve(i, prev):
            if i == len(arr1):
                return 0

            res = INF

            # Option 1: keep arr1[i]
            if arr1[i] > prev:
                res = min(res, solve(i + 1, arr1[i]))

            # Option 2: replace arr1[i]
            j = bisect.bisect_right(arr2, prev)
            if j < len(arr2):
                res = min(res, 1 + solve(i + 1, arr2[j]))

            return res

        ans = solve(0, -1)
        return ans if ans < INF else -1
