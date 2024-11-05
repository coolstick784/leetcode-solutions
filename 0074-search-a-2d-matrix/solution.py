from collections import Counter
class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for el in row:
                if el == target:
                    return True
        return False

                    
        
        
        
