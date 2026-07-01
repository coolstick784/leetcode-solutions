"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        @lru_cache(None)
        def allSame(r, c, er, ec):
            if r > er or c > ec:
                return 2 # out of range
    
            down = allSame(r+1, c, er, ec)
            right = allSame(r, c+1, er, ec)
            val = grid[r-1][c-1]
            if (val == down or down == 2) and (val == right or right == 2):
                
                return val
            return -1

        @lru_cache(None)
        def solve(r, c, er, ec):
            print("solve", "r", r, "c", c, "er", er, "ec", ec)
            cur_val = grid[r-1][c-1]
            if (r == er and c == ec) or allSame(r, c, er, ec) != -1:
                print("solved")
                return Node(val=cur_val, isLeaf = True, topLeft = None, topRight = None, bottomLeft = None, bottomRight = None)
            cur_node = Node(val=cur_val, isLeaf = False)
            cur_node.topLeft = solve(r, c, (er-r+1)//2+r-1, (ec-c+1)//2+c-1)
            cur_node.topRight = solve(r, (ec-c+1)//2+c, (er-r+1)//2+r-1, ec)
            cur_node.bottomLeft = solve((er-r+1)//2+r, c, er, (ec-c+1)//2+c-1)
            cur_node.bottomRight = solve((er-r+1)//2+r, (ec-c+1)//2+c, er, ec)
            return cur_node


        return solve(1, 1, len(grid), len(grid))
