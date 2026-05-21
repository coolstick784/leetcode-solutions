class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = 0
        max_r = len(matrix) - 1
        max_c = len(matrix[0]) - 1
        min_r = 0
        min_c = 0
        while r>=0 and  r < len(matrix) and c >= 0 and c < len(matrix[0]):

            el = matrix[r][c]
            if el == target:
                return True
            elif el < target:
                if c < max_c:
                    c += 1
                elif r < max_r:
                    r += 1
                else:
                    return False
            elif el > target:
                if c > 0:
                    max_c = c-1
                    c -= 1
                else:
                    max_r = r-1
                    r -= 1

        return False
                
