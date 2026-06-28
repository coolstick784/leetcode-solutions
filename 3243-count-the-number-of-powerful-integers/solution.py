class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        


        def findRes(curEnd, s):
            if int(s) > curEnd:
                return 0

            s = [i for i in s]
            curEnd2 = [i for i in str(curEnd)]
            s_digit_min = len(curEnd2) - len(s) 
            curEnd_match = int("".join(curEnd2[s_digit_min:]))
            s_match = int("".join(s))
            if curEnd_match >= s_match:
                curEnd = [int(i) for i in curEnd2[:s_digit_min]] + [int(i) for i in s]
                
            else:
                p1 = int("".join(curEnd2[:s_digit_min]))-1
                curEnd = [int(i) for i in str(p1)] + [int(i) for i in s]

            s = [int(i) for i in s]
            
     
            num_digits = len(str(curEnd))       
            s_digit_min = len(curEnd) - len(s)  
            @lru_cache(None)
            def solve(digit_no, first_part_matches):
                nonlocal s_digit_min
                nonlocal num_digits
                out = 0
                if digit_no > s_digit_min:
                    return 1
                if first_part_matches and curEnd[digit_no-1] <= limit:
                    out += solve(digit_no+1, True)
                    out += curEnd[digit_no-1] * solve(digit_no+1, False)
                else:
                    out += (limit + 1) * solve(digit_no+1, False)
                    
              
                return out 
            return solve(1, True)
        
        res = findRes(finish, s)
        res -= findRes(start-1, s)
        return res

