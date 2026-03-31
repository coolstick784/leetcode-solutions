class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0 
        pre = [-1 for _ in range(n)]
        p = -1 

        for i in range(n): 
            pre[i] = p 

            if s[i] == "0": 
                p = i 
       
        res = 0    
        for i in range(n):
            cnt0 = 1 if s[i] == "0" else 0
            j = i
            while j >= 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res



