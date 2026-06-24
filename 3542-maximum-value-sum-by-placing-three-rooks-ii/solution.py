# 1. what's the best if a row and col are removed
# 2. what's the best 2 if a row and col are removed

from collections import deque
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        best_1 = [] # (value, r1, c1, r2, c2)
        vals = [] # (value, r, c)
        for r, row in enumerate(board):
            for c, el in enumerate(row):
                vals.append((el, r, c))
        vals.sort()
        vals.reverse()
        l = len(board)
        w = len(board[0])
        vals = vals[:(w+l) * 3]
        top_3 = set([(r, c) for val, r, c in vals])
        for r, row in enumerate(board):
            for c, el in enumerate(row):
                if (r, c) not in top_3:
                    continue
                idx = 0
                ctr = 0
                while idx < len(vals) and ctr <(len(board) + len(board[0])):
                    while vals[idx][1] == r or vals[idx][2] == c:
                        idx += 1
                        if idx >= len(vals):
                            break
                    if idx >= len(vals):
                        break
                    best_1.append((vals[idx][0] + el, r, c, vals[idx][1], vals[idx][2]))
                    idx += 1
                    ctr += 1

        
        best_1.sort()
        best_1.reverse()
        best_1 = best_1[:1000]
        rows = []
        cols = []
        rows2 = []
        cols2 = []
        prev_row = None
        prev_col = None
        pr2 = None
        pc2 = None
        for idx, t in enumerate(best_1):
            v, r1, c1, r2, c2 = t
            if r1 != prev_row:
                prev_row = r1
                rows.append(idx)
            if c1 != prev_col:
                prev_col = c1
                cols.append(idx)
            if r2 != pr2:
                pr2 = r2
                rows2.append(idx)
            if c2 != pc2:
                pc2 = c2
                cols2.append(idx)

        
        res = -float('inf')
        for r, row in enumerate(board):
            for c, el in enumerate(row):
                idx= 0
                b1 = best_1[idx]
                row_idx = 0 
                col_idx = 0
                r2_idx = 0
                c2_idx = 0
                while idx < len(best_1)-1 and (b1[1] == r or b1[2] == c or b1[3] == r or b1[4] == c):
                    # if b1[1] == r:
                        
                    #     while  idx >= rows[row_idx]:
                    #         row_idx += 1
                    #     idx = rows[row_idx]
                    # elif b1[2] == c:
           
                    #     while col_idx < len(cols) and idx >= cols[col_idx]:
                    #         col_idx += 1
                    #     idx = cols[col_idx]
                    # elif b1[3] == r:
                    #     while idx >= rows2[r2_idx]:
                    #         r2_idx += 1
                    #     idx = rows2[r2_idx]
                    # else:
                    #     while idx >= cols2[c2_idx]:
                    #         c2_idx += 1
                    #     idx = cols2[c2_idx]
                    idx += 1
                    b1 = best_1[idx]
                if not (b1[1] == r or b1[2] == c or b1[3] == r or b1[4] == c):
                    res = max(res, el + b1[0])
        return res
                



