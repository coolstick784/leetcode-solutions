class Solution:
    def canWinNim(self, n: int) -> bool:
        # The goal is to get it to 4, with the other person drawing
        # n between 1 and 3 -> you win
        # n = 4 -> you lose
        # n = 5 -> you win
        # n = 6 -> you win 
        # n = 7 -> you win 
        # n = 8 -> you lose
        if n % 4 == 0:
            return False
        return True
        
