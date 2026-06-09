class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_even = [n%2 == 0 for n in arr]
        num_even = 0
        num_odd = 0
        res = 0
        for n in odd_even:
            if n:
                num_even += 1
            else:
                num_even, num_odd = num_odd, num_even
                num_odd += 1
         
            res += num_odd
            res = res % (10**9+7)
                

        return res
