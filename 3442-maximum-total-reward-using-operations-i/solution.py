class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp = {}
        def solve(cur, idx):
            if (cur, idx) in dp:
                return dp[(cur, idx)]
            if idx >= len(rewardValues) or cur >= rewardValues[-1]:
                return cur
            out = -float('inf')
            if cur < rewardValues[idx]:
                out = max(out, solve(cur+rewardValues[idx], idx+1))
            out = max(out, solve(cur, idx+1))
            dp[(cur, idx)] = out
            return out
        
        res = solve(0, 0)
        del dp
        
        return res
