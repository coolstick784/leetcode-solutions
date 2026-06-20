class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()

        # Building 1 must be height 0
        restrictions = [[1, 0]] + restrictions

        # If building n is not restricted, its natural max is n - 1
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        # Left to right: each restriction cannot be more than previous + distance
        for i in range(1, len(restrictions)):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)

        # Right to left: each restriction cannot be more than next + distance
        for i in range(len(restrictions) - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)

        res = 0

        # Find max possible peak between every pair of restrictions
        for i in range(1, len(restrictions)):
            left_idx, left_h = restrictions[i - 1]
            right_idx, right_h = restrictions[i]

            dist = right_idx - left_idx

            middle_max = (left_h + right_h + dist) // 2
            res = max(res, middle_max)

        return res
