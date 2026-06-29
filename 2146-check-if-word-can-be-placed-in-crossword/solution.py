class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:

        for r, row in enumerate(board):
            idx = 0
            for c, el in enumerate(row):
                if idx >= len(word) and el != '#':
                    idx += 1
                elif idx != -float('inf') and idx < len(word) and (el == word[idx] or el == ' '):
                    idx += 1
                elif el != '#' and idx != -float('inf') and idx < len(word) and el != word[idx]:
                    idx = -float('inf')
                elif el == '#':
                    idx = 0
                if idx == len(word) and (c == len(board[0]) - 1 or board[r][c+1] == '#'):
                    return True
        for c in range(len(board[0])):
            idx = 0
            for r in range(len(board)):
                el = board[r][c]
                if idx >= len(word) and el != '#':
                    idx += 1
                elif idx != -float('inf') and idx < len(word) and (el == word[idx] or el == ' '):
                    idx += 1
                elif el != '#' and idx != -float('inf') and idx < len(word) and el != word[idx]:
                    idx = -float('inf')
                elif el == '#':
                    idx = 0
                if idx == len(word) and (r == len(board) - 1 or board[r+1][c] == '#'):
                    return True
        for c in range(len(board[0])):
            idx = 0
            for r in range(len(board)-1, -1, -1):
                el = board[r][c]
                if idx >= len(word) and el != '#':
                    idx += 1
                elif idx != -float('inf') and idx < len(word) and (el == word[idx] or el == ' '):
                    idx += 1
                elif el != '#' and idx != -float('inf') and idx < len(word) and el != word[idx]:
                    idx = -float('inf')
                elif el == '#':
                    idx = 0
               
                if idx == len(word) and (r == 0 or board[r-1][c] == '#'):
                    return True
        for r, row in enumerate(board):
            idx = 0
            for c in range(len(board[0])-1, -1, -1):
                el = board[r][c]
                if idx >= len(word) and el != '#':
                    idx += 1
                elif idx != -float('inf') and idx < len(word) and (el == word[idx] or el == ' '):
                    idx += 1
                elif el != '#' and idx != -float('inf') and idx < len(word) and el != word[idx]:
                    idx = -float('inf')
                elif el == '#':
                    idx = 0
                print("idx", idx, "r", r, "c", c)
                if idx == len(word) and (c == 0 or board[r][c-1] == '#'):
                    return True
        return False
