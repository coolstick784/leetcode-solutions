class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # include DP
        # At each elemetn in nums, we want the highest possible value ending with that number. 
        # We want the largest possible value going into the element that is either positive or negative

        # If there's a negative and positive going into it, we want to multiply by both
        # If there's only positive, just multiply by that
        # If there's only negative, keep the negative as well as the positive

        dp = [[None, None] for _ in range(len(nums))]
        res = -2**31 
        for idx, n in enumerate(nums):
            if idx == 0:
                dp[idx] = [n, n]


            else:
                prev = dp[idx-1]
                if (prev[0] > 0 and prev[1] < 0) and n < 0:
                    dp[idx] = [prev[1] * n, prev[0] * n]
                elif  (prev[0] > 0 and prev[1] < 0) and n > 0:
                    dp[idx] = [prev[0] * n, prev[1] * n]
                elif prev[0] > 0 and prev[1] > 0:
                    dp[idx] = [prev[0] * n, prev[1] * n]
                elif (prev[0] < 0 and prev[1] < 0) and n < 0:
                    dp[idx] = [max(prev[0] * n, prev[1] * n), n]
                elif (prev[0] < 0 and prev[1] < 0) and n > 0:
                    dp[idx] = [n, min(prev[0] * n, prev[1] * n)]
                elif prev[0] == 0 or prev[1] == 0:
                    dp[idx] = [n, n]
                else:
                    dp[idx] = [0, 0]
            print('n', n)
            print(dp[idx])
            res = max(res, max(dp[idx]))

            

        if 0 in nums:
            res = max(res, 0)
        return res

                


