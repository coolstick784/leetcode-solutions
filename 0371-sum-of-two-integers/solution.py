class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = (1 << 32) - 1


        carry = 0
        while b != 0:

            a, carry = (a ^ b) & mask, (a & b) & mask
            b = carry << 1
        if a <= 1<<31-1:
            return a
        return ~(a^mask)
