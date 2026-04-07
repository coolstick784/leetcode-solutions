class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        sums = set()
        res = set()
        
        for n1 in range(1,  int(n ** (1/3)) + 2):
            for n2 in range(n1,  int(n ** (1/3)) + 2):
                cur_val = n1**3 + n2**3
                if cur_val in sums and cur_val <= n:
                    res.add(cur_val)
                else:
                    sums.add(cur_val)
        res = list(res)
        res.sort()
        return res
