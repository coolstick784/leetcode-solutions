from functools import lru_cache
from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        @lru_cache(None)
        def solve(idx, diff):
            if idx == len(rods):
                if diff == 0:
                    return 0
                return -float("inf")

            rod = rods[idx]

            # Option 1: skip rod
            out = solve(idx + 1, diff)

            # Option 2: add rod to taller side
            out = max(out, solve(idx + 1, diff + rod))

            # Option 3: add rod to shorter side
            # If we add to shorter side, the equal/shared height increases by min(diff, rod)
            out = max(out, min(diff, rod) + solve(idx + 1, abs(diff - rod)))

            return out

        return solve(0, 0)
