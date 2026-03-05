class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = [[] for _ in range(len(mat[0]))]
        for r in mat:
            for idx, n in enumerate(r):
                cols[idx].append(n)
        col_sums = [sum(l) for l in cols]
        row_sums = [sum(l) for l in mat]
        res = 0
        for i, r in enumerate(mat):
            for i2, el in enumerate(r):
                if el == 1 and col_sums[i2] == 1 and row_sums[i] == 1:
                    res += 1
        return res
        
