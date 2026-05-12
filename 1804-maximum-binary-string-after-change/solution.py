# 1100 -> 1010 -> 1001 -> 0101 -> 0011 -> 1011
# 1100 -> 1010 -> 1001 -> 1101 
# 1100 -> 1110

# if it's a 1, we don't want to mess with it
# if it's a 0, we want to do whatever we can to make it a 1 using only that and the digits to the right
# if the next digit is 0, easy, make it 1
# if the next digit is 1, 

# 0110 -> 0101 -> 0011 -> 1011
# if it's a zero, find the next zero. that index becomes 1, the zero index becomes 1, and the idx + 1 becomes 0
# 010
# 001
# 101

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        left = 0
        next_zero = 0
        res = []
        binary = list(binary)
        is_zero = False
        while left < len(binary):
            cur = binary[left]


            if cur == "1":
                res.append("1")
                left += 1

                continue
            next_zero = max(next_zero+1, left+1)
            while next_zero < len(binary) and binary[next_zero] == "1":
                next_zero += 1

            if next_zero < len(binary) and next_zero == left + 1:
                res.append("1")
                
      
                left += 1
  
            elif next_zero < len(binary):
                res.append("1")
                binary[left+1] = "0"
                binary[next_zero] = "1"
                left += 1
            else:
                res.append("0")
                left += 1


        
        return "".join(res)

