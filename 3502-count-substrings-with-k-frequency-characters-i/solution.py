class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        res = 0
        while left < len(s):
            ctr = {}
            while right < len(s):
                ch = s[right]
                ctr[ch] = ctr.get(ch, 0) + 1
                
                if ctr[ch] >= k:

                    res += len(s) - right 
                    right = len(s)
                right += 1
            left += 1
            right = left
        return res


