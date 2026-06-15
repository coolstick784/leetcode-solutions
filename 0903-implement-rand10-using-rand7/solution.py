# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ctr = {}
        low = None
        high = None
        while True:
            n = rand7()
            if n <= 5 and not low:
                low = n
            elif n > 5 and not high:
                high = n
            if low and high:
                break
        return low*2 + high - 6 - 1
    
