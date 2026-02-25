class Solution:
    def romanToInt(self, s: str) -> int:
        map_dict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        idx = 0
        
        while idx < len(s):
            ch = s[idx]
            if idx < len(s) - 1:
                if map_dict[ch] < map_dict[s[idx+1]]:
                    res += map_dict[s[idx+1]] - map_dict[ch]
                    idx += 2
                else:
                    res += map_dict[ch]
                    idx += 1
            else:
                res += map_dict[ch]
                idx += 1

        return res
