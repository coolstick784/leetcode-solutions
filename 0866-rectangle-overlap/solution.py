class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # they overlap if any of the following apply:
        # 1. x start from rec2 is between x in rec1 AND 3 or 4
        # 2. x end from rec2 is between x in rec1 AND 3 or 4
        # 3. y start from rec2 is between y in rec1 AND 1 or 2
        # 4. y end from rec2 is between y in rec1 AND 1 or 2
        if rec1 == rec2:
            return True

        x_cond_1 = rec2[0] > rec1[0] and rec2[0] < rec1[2]
        x_cond_2 = rec2[2] > rec1[0] and rec2[2] < rec1[2]
        y_cond_1 = rec2[1] > rec1[1] and rec2[1] < rec1[3]
        y_cond_2 = rec2[3] > rec1[1] and rec2[3] < rec1[3]

        x_cond_3 = rec1[0] > rec2[0] and rec1[0] < rec2[2]
        x_cond_4 = rec1[2] > rec2[0] and rec1[2] < rec2[2]
        y_cond_3 = rec1[1] > rec2[1] and rec1[1] < rec2[3]
        y_cond_4 = rec1[3] > rec2[1] and rec1[3] < rec2[3]
        if (x_cond_1 or x_cond_2 or x_cond_3 or x_cond_4) and (y_cond_1 or y_cond_2 or y_cond_3 or y_cond_4):
            return True
        return False
        
