# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# We want the row # and col #
# If we're at the edge/another number is to the right and moving right, go down
# If we're moving left and at the edge/another number is to the left, go up
# If we're moving down and we're at the edge/another number is down, go left
# If we're moving up and we're at the edge/another number is up, go right
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(m)]
        cur_cell = (1, 1)
        dirs = ["right", "down", "left", "up"]
        cur_dir = "right"
        done = 0
        def is_valid(pot_next):
            row, col = pot_next
            if row > m or col > n or res[row-1][col-1] is not None:
                return False
            return True
        def getPotNext(cur_dir, cur_row, cur_col):
            if cur_dir == "right":
                pot_next = (cur_row, cur_col+1)
            elif cur_dir == "down":
                pot_next = (cur_row+1, cur_col)
            elif cur_dir == "left":
                pot_next = (cur_row, cur_col-1)
            else:
                pot_next = (cur_row-1, cur_col)

            return pot_next
        cur = head
        while done < (m*n):
            cur_row = cur_cell[0]
            cur_col = cur_cell[1]

            if cur is not None:
                res[cur_row-1][cur_col-1] = cur.val
                cur = cur.next
            else:
                res[cur_row-1][cur_col-1] = -1

            
            done += 1
            
            
            pot_next = getPotNext(cur_dir, cur_row, cur_col)
            if not is_valid(pot_next):
                cur_dir= dirs[(dirs.index(cur_dir) + 1) % 4]
                pot_next = getPotNext(cur_dir, cur_row, cur_col)
            
            cur_cell = pot_next
                 

        return res
        

        
