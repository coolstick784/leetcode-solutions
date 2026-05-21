# 2: every odd is on
# 3: every multiple of 3 is off except for multiples of 3 and 2
# 4: every multiple of 4 is off except 

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(n**0.5)
        
