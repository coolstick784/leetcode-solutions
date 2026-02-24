class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pows = [2**i for i in range(-31, 32)]
        if n in pows:
            return True
        return False
