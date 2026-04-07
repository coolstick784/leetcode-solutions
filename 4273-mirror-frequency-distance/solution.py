class Solution:
    def mirrorFrequency(self, s: str) -> int:
        orig = {} 
        map_dict = {}
        mirrored = {} # only account for first 13
        orig = Counter(s)
        for n in range(26):
            
            map_dict[chr(ord('a') + n)] = chr(ord('z') - n)
            if n < 10:
                
                map_dict[str(n)] = str(9-n)
        for n in range(13):
            cur_ch = chr(ord('a') + n)
            mirrored[cur_ch] = orig[map_dict[cur_ch]]
            if n < 5:
                mirrored[str(n)] = orig[map_dict[str(n)]]
        res = 0
        for ch in mirrored:
            res += abs(mirrored[ch] - orig[ch])
 
        return res
