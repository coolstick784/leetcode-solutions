class Solution:
    def checkRecord(self, s: str) -> bool:
        ctr = Counter(s)
        if ctr.get('A', 0) >= 2:
            return False
        l_ctr = 0
        for ch in s:
            if ch == "L":
                l_ctr += 1
            else:
                l_ctr = 0
            if l_ctr == 3:
                return False
        return True
        
        
