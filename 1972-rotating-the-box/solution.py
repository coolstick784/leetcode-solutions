# 1. transpose the matrix
# 2. starting at the bottom row, replace the stone with air if the square below is air. continue until there is no air behind or we're at the bottom row

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        transposed = [[None for _ in range(len(boxGrid))] for _ in range(len(boxGrid[0]))]
        num_c = len(boxGrid)
        for r, row in enumerate(boxGrid):
            
            for c, el in enumerate(row):
                transposed[c][num_c - r-1] = el
        lowest = [len(transposed) for _ in range(len(transposed[0]))]

        
        for row in range(len(transposed)-1, -1, -1):
            for col in range(len(transposed[0])):
    
                if transposed[row][col] == "#":

                    bottom = lowest[col] - 1
                    transposed[row][col], transposed[bottom][col] = transposed[bottom][col], transposed[row][col]
                    lowest[col] = bottom
                elif transposed[row][col] == "*":
                    lowest[col] = row
        return transposed
        
