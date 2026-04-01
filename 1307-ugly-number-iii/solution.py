class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # find LCM of A and B, A and C, B and C, and A/B/C
        # then we do a binary search between 1 and 2*10*9
        # to get the number of ugly numbers before a number n, we can do 
        # number of multiples of A at or equals + B + C - A and B - B and C - A and C + A and B and C
        # 12 ... 2, 3, 4, 6, 8, 9, 10, 12 ... 6 + 4 + 3 - 2 - 3 - 1 + 1 = 8
        # if it's equal to but not a multiple, subtract the minimum remainder from A/B/C

        def lcm(n1, n2):
            if n2 > n1:
                n1, n2 = n2, n1
            cur = n1
            while cur % n2 != 0 and cur <= 2*10**9:
                cur += n1

            return cur
        
        a_b_lcm = lcm(a, b)
        a_c_lcm = lcm(a, c)
        b_c_lcm = lcm(b, c)
        a_b_c_lcm = lcm(a_b_lcm, c)
        left = 1
        right = 2 * 10 **9

     


        while True:

            med = (left+right) // 2
    
            num_multiples = med // a + med // b + med // c - med // a_b_lcm - med // a_c_lcm - med // b_c_lcm + med // a_b_c_lcm
     
            if num_multiples > n:
                right = med
            elif num_multiples < n:
                left = med+1 
            else:
      
                return med - min([med%a, med%b, med%c])
