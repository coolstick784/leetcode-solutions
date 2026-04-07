class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. find all common factors of len1 and len2
        # 2. check if those are repeating
        
        def find_all_factors(len1, len2):
            max_val = min(len1, len2)
            out = []
            for n in range(1, max_val+1):
                if len1 % n == 0 and len2 % n == 0:
                    out.append(n)
            return out
        
        def check_repeating(substr, len1, len2):
            mul_1 = len1 // len(substr)
            mul_2 = len2 // len(substr)
            if substr * mul_1 == str1 and substr * mul_2 == str2:
                return True
            return False
        factors = find_all_factors(len(str1), len(str2))
        res = ""
        for factor in factors:
            substr = str1[:factor]
            if check_repeating(substr, len(str1), len(str2)):
                res = substr
        return res
                
