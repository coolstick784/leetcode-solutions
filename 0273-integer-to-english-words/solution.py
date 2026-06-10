class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        manual = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        def solve(cur):
            
            if cur < 20:
                return [manual[cur]]
            elif cur < 100:
                out= [tens[cur//10]] 
                if cur % 10 != 0:
                    out += [manual[cur % 10]]
            else:
                out = [manual[cur//100]] + ["Hundred"]
                if cur % 100 != 0:
                    out += solve(cur % 100)
            return out

            


  
        res = solve(num % 1000) if num % 1000 != 0 else []
        num = num // 1000
        if num and num % 1000 != 0:
            res = ["Thousand"] + res
            res = solve(num % 1000) + res


        num = num // 1000
    
        if num and num % 1000 != 0:
            res = ["Million"] + res

            res = solve(num % 1000) + res


        num = num // 1000
        if num:
            res = ["Billion"] + res
        
            res = solve(num) + res
        return " ".join(res)
        

