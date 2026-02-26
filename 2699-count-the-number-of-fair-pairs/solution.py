from typing import List
from collections import Counter
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ctr = Counter(nums)
        keys = sorted(ctr)

        # prefix counts over unique keys (counts, not sums)
        pref = [0] * (len(keys) + 1)
        for i, k in enumerate(keys):
            pref[i + 1] = pref[i] + ctr[k]

        def count_in_range(lo_val: int, hi_val: int) -> int:
            """# of elements (with multiplicity) whose value is in [lo_val, hi_val]."""
            L = bisect_left(keys, lo_val)
            R = bisect_right(keys, hi_val)
            return pref[R] - pref[L]

        res = 0
        for i, a in enumerate(keys):
            ca = ctr[a]

            # valid b range for sums:
            lo_b = lower - a
            hi_b = upper - a

            # enforce b >= a to avoid double counting
            if hi_b < a:
                continue
            lo_b = max(lo_b, a)

            # count all b values in [lo_b, hi_b] with multiplicity
            total_b = count_in_range(lo_b, hi_b)

            # remove the "b == a" part from that total, we'll handle it carefully
            use_same = (lo_b <= a <= hi_b)
            if use_same:
                total_b -= ca

                # pairs (a,a): choose 2 out of ca
                res += ca * (ca - 1) // 2

            # pairs (a,b) where b > a: ca * (count of such b)
            res += ca * total_b

        return res
