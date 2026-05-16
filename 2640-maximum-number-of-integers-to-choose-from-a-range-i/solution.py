class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cur = 0
        res = 0
        for j in range(1, n+1):
            val = cur + j
            if j not in banned:
                if val > maxSum:
                    break
            
                cur += j
                res += 1

        return res
