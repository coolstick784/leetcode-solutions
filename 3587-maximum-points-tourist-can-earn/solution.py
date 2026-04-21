class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n   # this is for day k

        for day in range(k - 1, -1, -1):
            new_dp = [0] * n

            for city in range(n):
                best = stayScore[day][city] + dp[city]   # stay

                for new_city in range(n):
                    best = max(best, travelScore[city][new_city] + dp[new_city])  # travel

                new_dp[city] = best

            dp = new_dp

        return max(dp)
