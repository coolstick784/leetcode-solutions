# at each index, 

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_even = []
        for n in nums:
            if n % 2 == 0:
                odd_even.append(True)
            else:
                odd_even.append(False)
        ts = odd_even.count(True)
        fs = odd_even.count(False)
        ending_false = 0
        ending_true = 0
        for val in odd_even:
            if val == True:
                ending_true = ending_false + 1
            else:
                ending_false = ending_true + 1




        return max([ts, fs, ending_false, ending_true])
