# to get our answer, it's sum of everything below/right of top left - everything below/right of first row, last col + 1 - everything below/right of first col, last row + 1 + everything below/right of col+1, row+1
# to get sum below/right, it's sum below/right of row + 1, col + 1 + sum right + sum below


# sumRight = 6
# sumBelow = 3
# sumBelowRight = 13  - 17 + 11  + 4 
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        sumBelow = {}
        sumRight = {}
        sumBelowRight = {}
        for r in range(len(matrix)-1, -1, -1):
            for c in range(len(matrix[0])):
                sumBelow[(r-1, c)] = sumBelow.get((r, c), 0) + matrix[r][c]
        for c in range(len(matrix[0])-1, -1, -1):
            for r in range(len(matrix)):
                sumRight[(r, c-1)] = sumRight.get((r, c), 0) + matrix[r][c]
        for r in range(len(matrix)-1, -1, -1):
            for c in range(len(matrix[0])-1, -1, -1):
                sumBelowRight[(r,c)] = sumBelowRight.get((r+1, c+1), 0) + sumRight.get((r, c), 0) + sumBelow.get((r, c), 0) + matrix[r][c]
        self.sumBelowRight = sumBelowRight


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumBelowRight.get((row1, col1), 0) - self.sumBelowRight.get((row1, col2+1), 0) - self.sumBelowRight.get((row2+1, col1), 0) + self.sumBelowRight.get((row2+1, col2+1), 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
