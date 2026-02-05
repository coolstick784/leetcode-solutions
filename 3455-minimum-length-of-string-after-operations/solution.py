class Solution:
    def minimumLength(self, s: str) -> int:
        ctr = Counter(s)

        start = len(s)
        for c in ctr:
            len_c = ctr[c]
            
            if len_c % 2 == 0:
                start -= (len_c - 2)
            else:
                start -= (len_c - 1)
        return start
            
        
