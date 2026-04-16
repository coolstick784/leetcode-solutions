# use dp here
# so basically, we want the counts of everything up to it, and the new counts
# so originally we start with {0:1}
# then, for each number to k, add to the new dp with the new count
# if it's > target, don't include it
# so .eg. if our face is 5 and we start at 3, dp[5] = d[3] from 2 and add them and so on
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        cur_dp = {0:1}
        new_dp = {}
        
        for die in range(n):
            for face in range(1, k+1):
                for prev in cur_dp:
                    if prev+face > target:
                        continue
                    new_dp[prev+face] = (new_dp.get(prev+face, 0) + cur_dp[prev]) % (10**9+7)
            cur_dp = new_dp.copy()
            new_dp = {}
        return cur_dp.get(target, 0) % (10**9+7)
