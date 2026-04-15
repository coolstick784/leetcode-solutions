# get the count of each digit
# if it's even, add that //2 to our total
# if our total is < len(num), add 1 for the middle
# if it's all 0s, return 0

class Solution:
    def largestPalindromic(self, num: str) -> str:
        ctr = Counter(num)
  
        start = ""
        sorted_digits = [int(d) for d in ctr.keys()]
        sorted_digits.sort()
        sorted_digits.reverse()
        middle = -1
        for digit in sorted_digits:

            if ctr[str(digit)] % 2 == 1:
                middle = max(middle, digit)
            start += str(digit) * (ctr[str(digit)] // 2)
        
  
        end = list(start)
        end.reverse()
        if middle == -1:
            middle = ""
        res = start + str(middle) + "".join(end)

        while res and res[0] == "0":
            res = res[1:-1]
        if not res:
            return "0"
        
        return res


# "444947137"
# 9: 1 7: 2 4: 4 3:1 1: 1
# [9, 7, 4, 3, 1]
# "" "9"
# "7" "9"
# "744" "9"
# "744" "9" 


