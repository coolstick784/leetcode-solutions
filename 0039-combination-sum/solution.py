from functools import lru_cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(set(candidates))
        candidates.sort()

        @lru_cache(None)
        def solve(t, start):
            out = []

            for i in range(start, len(candidates)):
                c = candidates[i]

                if c == t:
                    out.append([c])
                elif c < t:
                    for sol in solve(t - c, i):
                        out.append([c] + sol)
                else:
                    break

            return out

        return solve(target, 0)
