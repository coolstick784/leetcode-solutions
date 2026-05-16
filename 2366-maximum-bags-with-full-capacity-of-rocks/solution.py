#[1, 1, 0, 1]
#[0, 1, 1, 1]
# 1, 2, 3


# [0, 2, 8]
# 1, 2, 3

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = []
        for idx, r in enumerate(rocks):
            diffs.append(capacity[idx] - r)
        diffs.sort()
        cur = additionalRocks
        res = 0
        while cur >= 0 and res < len(diffs):
            if cur >= diffs[res]:
                cur -= diffs[res]
                res += 1
            else:
                break

        return res
