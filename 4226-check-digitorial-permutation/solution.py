# get the sum of its factorials
# figure out if that sum is a permutation of the original
# to get the sum of its factorials, we can first drop each number by hard dividing by 10, and then the remainder is the digit
# then, we convert that sum to a string
# then, we convert that string to a counter, where we have the counter of each digit
# then, we check if that coutner is equal to the original n (as a string)'s counter
# we don't have to worry about 0 counting since n >= 1

from collections import Counter
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def factorial(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            return n * factorial(n-1)
        sum_factorials = 0
        cur_n = n
        while cur_n > 0:
            mod = cur_n % 10
            sum_factorials += factorial(mod)
            cur_n = cur_n // 10
        ctr_sum = Counter(str(sum_factorials))
        ctr_og = Counter(str(n))
        if ctr_og == ctr_sum:
            return True
        return False
        
