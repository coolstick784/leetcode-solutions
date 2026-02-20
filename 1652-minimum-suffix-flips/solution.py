class Solution:
    def minFlips(self, target: str) -> int:
        res = 0

        
        left = 0 
        next_char = "0"
        while left < len(target):

            if next_char != target[left]:
                res += 1
            left += 1
            next_char = "1" if res % 2 else "0"
            
        return res
