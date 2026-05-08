# a1 + a2 - overlap
# overlap is amount of x overlap * amount of y overlap


# either the min of rectangle 2 is between rectangle 1 or vice versa

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a1 = abs(ax2-ax1) * abs(ay2-ay1)
        a2 = abs(bx2-bx1) * abs(by2-by1)

        overlap_x = 0
        overlap_y = 0
        if bx1 >= ax1 and bx1 <= ax2:
            overlap_x = abs(min(ax2, bx2) - bx1)
        elif ax1 >= bx1 and ax1 <= bx2:
            overlap_x = abs(min(ax2, bx2) - ax1)
        if by1 >= ay1 and by1 <= ay2:
            overlap_y = abs(min(ay2, by2) - by1)
        elif ay1 >= by1 and ay1 <= by2:
            overlap_y = abs(min(ay2, by2) - ay1)
        overlap = overlap_x * overlap_y

        return a1 + a2 - overlap
