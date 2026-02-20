class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]
        cur = 1
        while cur < k:
            cur =  f[-2] + f[-1]
            if cur <= k:
                f.append(cur)
        res = 0
        cur_val = k
        f.reverse()
        # k = 7, [5, 3, 2, 1, 1] 7 > 5 -> subtract and add 1
        # 2, [3, 2, 1, 1] 2 < 3 -> pass
        # 2, [2, 1, 1] 2 = 2 -> add 1 and end
        for n in f:
            if n < cur_val:
                cur_val -= n
                res += 1
            elif n > cur_val:
                continue
            else:
                res += 1
                return res


