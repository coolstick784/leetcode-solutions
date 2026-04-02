class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        dp = [len(A)] * 4
        for a in A:
            dp[a] -= 1
            dp[2] = min(dp[2], dp[1]);
            dp[3] = min(dp[3], dp[2]);
        return dp[3]
