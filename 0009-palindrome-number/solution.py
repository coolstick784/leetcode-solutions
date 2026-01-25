class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        r = 0
        tmp = x
        r_nums = []
        while tmp > 0:
            last_num = tmp % 10
            tmp = int(tmp/10)
            r_nums.append(last_num)
        
        cur_p = len(r_nums) - 1
        idx = 0
        while cur_p >= 0:
            r += 10 ** cur_p * r_nums[idx]
            idx  += 1
            cur_p -= 1
        print(r_nums)

        

        
        if r == x:
            return True
        return False
