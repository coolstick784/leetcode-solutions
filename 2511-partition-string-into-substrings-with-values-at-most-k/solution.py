# if a digit is >= k, 

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur = 0
        res = 1
        for ch in s:
            n = int(ch)
            if n > k:
                return -1
            
            cur = cur * 10 + n
       
            if cur > k:
                res += 1
                cur = n
        
        return res
