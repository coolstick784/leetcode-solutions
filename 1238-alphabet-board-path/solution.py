class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        idxs = {}
        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                idxs[ch] = (r, c)
        def solve(start, idx):
            res = []
            if idx == len(target):
                return []
            r, c = idxs[start]
            r2, c2 = idxs[target[idx]]

            if r > r2:
                for _ in range(r-r2):
                    res.append("U")
            if c > c2:
                for _ in range(c-c2):
                    res.append("L")
            else:
                for _ in range(c2-c):
                    res.append("R")
            if r < r2:
                for _ in range(r2-r):
                    res.append("D")

            res.append("!")
            return res + solve(target[idx], idx+1)

        return "".join(solve("a", 0))
        

