class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # convert each digit to an integer by doing a subtraction of its ord from 0
        # then, fill in the smaller number (in terms of digits) with leading zeros
        # add them right to left, and carry the remainder
        # add the final remainder to the start
        
        while len(num1) < len(num2):
            num1 = "0" + num1
        while len(num2) < len(num1):
            num2 = "0" + num2
        res = ""
        rem = 0
        for idx in range(len(num1)- 1, -1, -1):
            cur_n1 = ord(num1[idx]) - ord("0")
            cur_n2 = ord(num2[idx]) - ord("0")
            total = cur_n1 + cur_n2 + rem
            if total >= 10:
                rem = 1
                total -= 10
            else:
                rem = 0
            res = str(total) + res
        if rem == 1:
            res = "1" + res
        return res
            
