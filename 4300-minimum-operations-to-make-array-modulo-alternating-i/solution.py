class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        res = float('inf')
        for x in range(k):
            for y in range(k):
                if x == y:
                    continue
                cur = 0
                for idx, n in enumerate(nums):
                    if idx % 2 == 0:
                        goal = x
                    else:
                        goal = y
                    m = n % k
                    cur += min(abs(m-goal), abs(m-(goal-k)), abs(m-(goal+k)))
                print("x", x, "y", y, "cur", cur)
                res = min(res, cur)
        return res
