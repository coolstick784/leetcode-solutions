class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        l = len(colors) 
        for start in range(len(colors)):
            if colors[start % l] != colors[(start+1) % l] and colors[(start+2) % l] != colors[(start+1)% l]:
                res += 1
        
        return res
