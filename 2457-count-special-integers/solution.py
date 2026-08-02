import math
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        pows = [10**n for n in range(1, 10)]
     
        def solve(num):
            digits = len(str(num))
            
            if num < 10:
                return num
            if num in pows:
                
                out =  9 * math.factorial(9) // math.factorial(9 - digits + 2) + solve(num // 10)
                if num == 100:
                    out -= 1
                return out
            s = str(num)

            base = solve(pows[bisect.bisect(pows, num) - 1])
            if num > 10 and num < 100:
                base -= 1
            print("base", base)
            add = 0
            nums = set()
            for idx, ch in enumerate(s):
                cur = int(ch)
                
                if idx == 0:
                    add += (cur - 1) * math.factorial(9) // math.factorial(9 - (digits-idx) + 1)
                    print("idx", idx, "add", (cur - 1) * math.factorial(9) // math.factorial(9 - (digits-idx) + 1))
                else:
                    

                    cur_add = 0
                    for p in range(cur):
                        if str(p) not in nums:
                            cur_add += math.factorial(9-idx) // math.factorial((9-idx) - (digits-idx) + 1)

                    add += cur_add
                 
                    if ch in nums:
                        break
                nums.add(ch)
            if len(set(s)) == digits:
                add += 1

            return base + add
        return solve(n)
