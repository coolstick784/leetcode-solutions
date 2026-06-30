class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        ctr = {'a':0, 'b':0, 'c':0}
        found = False
        while right < len(s):
            ch = s[right]
            ctr[ch] = ctr[ch] + 1
            
            while ctr['a'] > 0 and ctr['b'] > 0 and ctr['c'] > 0:
                found = True
                l = s[left]
                ctr[l] -= 1
                left += 1
            if found:
                res += left
            right += 1
        return res
        
