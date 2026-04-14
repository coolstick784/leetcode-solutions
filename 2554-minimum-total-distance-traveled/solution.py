from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        @lru_cache(None)
        def solve(i, j):
            if i == len(robot):
                return 0
            if j == len(factory):
                return float("inf")

            pos, limit = factory[j]

            # option 1: skip this factory
            ans = solve(i, j + 1)

            # option 2: send k robots to this factory
            dist = 0
            for k in range(1, min(limit, len(robot) - i) + 1):
                dist += abs(robot[i + k - 1] - pos)
                ans = min(ans, dist + solve(i + k, j + 1))

            return ans

        return solve(0, 0)
