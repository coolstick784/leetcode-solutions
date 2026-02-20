class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])

        # DP table with extra padding to avoid boundary checks
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]

        # Base cases
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1

        # Fill DP table bottom-up
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, need)

        return dp[0][0]
