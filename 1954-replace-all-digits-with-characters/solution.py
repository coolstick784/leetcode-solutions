class Solution:
    def replaceDigits(self, s: str) -> str:
        digits = [str(n) for n in range( 10)]
        len_s = len(s)
        res = ""
        for idx, ch in enumerate(s):
            if ch in digits:
                continue
            res += ch
            if (idx+1) < len(s):

                res += chr(ord(ch) + int(s[idx+1]))
                
        return res

        
