class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = -1
        else:
            neg = 1
        x = abs(x)
        rev_x = str(x)[::-1]

        int_rev_x = int(rev_x) * neg
        if int_rev_x > 2**31-1 or int_rev_x < -2**31:
            return 0
        else:
            return int_rev_x

        
