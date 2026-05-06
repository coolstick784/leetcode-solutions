#djisktra's algo
# always take the one costing the least moves
# if it's n^2, thats your ans
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        goal = len(board)**2
        n = len(board)
        heap = [(0, 1)]
        best = [float('inf') for _ in range(goal)]
        @lru_cache(None)
        def get_rc(c):
            row = n - ((c-1)//n+1)
            if (n-row-1) % 2 == 0:
                even = True
            else:
                even = False
            if even:
                col = (c-1) % n 
            else:
                col = n-1 - ((c-1)%n)

            return (row, col)
        @lru_cache(None)
        def return_cell(new, row, col):
            if board[row][col] == -1:
                return new
            else:
                return board[row][col]
        

        @lru_cache(None)
        def get_cell(row, col):
            if (n-row-1) % 2 == 0:
                even = True
            else:
                even = False
            if even:
                return goal - (row*n) - (n-1 - col)
            else:
                return goal - (row*n) - (col)

        while heap:
            cost, cell = heapq.heappop(heap)
            if cell == goal:
                return cost
            if cost >= best[cell-1]:
                continue
            best[cell-1] = cost
            row, col = get_rc(cell)
            for new in range(cell+1, min(cell+6, goal)+1):
                new_row, new_col = get_rc(new)
                heapq.heappush(heap, (cost+1, return_cell(new, new_row, new_col)))
        return -1
