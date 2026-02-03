class Solution:
    def monkeyMove(self, n: int) -> int:
        modulo = 1_000_000_007
        answer = 1
        exponent = 2
        while n:
            if n&1:
                answer *= exponent                
            exponent = (exponent*exponent) % modulo
            n >>= 1
        answer += modulo - 2
        answer %= modulo      
        return answer
