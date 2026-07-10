MOD = 10**9+7
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
    
        

        
        best = {} # ending at idx -> number of sols
        for idx in range(len(s) -1, -1, -1):
            best[idx] = 0
            for d in range(1, 11):
                if s[idx] == "0":
                    continue
                if idx + d > len(s):
                    continue
                cur_s = int(s[idx:idx+d])
                if cur_s >= 1 and cur_s <= k:
                    if idx + d == len(s):
                        best[idx] += 1
                    else:
                        best[idx] += best.get(idx+d, 0)
            best[idx] = best[idx] % MOD



        
        return best.get(0, 0) 
