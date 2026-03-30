class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        cols = [-1 for _ in range(len(matrix[0]))]
        for row in matrix: 
            for idx, el in enumerate(row):
                cols[idx] = max(cols[idx], el)
        ans = [[] for _ in range(len(matrix))]
        for r, row in enumerate(matrix):
            for idx, el in enumerate(row):
                if el != -1:
                    ans[r].append(el)
                else:
                    ans[r].append(cols[idx])
        return ans
        

