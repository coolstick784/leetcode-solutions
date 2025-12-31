class Solution:
    def romanToInt(self, s: str) -> int:
        mapping_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        idx = 0
        out = 0
        while idx < (len(s)):
            next_val = mapping_dict[s[idx]]
            after_next = 0
            if idx < (len(s) - 1):
                after_next = mapping_dict[s[idx+1]]
            if next_val < after_next:
                out -= next_val
            else:
                out += next_val
            idx += 1

        return out
        
