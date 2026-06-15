class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        order = []
        squares = {}
        rows = {}
        cols = {}

        for r, row in enumerate(board):
            for c, el in enumerate(row):
                sqRow = r // 3
                sqCol = c // 3

                if el == ".":
                    order.append((r, c))
                else:
                    squares.setdefault((sqRow, sqCol), set()).add(el)
                    rows.setdefault(r, set()).add(el)
                    cols.setdefault(c, set()).add(el)

        nums = set(str(n) for n in range(1, 10))

        def get_options(r, c):
            sqRow = r // 3
            sqCol = c // 3
            used = (
                squares.get((sqRow, sqCol), set())
                | rows.get(r, set())
                | cols.get(c, set())
            )
            return nums - used

        def solve(idx):
            if idx == len(order):
                return True

            best = idx
            best_options = None

            for i in range(idx, len(order)):
                r, c = order[i]
                options = get_options(r, c)

                if best_options is None or len(options) < len(best_options):
                    best = i
                    best_options = options

                if len(best_options) == 1:
                    break

            if not best_options:
                return False

            order[idx], order[best] = order[best], order[idx]

            r, c = order[idx]
            sqRow = r // 3
            sqCol = c // 3

            for el in best_options:
                squares.setdefault((sqRow, sqCol), set()).add(el)
                rows.setdefault(r, set()).add(el)
                cols.setdefault(c, set()).add(el)
                board[r][c] = el

                if solve(idx + 1):
                    return True

                squares[(sqRow, sqCol)].remove(el)
                rows[r].remove(el)
                cols[c].remove(el)
                board[r][c] = "."

            order[idx], order[best] = order[best], order[idx]

            return False

        solve(0)
