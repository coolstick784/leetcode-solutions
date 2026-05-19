class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        islands = {}
        explored = set()
        def dfs(row, col, prev):
            if (row, col) in explored or row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            explored.add((row, col))
            if board[row][col] == 'X':
                return
            islands[prev][0].add((row, col))
            if row == 0 or row == len(board) -1 or col == 0 or col == len(board[0])  -1:
                islands[prev][1] = True
            dfs(row-1, col, prev)
            dfs(row+1, col, prev)
            dfs(row, col+1, prev)
            dfs(row, col-1, prev)
        for r, row in enumerate(board):
            for c, el in enumerate(row):
                
                if (r, c) in explored:
                    continue
                explored.add((r, c))
                if el == 'O':
                    if r == 0 or r == len(board) -1 or c == 0 or c == len(board[0])  -1:

                        islands[(r, c)] = [set({(r, c)}), True]
                    else:
                        islands[(r, c)] = [set({(r, c)}), False]
                    dfs(r-1, c, (r, c))
                    dfs(r+1, c, (r, c))
                    dfs(r, c-1, (r, c))
                    dfs(r, c+1, (r, c))
        print("islands", islands)
        for i in islands:
            cur = islands[i]
            if not cur[1]:
                for r, c in cur[0]:
                    board[r][c] = 'X'
