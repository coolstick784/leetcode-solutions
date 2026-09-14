class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        c1 = pattern[0]
        c2 = pattern[1]
        base = 0
        ct_c1 = 0
        ct_c2 = 0
        if c1 == c2:
            ct = text.count(c1)
            return int(ct * (ct+1)/2)
        for idx, ch in enumerate(text):
            if ch == c1:
                ct_c1 += 1
            elif ch == c2:
                base += ct_c1
                ct_c2 += 1
        return max(base + ct_c1, base + ct_c2)

            
            
