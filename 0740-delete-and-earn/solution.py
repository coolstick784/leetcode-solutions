class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # At each number, we should either choose to add its total, or delete it via n-1 or n+1
        # Therefore, we should use DP
        # DP[first element] = value
        # DP[second el] = value
        # DP[third el] = DP[first element] + DP[third el]
        # DP[4th and beyond] = max(dp[n-2], dp[n-3]) + dp[n]
        nums.sort()
        ctr = Counter(nums)
        vals = {}
        for n in ctr:
            vals[n] = ctr[n] * n
        dp = {}
        res = 0



        for idx, n in enumerate(vals):
  

            if n-1 not in dp:
                dp[n] = res + vals[n]
            else:
                dp[n] = max(dp[n-1], prev_res+vals[n])
            if n+1 in vals:
                prev_res = res
            res = dp[n]

        

        return res

            
        
        

        
