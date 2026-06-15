# 1 -> 2, 3, 4, 5, 6
# 2 -> 1, 3, 5
# 3 -> 1, 2, 4, 5
# 4 -> 1, 3, 5
# 5 -> 1, 2, 3, 4, 6
# 6 -> 1, 5



class Solution:
    def distinctSequences(self, n: int) -> int:
        @lru_cache(None)
        def solve(lastTwo, left):
            if left <= 0:
                return 1
            able = set()
            prev = lastTwo[1]
            if prev == 1:
                able = set([2, 3, 4, 5, 6])
            elif prev == 2:
                able = set([1, 3, 5])
            elif prev == 3:
                able = set([1, 2, 4, 5])
            elif prev == 4:
                able = set([1, 3, 5])
            elif prev == 5:
                able = set([1, 2, 3, 4, 6])
            elif prev == 6:
                able = set([1, 5])
            elif prev == 0:
                able = set([1, 2, 3, 4, 5,6])
            if lastTwo[0] in able:
                able.remove(lastTwo[0])
            res = 0
        
            for p in able:
                res += solve((prev, p), left-1)
 
            return res % (10**9+7)



        return solve((0, 0), n)
