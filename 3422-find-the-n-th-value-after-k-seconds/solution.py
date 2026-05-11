# 4 + 3 + 2 + 1 , 1*4 + 1*3 + 1*2 + 1*1 = 10
# 4 + 3 + 2 + 1 + 3 + 2 + 1 + 2 + 1 + 1, 1*4 + 2*3 + 3*2 + 4*1 = 20
# 4 + 3 + 2 + 1 + 3 + 2 + 1 + 2 + 1 + 1 + 3 + 2 + 1 + 2 + 1 + 1 + 2 + 1 + 1 + 1, 1*4 + 3*3+6*2+1*10 = 35

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        prev = [None for _ in range(n)]
        cur = [1 for _ in range(n)]
        for i in range(k):
            prev = cur.copy()
            cur_s = 0
            for idx, p in enumerate(prev):
                cur[idx] = p + cur_s
                cur_s += p

        
        return cur[-1] % (10**9+7)
