from collections import Counter
class Solution(object):
    def setZeroes(self, matrix):
        cols = [[r[idx] for r in matrix] for idx in range(len(matrix[0]))]
        rows = [r for r in matrix]
        for r_idx, r in enumerate(matrix):
            for c_idx, el in enumerate(r):
                if el == 0:
                    cols[c_idx] = [0 for _ in range(len(matrix))]
                    rows[r_idx] = [0 for _ in range(len(matrix[0]))]
        out = matrix.copy()
        for r_idx, r in enumerate(out):
            for c_idx, el in enumerate(r):
                if cols[c_idx] == [0 for _ in range(len(matrix))]:
                    out[r_idx][c_idx] = 0
                elif rows[r_idx] == [0 for _ in range(len(matrix[0]))]:
                    out[r_idx][c_idx] = 0
        return out
                    
        
        
        
