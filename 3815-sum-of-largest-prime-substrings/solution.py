class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        # WRITE A FUNCTION TO FIND NUMBER IS PRIME IT MUST TAKE LESS TIME
        def is_prime(n):
            if n < 2:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        # TAKE SET TO REDUCE REPITAIONS IF EXIST
        l=set()
        for i in range(len(s)):
            a=''
            for j in range(i,len(s)):
                a+=s[j]
                # CHECK IF SUBSTRING IS PRIME
                if is_prime(int(a)):

                    # TAKE INTO SET IF PRIME
                    l.add(int(a))
        k=list(l)
        # IF LENGTH IS LESS THAN 3 ANSWER IS SUM
        if len(k)<=3:
            return sum(k)
        # SORT IT TO GET MAXIMUM THREE TO LAST OF LIST
        k.sort()
        # RETURN SUM OF LAST THREE ELEMENTS
        return k[-1]+k[-2]+k[-3]
# PLEASE UP VOTE
# PLEASE UP VOTE
# PLEASE UP VOTE
# PLEASE UP VOTE
