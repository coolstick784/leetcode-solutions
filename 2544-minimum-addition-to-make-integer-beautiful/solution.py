class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n_l = [int(s) for s in str(n)]
        pow_10 = 0
        num_l = len(n_l)
        res = 0
        if sum(n_l) <= target:
            return 0

        for idx in range(num_l-1, -1, -1):
            print("idx", idx)
            print("n_l", n_l)
            cur = n_l[idx]
            if cur == 0:
                pow_10 += 1
                continue
            
            change = (10 - cur) * 10**pow_10
            res += change
            for idx2 in range(idx-1, -1, -1):
                n_l[idx2] += 1
                if n_l[idx2] < 10:
                    break
                if n_l[idx2] == 10:
                    n_l[idx2] = 0
            cur_sum = sum(n_l[:idx])
            if cur_sum <= target:
                return res
            pow_10 += 1


        





        
