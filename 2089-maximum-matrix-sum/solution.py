class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        num_neg = 0
        num_pos = 0
        total = 0
        min_val = 10**7
        for m in matrix:
            for n in m:
                if n < 0:
                    num_neg += 1
                elif n > 0:
                    num_pos += 1
                total += abs(n)
                if abs(n) < min_val:
                    min_val = abs(n)
        if num_neg == num_pos or num_neg == 0 or num_neg % 2 == 0:
            return total
        else:
            return total - min_val*2

        
