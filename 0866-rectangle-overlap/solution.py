# if (the second rectangle's max x is between the x limits of the first ,or the second rectangle min x is between the x limits of the first
# or the first rectangle's...)
# same with y

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        first_min_x = rec1[0]
        first_max_x = rec1[2]
        first_min_y = rec1[1]
        first_max_y = rec1[3]
        second_min_x = rec2[0]
        second_max_x = rec2[2]
        second_min_y = rec2[1]
        second_max_y = rec2[3]
        if ((first_min_x < second_max_x and first_min_x > second_min_x) or \
        (first_max_x < second_max_x and first_max_x > second_min_x) or \
        (second_min_x < first_max_x and second_min_x > first_min_x) or \
        (second_max_x < first_max_x and second_max_x > first_min_x) or \
           (first_max_x == second_max_x and first_min_x == second_min_x)) and \
        ((first_min_y < second_max_y and first_min_y > second_min_y) or\
        (first_max_y < second_max_y and first_max_y > second_min_y) or\
        (second_min_y < first_max_y and second_min_y > first_min_y) or\
        (second_max_y < first_max_y and second_max_y > first_min_y) or \
           (first_max_y == second_max_y and first_min_y == second_min_y)) :
            return True
        return False
        
