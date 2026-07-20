# 1. the queen can be taken by the rook 
# 2. the queen can be taken by the bishop top left
# 2.2 the queen can be taken by the bishop bottom right
# 2.5 THE QUEEN can be taken by the bishop top right
# 2.75 the queen can be taken by the bishop bottom left
# 3. if the bishop moves, the rook can take the queen
# 4. the rook needs to move to take the queen
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if (a == e and f < b and (c != a or d < f or d > b)):
            return 1
        if (a == e and f > b and (c != a or d > f or d < b)):
            return 1
        if (b ==f and e < a and (d != b or c < e or c > a)):
            return 1
        if (b == f and e > a and (d != b or c > e or c < a)):
            return 1
        if (d-c == f-e and e < c and (d-c != b-a or a < e or a > c)):
            return 1
        if (d-c == f-e and e > c and (d-c != b-a or a > e or a < c)):
            return 1
        if (d + c == f + e and e > c and (d + c != b + a or a > e or a < c)):
            return 1
        if (d+c == f + e and e < c and (d+c != b+a or a < e or a > c)):
            return 1

        return 2
