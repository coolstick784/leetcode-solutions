class Solution(object):
    
    def solveSudoku(self, board):
        def get_closest(n):
            return (n // 3) * 3
        
        def is_valid(board, r, c, num):
            for i in range(9):
                if board[r][i] == num or board[i][c] == num:
                    return False
                if board[get_closest(r) + i // 3][get_closest(c) + i % 3] == num:
                    return False
            return True
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(board, r, c, num):
                                board[r][c] = num
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True
        
        solve()
        

