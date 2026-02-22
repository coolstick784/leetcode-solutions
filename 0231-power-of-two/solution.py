class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powers = []
        for i in range(31):
            powers.append(2**i)
        if n in powers:
            return True
        return False

