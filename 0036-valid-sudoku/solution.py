class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check_row(board):
            for row in board:
                non_blank = [el for el in row if el != '.']
                if len(list(set(non_blank))) != len(non_blank):
                    return False
            return True
        def check_col(board):
            cur_col = []
            for col in range(9):
                cur_col = [row[col] for row in board]

                non_blank = [el for el in cur_col if el != '.']
                if len(list(set(non_blank))) != len(non_blank):
                    return False
            return True
        def check_box(board):
            for left in range(0, 9, 3):
                for upper in range(0, 9, 3):
                    cur_box = []
                    for col in range(left, left+3):
                        for row in range(upper, upper+3):
                            cur_box.append(board[row][col])
                    non_blank = [el for el in cur_box if el != '.']
                    if len(list(set(non_blank))) != len(non_blank):
                        return False
            return True
        if check_row(board) and check_col(board) and check_box(board):
            return True
        else:
            return False
            
