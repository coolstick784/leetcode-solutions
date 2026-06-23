# for each index, how many <= it are going up, and how many >= it are going down?

# 1. how many possible options do we have that are increasing at idx-1 for all nums <= n and >= 0?
# 2. for its counterpart, how many options do we have that are decreasing at idx-1 for all nums >= c and <= num?
# there will always be a pair that exists
# at the end, we just need to get the min of (n, c)
MOD = 10**9+7
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        down = {}
        up = {}

        for idx in range(1, len(nums)+1):
            new_up = {}
            new_down = {}
            num = nums[idx-1]
            pre = 0
            suf = 0
            for n in range(num+1): 
                c = num - n
                if idx == 1:
                    new_up[n] = 1
                    new_down[c] = 1
                    continue
                pre += up.get(n, 0)
                new_up[n] = pre
                suf += down.get(c, 0)
                new_down[c] = suf
                mn = min(new_up[n], new_down[c])
                new_up[n], new_down[c] = mn, mn
            up = new_up.copy()
            down = new_down.copy()
         
        last = nums[-1]
        res = 0
        for n in range(last+1):
            poss = min(up[n], down[last-n])
            res += poss
            res = res % MOD

        return res
                    
